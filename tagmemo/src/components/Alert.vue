<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { useAuthData } from '../stores/AuthCommon';

const { t } = useI18n();
const authData = useAuthData();
</script>

<template>
  <div class="alert-container">
    <v-alert
      v-if="authData.isError"
      title="Login Failed"
      icon="$error"
      type="error"
      closable
      @click:close="authData.isError = false"
      icon-color="white"
      >
      {{ t("loginPage.error") }}
    </v-alert>
    <v-alert
      v-if="authData.isLoginCheck"
      title="Login Successful"
      icon="$success"
      type="success"
      closable
      @click:close="authData.isLogin = false"
      icon-color="white"
      >
      {{ t("loginPage.success") }}
    </v-alert>
  </div>
</template>

<style scoped>
.alert-container {
  position: fixed;
  margin-top: 8%;
  margin-left: 80%;
  z-index: 1000;
  max-width: 400px;
  animation: fadeInUp 0.5s ease-out;
}

@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(100%);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.v-alert {
  animation: fadeOut 3s;
}

@keyframes fadeOut {
    0% {
      opacity: 1;
    }
    50% {
      opacity: 0.7;
    }
    100% {
      opacity: 0;
    }
}
</style>
