<template>
    <div class="patientBar">
        <div @click="$emit('SelectPatient', patient)" class="main" :class="{
            'select': selected.true
        }">
            <h3 class="Fio left">{{ patient.Fio }}</h3>
            <h3 @click.stop="copyPhone" class="Phone left">{{ patient.Phone }}</h3>
            <h3 class="Place left">{{ patient.Age }}</h3>
            <h3 class="Stage">{{ patient.Gender }}</h3>
        </div>
    </div>
</template>


<script>

    export default {
        name: 'patient-bar',
        props: {
            selected: {
                Type: Boolean,
                default: false
            },
            patient: {
                Type: Object,
                required: true
            }
        },
        methods: {
            copyPhone() {
                navigator.clipboard.writeText(this.patient.Phone)
                alert("Скопирован номер " + this.patient.Phone)
            }
        }
    }

</script>


<style scoped>

    .patientBar {
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