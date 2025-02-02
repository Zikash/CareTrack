<template>
    <div class="doctorBar">
        <div @click="$emit('SelectDoctor', doctor)" class="main" :class="{
            'select': selected.true
        }">
            <h3 class="Fio left">{{ doctor.Fio }}</h3>
            <h3 @click.stop="copyPhone" class="Phone left">{{ doctor.Phone }}</h3>
            <h3 class="Place left">{{ doctor.Place }}</h3>
            <h3 class="Stage">{{ doctor.Stage }}</h3>
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
            copyPhone() {
                navigator.clipboard.writeText(this.doctor.Phone)
                alert("Скопирован номер " + this.doctor.Phone)
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