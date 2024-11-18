<script setup lang="ts">
import { useAuthData } from '../components/AuthCommon.vue';

const authData = useAuthData();
</script>

<template>
  <div class="page-container">
    <h1>Profile</h1>
    <h2>{{ authData.userId }}さんのプロフィール</h2>
    <h3>メールアドレス: {{ authData.email }}</h3>
  </div>
</template>
