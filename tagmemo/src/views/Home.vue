<script setup lang="ts">
import { useI18n } from 'vue-i18n';
const { t } = useI18n();
</script>

<template>
  <div class="page-container">
    <h1>{{ t("title")}}</h1>
    <!-- <p>{{ t("description") }}</p> -->
    <p>ねこちゃん</p>
  </div>
</template>
