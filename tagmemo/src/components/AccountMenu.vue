<script setup lang="ts">
import { useAuthData } from './AuthCommon.vue';

const authData = useAuthData();
const onClickOutside = () => {
  authData.showMenu = false;
};
</script>

<template>
    <div class="account-menu-container" v-if="authData.showMenu" v-click-outside="onClickOutside">
      <div class="menu">
        <router-link to="/profile">プロフィール</router-link>
        <router-link to="/settings">設定</router-link>
        <router-link @click="authData.logout()" to="/">ログアウト</router-link>
      </div>
    </div>
</template>

<style scoped>
.account-menu-container {
  position: fixed;
  top: 6%;
  right: 0;
  z-index: 998;
  border-radius: 5px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.1);
  color: white;
}
.menu {
  display: flex;
  flex-direction: column;
  gap: 10px;
  color: "white";
}
</style>
