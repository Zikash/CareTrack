<template>

    <ul>
        <h3>
            Место осмотра
        </h3>
        <select @change="osmotr.place = $event.currentTarget.value">
            <option :value="Hospital">Больница</option>
            <option :value="Home">На дому</option>
        </select>
        <h3>
            Дата осмотра
        </h3>
        <input @input="osmotr.date = $event.target.value" type="date">
        <h3>
            Врач
        </h3>
        <select-user @change="osmotr.doctor = $event.currentTarget.value" :users="doctors"/>
        <h3>
            Пациент
        </h3>
        <select-user @change="osmotr.patient = $event.currentTarget.value" :users="patients"/>
        <h3>
            Симптомы
        </h3>
        <textarea @change="osmotr.simptomes = $event.currentTarget.value"></textarea>
        <h3>
            Диагноз
        </h3>
        <input @change="osmotr.result = $event.currentTarget.value" type="text"/>
        <h3>
            Предписания
        </h3>
        <textarea @change="osmotr.predpis = $event.currentTarget.value"></textarea>

        <div>
            <button @click="createOsmotr">
                Создать
            </button>
        </div>
    </ul>
</template>


<script>
import Data from '@/Mixins/Data';


    export default {
        name: 'create-osmotr',
        mixins: [
            Data
    ],
        data() {
            return {
                osmotr: {
                    id: 0,
                    serviced_area_number: "",
                    Date_This: 11.11,
                    patient: {

                    },
                    doctor: {

                    }
                }
            }
        },
        methods: {
            createOsmotr() {
                this.doctors.forEach(doctor => {
                    if(doctor.id == this.osmotr.doctor.id){
                        this.osmotr.doctor = doctor
                    }
                })
            }
        }
    }

</script>


<style scoped>

</style>