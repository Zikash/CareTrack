<script>
import data from "@/Mixins/Data";


    export default {
        mixins: [
            data
        ],
        data() {
            return {
                thenPage: "profile",
                editServiced_area_number: false,
                newServiced_area_number: '',
                limit: 10,
                page: 1,
                totalPages: 0,
                show: false,
                dialog: '',
                searchMass: [],
                osmotrs_doctor: [],
                This_doctor: [],
                searched: {
                    
                    surname: '',
                    name: '',
                    patronymic: ''
                    
                },
                info: {
                    view: false,
                    object_view: 'patient',
                    patient: {},
                    doctor: {},
                    osmotr: {},
                    osmotrs: []
                }
                                    
            }
        },
        watch: {
            thenPage() {
                this.page = 1
                switch (this.thenPage){
                    case "profile":
                        return
                        break;
                    case "doctors":
                        this.totalPages = Math.ceil(this.doctors.length / this.limit)
                        break;
                    case "patients":
                        this.totalPages = Math.ceil(this.patients.length / this.limit)
                        break;
                    case "osmotrs":
                        this.totalPages = Math.ceil(this.osmotrs_doctor.length / this.limit)
                        break;

                }

                this.searched = {
                    surname: '',
                    name: '',
                    patronymic: ''
                }
            },
            osmotrs_doctors(){
                this.osmotrs_doctor.forEach(osmotr => {
                    if (!this.osmotrs.includes(osmotr)){
                        this.osmotrs.push(osmotr)
                    }
                })
            }
        },
        methods: {
            createOsmotr(osmotr){

                this.osmotrs.push(osmotr)
            },
            searchedClient(mass){
                this.searchMass = mass.filter(elem => elem.surname.toLowerCase().includes(this.searched.surname.toLocaleLowerCase())
                                && elem.name.toLowerCase().includes(this.searched.name.toLocaleLowerCase())
                                && elem.patronymic.toLowerCase().includes(this.searched.patronymic.toLocaleLowerCase()))
                this.totalPages = Math.ceil(this.searchMass.length / this.limit)
                return this.searchMass
                
            },
            unAuthorizarion() {
                this.$router.push('/')
                this.$store.commit('updateDoctor', null)
            },
            updateServiced_area_number() {
                if (this.newServiced_area_number.split('@').length > 2){
                    alert("Такого участка не существует")
                    return
                }

                if (confirm("Вы уверены что хотите поменять участок " + this.$store.state.doctor.Serviced_area_number + " на новый " + this.newServiced_area_number)) {
                    this.$store.state.doctor.Serviced_area_number = this.newServiced_area_number
                }

                this.newServiced_area_number = ''
                this.editServiced_area_number = false
            },
            SelectPatient(patient) {
                if (patient.id == this.info.patient.id && this.info.view){
                    this.info.view =false
                    return
                }

                this.info.view = true
                this.info.object_view = 'patient'
                this.info.patient = patient
                this.info.osmotrs = []
                this.osmotrs.forEach(osmotr => {
                    if (osmotr.patient.id == patient.id){
                        this.info.osmotrs.push(osmotr)
                    }
                })
                
            },
            SelectOsmotr(osmotr) {
                if (osmotr.id == this.info.osmotr.id && this.info.view){
                    this.info.view =false
                    return
                }

                this.info.view = true
                this.info.object_view = 'osmotr'
                this.info.osmotr = osmotr
                
                this.doctors.forEach(doctor => {
                    if (doctor.id == osmotr.doctor.id){
                        this.info.doctor = doctor
                        return
                    }
                })

                this.patients.forEach(patient => {
                    if (patient.id == osmotr.patient.id) {
                        this.info.patient = patient
                        return
                    }
                })

                this.info.osmotrs = []
                
                
            },

            startShow(dialog){
                this.show = true
                this.dialog = dialog
            },
        },
        mounted() {
            this.osmotrs.forEach(osmotr => {
                if(this.$store.state.doctor.id == osmotr.doctor.id){
                    this.osmotrs_doctor.push(osmotr)
                }
            })
            this.This_doctor.push(this.$store.state.doctor)
        }
    }

</script>

