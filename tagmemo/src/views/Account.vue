<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { useAuthData } from '../components/AuthCommon.vue';

const authData = useAuthData();
const { t } = useI18n();
</script>

<template>
  <div class="page-container" v-if="authData.isLogin">
    <h2>{{  t("AccountPage.statusLogin") }}</h2>
  </div>
  <div class="page-container" v-if="!authData.isLogin">
    <h2>{{ t("AccountPage.statusNotLogin")}}</h2>
    <RouterLink v-bind:to="{ name: 'login' }">
      <button type="submit">{{ t("login")}}</button>
    </RouterLink>
  </div>
</template>

<style scoped>
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
