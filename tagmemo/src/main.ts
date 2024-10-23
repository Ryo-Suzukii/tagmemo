import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'

import App from './App.vue'
import router from './router'

import ja from '@/locales/ja.json'
import en from '@/locales/en.json'

const i18n = createI18n({
  locale: 'ja',
  fallbackLocale: 'en',
  messages: {
    ja,
    en
  }
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)

app.mount('#app')
