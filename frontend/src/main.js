import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import '@/assets/global.css'


createApp(App).use(router).mount('#app')
