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
      <router-link to="/profile" v-if="authData.isLogin">
        <font-awesome-icon :icon="['fas', 'user']" />
        プロフィール
      </router-link>
      <router-link to="/settings" v-if="authData.isLogin">
        <font-awesome-icon :icon="['fas', 'gear']" />
        設定
      </router-link>
      <router-link to="/login" v-if="!authData.isLogin">
        <font-awesome-icon :icon="['fas', 'sign-in-alt']" />
        ログイン
      </router-link>
      <router-link to="/register" v-if="!authData.isLogin">
        <font-awesome-icon :icon="['fas', 'user-plus']" />
        登録
      </router-link>
      <router-link @click="authData.logout()" to="/" v-if="authData.isLogin">
        <font-awesome-icon :icon="['fas', 'sign-out-alt']" />
        ログアウト
      </router-link>
    </div>
  </div>
</template>

<style scoped>
img {
  width: 3%;
  filter: invert(100%);
}

.account-menu-container {
  position: fixed;
  top: 6%;
  right: 1%;
  z-index: 1000;
  border-radius: 10px;
  padding: 15px;
  background: rgba(0, 0, 0, 0.8);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  color: white;
  animation: fadeIn 0.3s ease-out;
}

.menu {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.menu a {
  color: white;
  text-decoration: none;
  font-size: 16px;
  padding: 8px 12px;
  border-radius: 5px;
  transition: background 0.3s, color 0.3s;
}

.menu a:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #ffd700;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
