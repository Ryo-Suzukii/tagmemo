from typing import Any, NamedTuple

from decouple import config


def get_env(key: str, cast: type, default: None = None) -> Any:
    return config(key, cast=cast, default=default)


class ConstType(NamedTuple): ...


class EnvType(NamedTuple):
    ENV: str = get_env("ENV", str, "dev")


Const = ConstType()
Env = EnvType()
