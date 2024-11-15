<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import StarryBackground from './components/StarryBackground.vue';

const { locale } = useI18n();

const changeLanguage = (lang: string) => {
  locale.value = lang;
};
</script>

<template>
  <StarryBackground />
  <nav class="nav-links">
    <router-link to="/">Home</router-link>
    <router-link to="/login">Login</router-link>
    <router-link to="/register">Register</router-link>
    <router-link to="/account">Account</router-link>
    <select @change="event => changeLanguage((event.target as HTMLSelectElement)?.value ?? '')" id="changeLanguage" name="changeLanguage">
      <option value="ja">日本語</option>
      <option value="en">English</option>
    </select>
  </nav>
  <router-view></router-view>
</template>

<style scoped>
.nav-links {
  display: flex;
  align-items: center;
  gap: 1rem;
}
select {
  margin-left: auto;
  padding: 0.3rem;
  border-radius: 4px;
  background-color: #2b2b2b;
  color: #ffffff;
  font-size: 1rem;
  cursor: pointer;
  transition: border-color 0.3s, box-shadow 0.3s;
}

select:focus {
  border-color: #646cff;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}

select option {
  background-color: #2b2b2b;
  color: #ffffff;
}
</style>