<template>
<div class="main_div">
    <form class="form" @submit.prevent>
        <div class="main">
            <div class="headbar">
                    <h2 
                    @click="thenPage = 'profile'" 
                    class="name profile" 
                    :class="{
                        'thenPage': thenPage === 'profile'
                    }">Профиль</h2>
                    <h2 
                    @click="thenPage = 'patients'" 
                    class="name patients" 
                    :class="{
                        'thenPage': thenPage === 'patients'
                    }">Пациенты</h2>
                    <h2 
                    @click="thenPage = 'osmotrs'" 
                    class="name osmotrs" 
                    :class="{
                        'thenPage': thenPage === 'osmotrs'
                    }">Осмотры</h2>
                </div>

            <div class="main__view">
                <div class="DoctorProfile" v-if="thenPage === 'profile'">
                    <div class="rootBox">
                        <h2 class="root">Должность: {{ $store.state.doctor.job_title }}</h2>
                    </div>

                    <h3>Имя Фамилия Отчество</h3>
                    <div class="content_profile">
                        <h3>{{ $store.state.doctor.name }} {{ $store.state.doctor.surname }} {{ $store.state.doctor.patronymic }}</h3>
                    </div>

                    <h3>Номер телефона</h3>
                    <div class="content_profile">
                        <h3>{{ $store.state.doctor.phone }}</h3>
                    </div>
                    
                    <div class="content_profile">
                        <h3>Участок: {{ $store.state.doctor.Serviced_area_number }}</h3>
                        <button @click="editServiced_area_number=true">Изменить</button>
                        <input  v-model="newServiced_area_number" v-if="editServiced_area_number" placeholder="Введите новый участок..."/>
                        <button @click="updateServiced_area_number" v-if="editServiced_area_number">Подтвердить</button>
                    </div>

                    <div class="content_profile">
                        <h3>Ваш стаж: {{ $store.state.doctor.Experience }}</h3>
                        <h3 v-if="$store.state.doctor.Stage === 1">год</h3>
                        <h3 v-else-if="$store.state.doctor.Stage < 5">года</h3>
                        <h3 v-else-if="$store.state.doctor.Stage > 4">лет</h3>
                    </div>

                    <div class="exitBox">
                        <button @click="unAuthorizarion" class="exit">Выход</button>
                    </div>
                </div>

                <div class="AllPatients" v-if="thenPage === 'patients'">
                    <div class="menu">
                        <search-btn @click="startShow('search')" class="search_btn"/>  
                    </div>
                    <named-bar :names="['ФИО', 'Телефон', 'Возраст', 'Пол']"/>
                    <patient-bar @SelectPatient="SelectPatient" v-if="patients.length >= 1" v-for="patient in searchedClient(patients).slice(page*limit-limit, page*limit)" 
                        :patient="patient"
                        :selected="{
                            true: info.view && info.object_view === 'patient' && info.patient.id === patient.id
                    }"/>
                    <h3 class="empty" v-else>Пациентов нет</h3>
                    <div class="page_wrapper">
                            <h3 v-for="Npage in totalPages"
                            class="page_number"
                            :key="Npage"
                            :class="{
                                'this_page': page === Npage
                            }"
                            @click="page = Npage">{{ Npage }}</h3>
                    </div>
                </div>

                <div class="AllOsmotrs" v-if="thenPage === 'osmotrs'">
                    <div class="menu">
                        <add-btn @click="startShow('create')" class="add_btn"/>
                    </div>
                    <osmotr-bar 
                        v-if="osmotrs_doctor.length >= 1"
                        v-for="osmotr_doctor in osmotrs_doctor.slice(page*limit-limit, page*limit)" 
                        :osmotr="osmotr_doctor"
                        @SelectOsmotr="SelectOsmotr"
                        :selected="{
                            true: info.view && info.object_view === 'osmotr' && info.osmotr.id === osmotr_doctor.id
                    }"/>
                    <h3 class="empty" v-else>Осмотров нет</h3>
                    <div class="page_wrapper">
                        <h3 v-for="Npage in totalPages"
                        class="page_number"
                        :key="Npage"
                        :class="{
                            'this_page': page === Npage
                        }"
                        @click="page = Npage">{{ Npage }}</h3>
                    </div>
                </div>

                <my-dialog v-model:show="show" v-if="show">
                    <ul v-if="dialog === 'search'">
                        <li class="content__element">
                            <h3>Фамилия</h3>
                            <input v-model="searched.surname" class="surname_input input" type="text">
                        </li>
                        <li class="content__element">
                            <h3>Имя</h3>
                            <input v-model="searched.name" class="name_input input" type="text">
                        </li>
                        <li class="content__element">
                            <h3>Отчество</h3>
                            <input v-model="searched.patronymic" class="patronymic_input input" type="text">
                        </li>
                    </ul>
                    <create-osmotr
                        v-model:osmotrs="osmotrs_doctor"
                        :doctors="This_doctor"
                        :patients="patients"
                        v-model:view="show"
                        v-else-if="dialog === 'create'"/>
                </my-dialog>
            </div>
        </div>
    </form>

    <form class="info" @submit.prevent v-if="info.view">
        <div class="closeBox">
            <Button @click="info.view = false" class="close">X</Button>
        </div>
        <patient-info :info="info" v-if="info.object_view === 'patient'"/>
        <doctor-info :info="info" v-if="info.object_view === 'doctor'"/>
        <osmotr-info :info="info" v-if="info.object_view === 'osmotr'"/>
    </form>
