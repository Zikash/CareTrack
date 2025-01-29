import { createRouter, createWebHistory } from "vue-router";
import Main from "@/Components/Main.vue";
import Registration from "@/Components/Registration.vue";


const routes = [
    {
        path: "/",
        component: Main 
    },
    {
        path: "/registration",
        component: Registration
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})


export default router;