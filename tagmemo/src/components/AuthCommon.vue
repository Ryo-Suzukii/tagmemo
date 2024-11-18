<script lang="ts">
import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';

export const useAuthData = defineStore("authData", {
  state: () => ({
    isError: useStorage('authData_isError', false),
    isLogin: useStorage('authData_isLogin', false),
    isLoginCheck: useStorage('authData_isLoginCheck', false),
    email: useStorage('authData_email', ""),
    user_id: useStorage('authData_user_id', ""),
  }),
  actions: {
    logout() {
      this.isError = false;
      this.isLogin = false;
      this.isLoginCheck = false;
      this.email = "";
      this.user_id = "";
    },
  },
})
</script>
