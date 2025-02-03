<template>
    <div class="doctorBar">
        <div @click="$emit('SelectDoctor', doctor)" class="main" :class="{
            'select': selected.true
        }">
            <h3 class="Fio left">{{ doctor.Fio }}</h3>
            <h3 @click.stop="copyphone" class="phone left">{{ doctor.phone }}</h3>
            <h3 class="serviced_area_number left">{{ doctor.serviced_area_number }}</h3>
            <h3 class="experience">{{ doctor.experience }}</h3>
        </div>
    </div>
</template>


<script>

    export default {
        name: 'doctor-bar',
        props: {
            selected: {
                Type: Boolean,
                default: false
            },
            doctor: {
                Type: Object,
                required: true
            }
        },
        methods: {
            copyphone() {
                navigator.clipboard.writeText(this.doctor.phone)
                alert("Скопирован номер " + this.doctor.phone)
            }
        }
    }

</script>


<style scoped>

    .doctorBar {
        padding-bottom: 10px;
    }

    .main {
        background-color: #D9D9D9;
        display: flex;
        padding: 5px;
        border-radius: 5px;

        h3 {
            margin: auto;
            padding: 5px 15px;
        }

        
    }


    .select {
    background-color: #02b820;
    }

</style>