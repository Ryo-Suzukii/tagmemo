<script lang="ts">
import { defineStore } from 'pinia';

export const useAuthData = defineStore("authData",{
  state: () => ({
    isError: false,
    isLogin: false,
    email: "",
  }),
  actions: {
    logout() {
      this.isError = false;
      this.isLogin = false;
      this.email = "";
    },
  },
})
</script>
