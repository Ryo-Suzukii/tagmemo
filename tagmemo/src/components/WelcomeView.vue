<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconLogin.vue'
import ToolingIcon from './icons/IconTooling.vue'


</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>What "TagMemo"</template>
    <h3 class="no-wrap" style="color: rgb(1,180,122)">TagMemo </h3>
    <span class="no-warp">{{ $t('tagmemo_description_1') }}</span>
    <br />
    <h3 class="no-wrap" style="color: rgb(1,180,122)">TagMemo </h3>
    <span class="no-wrap">{{ $t('tagmemo_description_2') }}</span>
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>{{ $t('login') }}</template>
    {{ $t('login_description') }}
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>{{ $t('settings')}}</template>
    {{ $t('settings_description') }}
  </WelcomeItem>
</template>

<style scoped> 
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}
h2 {
  font-size: 2.4rem;
  margin: 0;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h2,
.greetings h3 {
  text-align: center;
}

.no-wrap {
  display: inline-block;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
