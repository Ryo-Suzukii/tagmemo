<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { useAuthData } from '../components/AuthCommon.vue';

const authData = useAuthData();
const { t } = useI18n();
</script>

<template>
  <div class="page-container" v-if="authData.isLogin">
    <h1>{{ t("title")}}</h1>
    <!-- <p>{{ t("description") }}</p> -->
    <p>ねこちゃん</p>
  </div>
  <div class="page-container" v-if="!authData.isLogin">
    <h1>ようこそ{{ t("title") }}へ！</h1>
  </div>
</template>
