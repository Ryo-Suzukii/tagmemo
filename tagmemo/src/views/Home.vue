<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { useAuthData } from '../components/AuthCommon.vue';

const authData = useAuthData();
const { t } = useI18n();
</script>

<template>
  <div class="page-container" v-if="!authData.isLogin">
    <h1>{{ t("title")}}</h1>
    <!-- <p>{{ t("description") }}</p> -->
    <p>{{ t("homePage.description") }}</p>
  </div>
  <div class="page-container" v-if="authData.isLogin">
    <h1>{{ authData.userId }}</h1>
    <h1>{{ t("homePage.welcome") }}</h1>
  </div>
</template>

<style scoped>
.page-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;}
</style>
