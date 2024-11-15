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
