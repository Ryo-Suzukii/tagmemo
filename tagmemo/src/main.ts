import { createApp } from 'vue'
import './style.css'
import { createI18n } from 'vue-i18n'
import App from './App.vue'
import router from './router'
import ja from './locales/ja.json'
import en from './locales/en.json'

const i18n = createI18n({
  locale: "ja",
  messages: {
    ja,
    en
  }
})

const app = createApp(App)
app.use(i18n)
app.use(router)
app.mount('#app')
