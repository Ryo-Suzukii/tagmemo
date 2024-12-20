import { createApp } from 'vue'
import './style.css'
import { createI18n } from 'vue-i18n'
import App from './App.vue'
import router from './router'
import ja from './locales/ja.json'
import en from './locales/en.json'

import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { createPinia } from 'pinia'

library.add(fas)

const i18n = createI18n({
  locale: "ja",
  messages: {
    ja,
    en
  }
})

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.use(i18n)
app.use(vuetify)
app.use(createPinia())
app.mount('#app')
