<script setup lang="ts">
import { useI18n } from 'vue-i18n';
const { t } = useI18n();
const handleRegister = () => {
  // 登録処理をここに実装
  console.log('登録処理');
};
</script>

<template>
  <div class="page-container">
    <h1>{{ t("register") }}</h1>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label>{{  t("username") }}</label>
        <input type="text" required />
      </div>
      <div class="form-group">
        <label>{{  t("mail") }}</label>
        <input type="email" required />
      </div>
      <div class="form-group">
        <label>{{ t("password")}}</label>
        <input type="password" required />
      </div>
      <div class="form-group">
        <label>{{ t("re_password")}}</label>
        <input type="password" required />
      </div>
      <button type="submit">{{  t("register") }}</button>
    </form>
  </div>
</template>
