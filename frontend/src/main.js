import './assets/main.scss'

import { createApp } from 'vue'
import { createStore } from 'vuex'

import App from './App.vue'
import router from './router'
import vuetify from './vuetify'

const store = createStore({
    state () {
      return {
        count: 0
      }
    },
    mutations: {
      increment (state) {
        state.count++
      }
    }
  })

const app = createApp(App)

app.use(router)
app.use(store)
app.use(vuetify)
app.mount('#app')
