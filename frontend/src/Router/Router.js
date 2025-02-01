import { createRouter, createWebHistory } from "vue-router";
import Main from "@/Page/Main.vue";
import Profile from "@/Page/Profile.vue";
import AuthPage from "@/Page/AuthPage.vue"


const routes = [
    {
        path: "/",
        component: Main 
    },
    {
        path: "/authorization",
        component: AuthPage
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