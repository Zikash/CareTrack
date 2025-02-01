<template>
    <div class="osmotrBar">
        <div @click="hello" class="main">
            <div class="main_content doctor">
                <h3 class="left">Врач</h3>
                <h3 class="Fio left">{{ osmotr.doctor.Fio }}</h3>
                <h3 @click.stop="copyPhone(osmotr.doctor)" class="Phone">{{ osmotr.doctor.Phone }}</h3>
            </div>
            <div class="main_content patient">
                <h3 class="left">Пациент</h3>
                <h3 class="Fio left">{{ osmotr.patient.Fio }}</h3>
                <h3 @click.stop="copyPhone(osmotr.patient)" class="Phone">{{ osmotr.patient.Phone }}</h3>
            </div>
            <div class="Main_Info">
                <div class="main_content">
                    <h3>Место осмотра</h3>
                    <h3 v-if="osmotr.place === 'Hospital'">Больница</h3>
                    <h3 v-else>{{ osmotr.patient.Address }}</h3>
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
        osmotr: {
            Type: Object,
            required: true
        }
    },
    methods: {
        copyPhone(object) {
                navigator.clipboard.writeText(object.Phone)
                alert("Скопирован номер " + object.Phone)
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

</style>







