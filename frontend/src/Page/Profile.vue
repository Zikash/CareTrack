<template>

    <div>
        <my-header/>

        <div v-if="$store.state.patient != null" class="Patient">
            <Patient/>
        </div>
        <div v-else-if="$store.state.doctor != null" class="Doctor">
            <Doctor/>
        </div>
        <div v-else-if="$store.state.administrator != null" class="Administrator">
            <Administrator/>
        </div>
        
        <div v-else class="noAuth">
            <h1 class="error">Ошибка вы не зарегистрированы!</h1>
        </div>


    </div>

</template>


<script>
import Doctor from '@/Components/Doctor.vue';
import Patient from '@/Components/Patient.vue';
import Administrator from '@/Components/Administrator.vue';


    export default {
        components: {
            Doctor,
            Patient,
            Administrator,        
        }
    }


</script>


<style scoped>
    .error {
        margin-top: 10vh;
        margin-left: auto;
        margin-right: auto;
        align-content: center;
        text-align: center;
        font-size: 120;
        color: red;
    }
</style>