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
    <template #heading>Login</template>
    このサービスを利用するにはログインが必要です。
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Setting</template>
    アカウントの設定を行います。(ログインが必要です)
  </WelcomeItem>
</template>
