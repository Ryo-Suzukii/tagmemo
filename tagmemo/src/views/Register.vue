<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';

import { useAuthData } from '../stores/AuthCommon';

const { t } = useI18n();
const authData = useAuthData();
const router = useRouter();
const handleRegister = () => {
  const userNameInput = document.querySelector('input[type="text"]') as HTMLInputElement;
  const emailInput = document.querySelector('input[type="email"]') as HTMLInputElement;
  const passwordInput = document.querySelectorAll('input[type="password"]')[0] as HTMLInputElement;
  const rePasswordInput = document.querySelectorAll('input[type="password"]')[1] as HTMLInputElement;
  const userName = userNameInput.value;
  const email = emailInput.value;
  const password = passwordInput.value;
  const rePassword = rePasswordInput.value;
  const userColor = Math.floor(Math.random() * 16777215).toString(16);
  if (password !== rePassword) {
    alert('Password does not match');
    return;
  }
  const url = import.meta.env.VITE_API_BASE_URL + '/live/dev-tagmemo-api-Function-Auth?user_id=' + userName + '&mail_address=' + email + '&password=' + password + '&color=' + userColor + '&mode=register';
  console.log(url);
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
        alert('Registration failed [401]');
      } else if (response.status == 200) {
        authData.isError = false;
        authData.isLogin = true;
        authData.isLoginCheck = true;
        setTimeout(() => {
          authData.isLoginCheck = false;
        }, 3000);
        authData.email = email;
        authData.userId = userName;
        authData.userColor = `#${userColor}`;
        console.log(authData.userColor);
        router.push({ name: 'home' });
      } else {
        alert(`Registration failed ${response.status}`);
      }
    })
};
</script>

<template>
  <div class="page-container">
    <h1>{{ t("registerPage.register") }}</h1>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label>{{  t("registerPage.username") }}</label>
        <input type="text" required />
      </div>
      <div class="form-group">
        <label>{{  t("registerPage.email") }}</label>
        <input type="email" required />
      </div>
      <div class="form-group">
        <label>{{ t("registerPage.password")}}</label>
        <input type="password" required />
      </div>
      <div class="form-group">
        <label>{{ t("registerPage.re_password")}}</label>
        <input type="password" required />
      </div>
      <button type="submit">{{  t("registerPage.register") }}</button>
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
