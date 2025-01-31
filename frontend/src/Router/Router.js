import { createRouter, createWebHistory } from "vue-router";
import Main from "@/Page/Main.vue";
import Registration from "@/Components/Registration.vue";
import Authorization from "@/Components/Authorization.vue";


const routes = [
    {
        path: "/",
        component: Main 
    },
    {
        path: "/registration",
        component: Registration
    },
    {
        path: "/authorization",
        component: Authorization
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})


export default router;