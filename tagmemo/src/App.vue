<script setup lang="ts">
import { useAuthData } from './stores/AuthCommon';

import StarryBackground from './components/StarryBackGround.vue';
import Alert from './components/Alert.vue';
import AccountMenu from './components/AccountMenu.vue';

const authData = useAuthData();

const clickMenu = () => {
  authData.showMenu = true;
};
</script>

<template>
  <StarryBackground />
  <Alert />
  <AccountMenu />
  <nav class="nav-links">
    <router-link to="/">Tagmemo</router-link>
  
    <div class="right-container">
      <h1 
        class="userData" 
        :style="{ backgroundColor: authData.userColor || 'gray' }" 
        @click="clickMenu"
        v-if="authData.isLogin && authData.userId">
        {{ authData.userId[0] }}
      </h1>
      <h1 
        class="userData" 
        :style="{ backgroundColor: 'gray' }" 
        @click="clickMenu"
        v-else>
        ?
      </h1>
    </div>
  </nav>
  <router-view></router-view>
</template>

<style scoped>
.nav-links {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.right-container {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.userData {
  border-radius: 50%;
  width: 3rem;
  height: 3rem;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 2rem;
}
</style>
