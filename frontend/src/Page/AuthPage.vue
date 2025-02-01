<template>
    
    <my-header/>

    <div v-if="$store.getters.isAuth">
        <h2 class="error">Вы уже авторизованы</h2>
    </div>
    <div v-else>
        <Authorization v-if="$store.state.auth === 'auth'"/>
        <Registration v-else/>
    </div>
    
    

</template>


<script>
import Authorization from '@/Components/Authorization.vue';
import Registration from '@/Components/Registration.vue';


export default {
    components: {
        Authorization,
        Registration
    }
}

</script>


<style scoped>

    .error {
        color: red;
        text-align: center;
        align-content: center;
    }

</style>