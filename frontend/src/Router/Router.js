import { createRouter, createWebHistory } from "vue-router";
import Main from "@/Components/Main.vue";


const routes = [
    {
        path: "/",
        component: Main 
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})


export default router;