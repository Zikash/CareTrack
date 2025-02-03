<template>
    <div class="patientBar">
        <div @click="$emit('SelectPatient', patient)" class="main" :class="{
            'select': selected.true
        }">
            <h3 class="Fio left">{{ patient.Fio }}</h3>
            <h3 @click.stop="copyphone" class="phone left">{{ patient.phone }}</h3>
            <h3 class="serviced_area_number left">{{ patient.Age }}</h3>
            <h3 class="experience">{{ patient.Gender }}</h3>
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
            copyphone() {
                navigator.clipboard.writeText(this.patient.phone)
                alert("Скопирован номер " + this.patient.phone)
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