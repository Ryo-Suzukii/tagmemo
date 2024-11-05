#!/bin/bash

# functions
login () {
    aws sso login --profile $AWS_PROFILE
    SSO_ACCOUNT=$(aws sts get-caller-identity --query 'Account' --profile $AWS_PROFILE)
}

get_ssm_parameter () {
    aws ssm get-parameter \
        --name $1 \
        --region ap-northeast-1 \
        --profile ${AWS_PROFILE} \
        --query Parameter.Value \
        --output text
}

convert_env_str () {
    local _ENVS=`cat ./cfn_params/param_${ENV}.json | jq -r '.Parameters | to_entries | map("\(.key)=\(.value|tostring)") | .[]'`
    local _SSM_PARAMS=`cat ./cfn_params/param_${ENV}.json | jq -r '.ParameterStore | to_entries | map("\(.key)=\(.value|tostring)") | .[]'`
    local _SSM_PARAMS_ARR=(${_SSM_PARAMS})
    for _SSM_PARAM in ${_SSM_PARAMS_ARR[@]}; do
        local _PARAM_NAME=`echo ${_SSM_PARAM} | cut -d '=' -f 1`
        local _PARAM_VALUE=`echo ${_SSM_PARAM} | cut -d '=' -f 2`
        local _PARAM_VALUE=`get_ssm_parameter ${_PARAM_VALUE}`
        _ENVS="${_ENVS} ${_PARAM_NAME}=${_PARAM_VALUE}"
    done

    echo ${_ENVS}
}

get_function_list () {
    template_file="template.yaml"
    function_list=$(yq '.Resources | to_entries[] | select(.value.Type == "AWS::Serverless::Function") | .key' "$template_file")
    echo "function_name list:"
    for function in $function_list; do
        echo " - $function"
    done
}

build () {
    sam build --config-env ${ENV} --config-file ${CONFIG}
}

deploy () {
    build
    sam deploy \
        --config-file ${CONFIG} \
        --config-env ${ENV} \
        --parameter-overrides $(convert_env_str) \
        --profile ${AWS_PROFILE} \
        --s3-bucket dev-suz-ry-sam-template \
        --s3-prefix tagmemo
}

sync () {
    build
    sam sync \
        --config-env ${ENV} \
        --config-file ${CONFIG} \
        --parameter-overrides $(convert_env_str) \
        --profile ${AWS_PROFILE} \
        --watch
}

local_invoke () {
    if [ $# -lt 2 ]; then
        # get function list
        echo "Usage: ./deploy.sh local [prod|dev] [function_name] [event_file]"
        get_function_list
        exit 1
    fi
    build
    sam local invoke \
        $1 \
        --log-file local_invoke.log \
        --event $2 \
        --profile ${AWS_PROFILE} \
        --parameter-overrides $(convert_env_str) \
        --config-env ${ENV} \
        --config-file ${CONFIG}
    tail -f local_invoke.log | while read LOGLINE
    do
        echo "$LOGLINE" | jq -R -r '. as $raw | try fromjson catch $raw'
    done
}

CONFIG=samconfig.yaml

if [ $# -lt 2 ]; then
    echo "Usage: ./deploy.sh [deploy|sync|local] [prod|dev]"
    exit 1
fi

COMMAND=$1
ENV=$2

if [ ${ENV} = "prod" ]; then
    AWS_PROFILE=prod-tagmemo
elif [ ${ENV} = "dev" ]; then
    AWS_PROFILE=dev-tagmemo
else
    echo "Usage: ./deploy.sh [deploy|sync|local] [prod|dev]"
    exit 1
fi

# check for AWS configuration
SSO_ACCOUNT=$(aws sts get-caller-identity --query 'Account' --profile $AWS_PROFILE)

main () {
    if [ ${#SSO_ACCOUNT} -ne 14 ]; then
        echo "AWS_PROFILE not set"
        echo "Logging in..."
        login
        if [ ${#SSO_ACCOUNT} -ne 14 ]; then
            echo "Login failed"
            exit 1
        fi
    fi

    if [ ${COMMAND} = "deploy" ]; then
        echo "Deploying..."
        deploy
    elif [ ${COMMAND} = "sync" ]; then
        echo "Syncing..."
        sync
    elif [ ${COMMAND} = "local" ]; then
        echo "Running locally..."
        local_invoke $3 $4
    else
        echo "Usage: ./deploy.sh [deploy|sync|local] [prod|dev]"
        exit 1
    fi
}

main $@
