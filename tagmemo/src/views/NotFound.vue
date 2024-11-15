<script setup lang="ts">
import { useI18n } from 'vue-i18n';

const { t } = useI18n();
</script>

<template>
  <div class="main">
    <h2>{{ t("NotFoundPage.description") }}</h2>
    <h2>{{  t("NotFoundPage.title") }}</h2>
  </div>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 40vh;
}
</style>
