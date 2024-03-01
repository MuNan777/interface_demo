import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index'
import { createPinia } from 'pinia'
import axiosConfig from './config/axios'

const pinia = createPinia()

const app = createApp(App)
app.use(router)
app.use(pinia)
app.use({
  install: () => {
    // axios 配置
    axiosConfig()
  }
})
app.mount('#app')
