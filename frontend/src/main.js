import { createApp } from 'vue'
import App from '@/App.vue'
import router from "@/Router/Router"
import components from "@/Components/UI"
import store from "@/store/store"


const app = createApp(App)


components.forEach(component => {
    app.component(component.name, component)
});


app
    .use(router)
    .use(store)
    .mount('#app')