</div>
</template>

<style scoped>


li {
    list-style-type: none;
}

input {
background-color: #F0EEEE;
}

textarea {
background-color: #F0EEEE;
}


form {
/*display: flex;*/
margin: auto;
}

.main_div {
display:flex;
flex-wrap: wrap;
margin-top: 20px;
margin-left: auto;
margin-right: auto;
min-width: 500px;
}

.main {
margin-top: 20px;
margin-left: auto;
margin-right: auto;
min-width: 500px;
}

.headbar {
display: flex;

}


.name {
background-color: white;
border-radius: 10px 10px 0 0;
align-content: center;
text-align: center;
width: 100%;
padding: 15px;
height: 50px;
}

.profile {
    box-shadow: -3px -3px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.doctors {
    box-shadow: 0px -2px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.patients {
    box-shadow: 0px -2px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.osmotrs {
    box-shadow: 3px -3px 4px 3px rgba(34, 60, 80, 0.2) inset;
}

.thenPage {
    box-shadow: 0px 0px 0px 0px rgba(34, 60, 80, 0.2) inset;
}



.main__view {
background-color: white;
padding: 35px;
margin-left: auto;
margin-right: auto;
border-radius: 0px 0px 10px 10px;
}

.rootBox {
    padding-left: 40px;
    padding-right: 40px;
    margin-bottom: 40px;
}

.root {
    margin-left: auto;
    margin-right: auto;
    text-align: center;
    align-content: center;
    background-color: #D9D9D9;
    height: 40px;
    border-radius: 5px;
}

.content_profile {
    display: flex;
    margin-top: 8px;
    margin-bottom: 15px;
}

.content_profile2 {
    display: flex;
    margin-top: 8px;
    margin-bottom: 15px;
}

.content_profile2 h3 {
    padding: 5px 10px;
    border-radius: 5px;
}

.content_profile h3 {
    background-color: #D9D9D9;
    padding: 5px 10px;
    border-radius: 5px;
}

.content_profile2 button {
    background-color: #69C553;
    border-radius: 5px;
    padding: 5px;
    margin-left: 20px;
    font-size: 15px;
}

.content_profile input {
    margin-left: 30px;
    background-color: #D9D9D9;
    padding: 5px;
    border-radius: 5px;
}


.content_profile button {
    background-color: #69C553;
    border-radius: 5px;
    padding: 5px;
    margin-left: 20px;
    font-size: 15px;
}

.empty {
    text-align: center;
    align-content: center;
    margin-top: 40px;
    font-size: 30px;
}

.exitBox {
    display: flex;
}

.exit {
    background-color: #B83E40;
    border-radius: 5px;
    padding: 8px;
    margin-top: 10px;
    margin-left: auto;
    margin-right: 20px;
}


.closeBox {
    padding-top: 40px;
    display: flex;
}

.close {
    height: 50px;
    width: 50px;
    font-size: 30px;
    margin-left: auto;
    margin-right: auto;
    background-color: red;
    border-radius: 100%;
}

.page_wrapper {
    margin-left:auto;
    display: flex;
    padding: 5px;
}

.page_number {
    margin-left: 10px;
    border: 2px black;
    padding: 10px;
    box-sizing: border-box;
    background-color: #69C553;
}

.this_page {
    background-color: green;
}

.menu {
    margin-bottom: 30px;
    display: flex;
}

.menu .search_btn{
    margin-left: 10px;
    margin-right: auto;
}

.menu .add_btn {
    margin-left: auto;
}


</style>