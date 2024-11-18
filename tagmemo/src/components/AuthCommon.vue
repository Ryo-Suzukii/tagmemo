<script lang="ts">
import { defineStore } from 'pinia';

export const useAuthData = defineStore("authData",{
  state: () => ({
    isError: false,
    isLogin: false,
    isLoginCheck: false,
    email: "",
    user_id: "",
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
