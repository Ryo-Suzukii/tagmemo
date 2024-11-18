<script setup lang="ts">
import { useI18n } from 'vue-i18n';

import { useAuthData } from './AuthCommon.vue';

const { locale } = useI18n();
const { t } = useI18n();

const authData = useAuthData();
const onClickOutside = () => {
  authData.showMenu = false;
};

const changeLanguage = (lang: string) => {
  locale.value = lang;
};

</script>

<template>
  <div class="account-menu-container" v-if="authData.showMenu" v-click-outside="onClickOutside">
    <div class="menu">
      <router-link to="/profile" v-if="authData.isLogin">
        <font-awesome-icon :icon="['fas', 'user']" />
        {{ t('accountMenuPage.profile') }}
      </router-link>
      <router-link to="/settings" v-if="authData.isLogin">
        <font-awesome-icon :icon="['fas', 'gear']" />
        {{ t('accountMenuPage.settings') }}
      </router-link>
      <router-link to="/login" v-if="!authData.isLogin">
        <font-awesome-icon :icon="['fas', 'sign-in-alt']" />
        {{  t('login') }}
      </router-link>
      <router-link to="/register" v-if="!authData.isLogin">
        <font-awesome-icon :icon="['fas', 'user-plus']" />
        {{ t('accountMenuPage.register') }}
      </router-link>
      <router-link @click="authData.logout()" to="/" v-if="authData.isLogin">
        <font-awesome-icon :icon="['fas', 'sign-out-alt']" />
        {{ t('accountMenuPage.logout') }}
      </router-link>
      <select @change="event => changeLanguage((event.target as HTMLSelectElement)?.value ?? '')" id="changeLanguage" name="changeLanguage">
        <option value="ja">日本語</option>
        <option value="en">English</option>
      </select>
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

select {
  padding: 0.3rem;
  border-radius: 4px;
  color: #ffffff;
  font-size: 1rem;
  cursor: pointer;
  transition: border-color 0.3s, box-shadow 0.3s;
}

select option {
  background-color: #2b2b2b;
  color: #ffffff;
}

select a {
  color: white;
  text-decoration: none;
  font-size: 16px;
  padding: 8px 12px;
  border-radius: 5px;
  transition: background 0.3s, color 0.3s;
}

select a:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #ffd700;
}
</style>
