<script setup lang="ts">
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { useAuthData } from '../components/AuthCommon.vue';

const { t } = useI18n();
const isError = ref(false);
const isLogin = ref(false);
const authData = useAuthData();

const handleLogin = () => {
  const emailInput = document.querySelector('input[type="email"]') as HTMLInputElement;
  const passwordInput = document.querySelector('input[type="password"]') as HTMLInputElement;
  const email = emailInput.value;
  const password = passwordInput.value;
  const url = 'api/live/dev-tagmemo-api-Function-Auth?mail_address=' + email + '&password=' + password + '&mode=login';
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  myHeaders.append("Accept", "*/*");
  myHeaders.append("Host", "6f5dgikzng.execute-api.ap-northeast-1.amazonaws.com");
  myHeaders.append("Connection", "keep-alive");
  myHeaders.append("Access-Control-Allow-Origin", "*");

  var requestOptions: RequestInit = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow' as RequestRedirect,
  };

  fetch(url, requestOptions)
    .then(response => {
      if (response.status == 401) {
        authData.isLogin = false;
        authData.isError = true;
      } else if (response.status == 200) {
        authData.isError = false;
        authData.isLogin = true;
        window.location.href = '/';
      } else {
        authData.isLogin = false;
        authData.isError = true;
      }
    })
  };
</script>

<template>
  <div class="page-container">
    <v-alert
      v-if="authData.isError"
      title="Login Failed"
      icon="$error"
      type="error"
      closable
      @click:close="isError = false"
      icon-color="white"
      >
      {{ t("loginPage.error") }}
    </v-alert>
    <v-alert
    v-if="authData.isLogin"
    title="Login Success"
    icon="$success"
    type="success"
    variant="tonal"
    closable
    @click:close="isLogin = false"
    icon-color="white"
    >
    {{  t("loginPage.success") }}
  </v-alert>
    <h1>{{ t("login") }}</h1>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">{{ t("mail")}}</label>
        <input type="email" id="email" name="email" autocomplete="email" required />
      </div>
      <div class="form-group">
        <label for="password">{{ t("password") }}</label>
        <input type="password" id="password" name="password" required />
      </div>
      <button type="submit">{{ t("login")}}</button>
    </form>
  </div>
</template>

<style scoped>
input {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.5rem;
  border: 1px solid rgb(255, 255, 255);
  border-radius: 0.25rem;
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

button {
  width: 100%;
  padding: 0.75rem;
  background: #646cff;
  color: white;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  transition: background-color 0.3s;
}
</style>
