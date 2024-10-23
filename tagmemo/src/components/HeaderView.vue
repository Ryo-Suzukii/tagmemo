<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const showDropdown = ref(false)

// 言語を変更する関数
const changeLanguage = (lang: string) => {
  locale.value = lang
  showDropdown.value = false
}

const toggleDropdown = () => {
  showDropdown.value = !showDropdown.value
}
</script>

<template>
  <div class="header">
    <h1>Header</h1>
  </div>
    <div class="language-selector">
      <button @click="toggleDropdown">{{ $t('select_language') }}</button>

      <div v-if="showDropdown" class="dropdown-menu">
        <ul>
          <li @click="changeLanguage('ja')">日本語</li>
          <li @click="changeLanguage('en')">English</li>
        </ul>
      </div>
    </div>
    <div class="wrapper">
      <HederView/>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </nav>
    </div>
</template>

<style scoped>
.header {
  line-height: 1.5;
  max-height: 100vh;
  position: relative;
  text-align: center;
}

nav {
  width: 100%;
  font-size: 20px;
  text-align: center;
  margin-top: 0.5rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 5px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.language-selector {
  position: absolute;
  top: 2%;
  right: 2%;
  display: inline-block;
  margin-top: 10px;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: rgb(27, 77, 124);
  border: 1px solid #ccc;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.dropdown-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.dropdown-menu li {
  padding: 8px 12px;
  cursor: pointer;
  white-space: nowrap;
}

.dropdown-menu li:hover {
  background-color: #09022b;
}

</style>
