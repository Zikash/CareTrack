import { createRouter, createWebHistory } from "vue-router";
import Main from "@/Page/Main.vue";
import Registration from "@/Page/Registration.vue";
import Authorization from "@/Page/Authorization.vue";
import Profile from "@/Page/Profile.vue";


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
    },
    {
        path: "/profile",
        component: Profile
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})


export default router;