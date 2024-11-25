import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';

export const useAuthData = defineStore("authData", {
  state: () => ({
    isError: useStorage('authData_isError', false),
    isLogin: useStorage('authData_isLogin', false),
    isLoginCheck: useStorage('authData_isLoginCheck', false),
    email: useStorage('authData_email', ""),
    userId: useStorage('authData_userId', ""),
    userColor: useStorage('authData_userColor', ""),
    showMenu: false,
  }),
  actions: {
    logout() {
      this.isError = false;
      this.isLogin = false;
      this.isLoginCheck = false;
      this.email = "";
      this.userId = "";
      this.userColor = "";
    },
  },
});
