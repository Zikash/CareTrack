<template>

    <ul class="content">
        <li class="content_element">
            <h3>
                Место осмотра
            </h3>
            <select :value="osmotr.place" @change="osmotr.place = $event.currentTarget.value">
                <option :key="Hospital" :value="Hospital">Больница</option>
                <option  :key="Home" :value="Home">На дому</option>
            </select>
        </li>
        <li class="content_element">
            <h3>
                Дата осмотра
            </h3>
            <input :value="osmotr.Date_this" @input="osmotr.Date_this = $event.target.value" type="date">

        </li>
        <li class="content_element">
            <h3>
                Врач
            </h3>
            <select-user v-model:value="osmotr.doctor.id" @change="osmotr.doctor.id = Number($event.currentTarget.value)" :users="doctors"/>

        </li>
        <li class="content_element">
            <h3>
                Пациент
            </h3>
            <select-user v-model:value="osmotr.patient.id" @change="osmotr.patient.id = Number($event.currentTarget.value)" :users="patients"/>

        </li>
        <li class="content_element">
            <h3>
                Симптомы
            </h3>
            <textarea :value="osmotr.Simptomes" @change="osmotr.Simptomes = $event.currentTarget.value"></textarea>

        </li>
        <li class="content_element">
            <h3>
                Диагноз
            </h3>
            <input :value="osmotr.Result" @change="osmotr.Result = $event.currentTarget.value" type="text"/>

        </li>
        <li class="content_element">
            <h3>
                Предписания
            </h3>
            <textarea :value="osmotr.Predpis" @change="osmotr.Predpis = $event.currentTarget.value"></textarea>

        </li>

        <div class="commit_box">
            <button class="commit" @click="createOsmotr">
                Создать
            </button>
        </div>
    </ul>
</template>


<script>
import Data from '@/Mixins/Data';


    export default {
        name: 'create-osmotr',
        props: {
            view: {
                Type: Boolean,
                required: true
            },
            patients: {
                Type: Array,
                required: true
            },
            osmotrs: {
                Type: Array,
                required: true
            },
            doctors: {
                Type: Array,
                required: true
            }
        },
        data() {
            return {
                osmotr: {
                    id: 0,
                    place: 'Hospital',
                    patient: {
                        id: 1
                    },
                    doctor: {
                        id: 1
                    },
                    Time_this: '11:11'
                }
            }
        },
        methods: {
            createOsmotr() {
                this.doctors.forEach(doctor => {
                    if(doctor.id == Number(this.osmotr.doctor.id)){
                        this.osmotr.doctor = doctor
                    }
                })

                this.patients.forEach(patient => {
                    if(patient.id == Number(this.osmotr.patient.id)){
                        this.osmotr.patient = patient
                    }
                })
                this.osmotr.id = this.osmotrs.length + 1
                this.osmotrs.push(this.osmotr)
        
                this.$emit('update:osmotrs', this.osmotrs)
                this.$emit('update:view', false)
            }
        }
    }

</script>


<style scoped>
    li {
        list-style: none;
    }

    .content_element {
        margin-bottom: 10px;
    }

    * {
        font-size: 20px;
    }

    .commit_box {
        margin-top: 40px;
        display: flex;
    }

    .commit {
        height: 40px;
        width: 100px;
        margin: auto;
        background-color: green;
        border-radius: 5px;
    }
</style>