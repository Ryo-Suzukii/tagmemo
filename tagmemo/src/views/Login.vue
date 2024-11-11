<script setup lang="ts">
import { useI18n } from 'vue-i18n';
const { t } = useI18n();
const handleLogin = () => {
  // ログイン処理をここに実装
  console.log('ログイン処理');
};
</script>

<template>
  <div class="page-container">
    <h1>{{ t("login") }}</h1>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label>{{ t("mail")}}</label>
        <input type="email" required />
      </div>
      <div class="form-group">
        <label>{{ t("password") }}</label>
        <input type="password" required />
      </div>
      <button type="submit">{{ t("login")}}</button>
    </form>
  </div>
</template>
