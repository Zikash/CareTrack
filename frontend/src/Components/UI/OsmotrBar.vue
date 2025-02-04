<template>
    <div class="osmotrBar">
        <div @click="$emit('SelectOsmotr', osmotr)" class="main" :class="{
            'select': selected.true
        }">
            <div class="main_content doctor">
                <h3 class="left">Врач</h3>
                <h3 class="Fio left">{{ osmotr.doctor.surname }} {{ osmotr.doctor.name }} {{ osmotr.doctor.patronymic }}</h3>
                <h3 @click.stop="copyphone(osmotr.doctor)" class="phone">{{ osmotr.doctor.phone }}</h3>
            </div>
            <div class="main_content patient">
                <h3 class="left">Пациент</h3>
                <h3 class="Fio left">{{ osmotr.patient.surname }} {{ osmotr.patient.name }} {{ osmotr.patient.patronymic }}</h3>
                <h3 @click.stop="copyphone(osmotr.patient)" class="phone">{{ osmotr.patient.phone }}</h3>
            </div>
            <div class="Main_Info">
                <div class="main_content">
                    <h3>Место осмотра</h3>
                    <h3 v-if="osmotr.serviced_area_number === 'Hospital'">Больница</h3>
                    <h3 v-else>{{ osmotr.patient.home_address }}</h3>
                </div>
                <div class="main_content">
                    <h3>Дата</h3>
                    <h3>{{ osmotr.Date_this }}</h3>
                    <h3>Время</h3>
                    <h3>{{ osmotr.Time_this }}</h3>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>

export default {
    name: 'osmotr-bar',
    props: {
        selected: {
                Type: Boolean,
                default: false
            },
        osmotr: {
            Type: Object,
            required: true
        }
    },
    methods: {
        copyphone(object) {
                navigator.clipboard.writeText(object.phone)
                alert("Скопирован номер " + object.phone)
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
        padding: 5px;
        border-radius: 5px;
        margin-bottom: 20px;

        h3 {
            margin: auto;
            padding: 5px 15px;
        }

        
    }

    .main_content {
        display: flex;
    }

    .select {
    background-color: #02b820;
    }

</style>







