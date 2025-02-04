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
                    @click="thenPage = 'doctors'"
                    class="name doctors" 
                    :class="{
                        'thenPage': thenPage === 'doctors'
                    }">Врачи</h2>
                    <h2 
                    @click="thenPage = 'osmotrs'" 
                    class="name osmotrs" 
                    :class="{
                        'thenPage': thenPage === 'osmotrs'
                    }">Осмотры</h2>
                </div>
                
            
                <div class="main__view">

                    <div  v-if="thenPage === 'profile'">
                        
                        <h3>Фамилия Имя Отчество</h3>
                        <div class="content_profile">
                            <h3>{{ $store.state.patient.surname }}
                                {{ $store.state.patient.name }}
                                {{ $store.state.patient.patronymic }}
                            </h3>
                        </div>
                        <h3>Номер телефона</h3>
                        <div class="content_profile">
                            <h3>{{ $store.state.patient.phone }}</h3>
                            <button @click="editphone=true">Изменить</button>
                            <input v-model="newphone" v-if="editphone" placeholder="Введите новый номер..."/>
                            <button @click="updatephone" v-if="editphone">подтвердить</button>
                        </div>
                        
                            <div class="content_profile1">
                                <h3 style="margin-right: 15px;">Пол: </h3>
                                <h3 style="background-color: #D9D9D9; padding: 5px 10px; border-radius: 5px;">{{ $store.state.patient.Gender }}</h3>
                            </div>
                        <h3>Домашний адрес</h3>
                        <div class="content_profile">
                            <h3>{{ $store.state.patient.home_address }}</h3>
                            <button @click="editAdress=true">Изменить</button>
                            <input  v-model="newAdress" v-if="editAdress" placeholder="Введите новый адрес..."/>
                            <button @click="updateAdress" v-if="editAdress">подтвердить</button>
                        </div>
                        <div class="exitBox">
                            <button @click="unAuthorizarion" class="exit">Выход</button>
                        </div>
                    </div>                       
                    <div class="AllDoctors" v-if="thenPage === 'doctors'">


                        <div class="menu">

                            <search-btn @click="startShow('search')" class="search_btn"/>
                                                        
                        </div>

                        <named-bar :names="['ФИО', 'Телефон', 'Участок', 'Стаж']"/>
                        <doctor-bar @SelectDoctor="SelectDoctor"  v-if="doctors.length >= 1" v-for="doctor in searchedClient(doctors).slice(page*limit-limit, page*limit)" 
                        :doctor="doctor"
                        :selected="{
                            true: info.view && info.object_view === 'doctor' && info.doctor.id === doctor.id
                        }"/>
                        <h3 class="empty" v-else>Врачей нет</h3>

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
                    <div class="AllOsmotrs" v-else-if="thenPage === 'osmotrs'">
                        

                        <div class="menu">

                            <add-btn @click="startShow('create')" class="add_btn"/>

                        </div>


                        <osmotr-bar 
                        v-if="osmotrs.length >= 1"
                        v-for="osmotr in osmotrs.slice(page*limit-limit, page*limit)" 
                        :osmotr="osmotr"
                        @SelectOsmotr="SelectOsmotr"
                        :selected="{
                            true: info.view && info.object_view === 'osmotr' && info.osmotr.id === osmotr.id
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

                    <my-dialog :show="show" v-if="show">
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
                    </my-dialog>

                    
                </div>
            </div>
            
            
        </form>
        <my-dialog :show="show" v-if="show">
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
                    </my-dialog>
        
    </div>

</template>


<script>
import data from '@/Mixins/Data';

    export default {
        mixins: [
            data
        ],
        data() {
            return {
                thenPage: "profile",
                editphone: false,
                editMail: false,
                editAdress: false,
                newphone: '',
                newMail: '',
                newAdress: '',
                limit: 10,
                page: 1,
                totalPages: 0,
                show: false,
                dialog: '',
                searchMass: [],
                searched: {
                    
                    surname: '',
                    name: '',
                    patronymic: ''
                    
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
                        this.totalPages = Math.ceil(this.osmotrs.length / this.limit)
                        break;

                }

                this.searched = {
                    surname: '',
                    name: '',
                    patronymic: ''
                }
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
                this.$store.commit('updatePatient', null)
            },
            updatephone() {
                if (this.newphone < 9){
                    alert("Номер слишком короткий")
                    return
                }

                if (confirm("Вы уверены что хотите поменять номер " + this.$store.state.patient.phone + " на новый " + this.newphone)) {
                    this.$store.state.patient.phone = this.newphone
                }

                this.newphone = ''
                this.editphone = false

            },
            updateMail() {
                if (this.newMail.split('@').length < 2){
                    alert("Не корректная почта")
                    return
                }

                if (confirm("Вы уверены что хотите поменять почту " + this.$store.state.patient.Mail + " на новую " + this.newMail)) {
                    this.$store.state.patient.Mail = this.newMail
                }

                this.newMail = ''
                this.editMail = false
            },
            updateAdress() {
                if (this.newAdress < 5){
                    alert("Адрес слишком короткий")
                    return
                }

                if (confirm("Вы уверены что хотите поменять Адрес " + this.$store.state.patient.home_address + " на новый " + this.newAdress)) {
                    this.$store.state.patient.home_address = this.newAdress
                }

                this.newAdress = ''
                this.editAdress = false
            },
            SelectDoctor(doctor) {
                if (doctor.id == this.info.doctor.id && this.info.view){
                    this.info.view =false
                    return
                }

                this.info.view = true
                this.info.object_view = 'doctor'
                this.info.doctor = doctor
                this.info.osmotrs = []
                this.osmotrs.forEach(osmotr => {
                    if (osmotr.doctor.id == doctor.id){
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
            }
        }
    }

</script>


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


.form {
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

.content_profile {
    display: flex;
    margin-top: 8px;
    margin-bottom: 15px;
}
.content_profile1 {
    display: flex;
}

.content_profile h3 {
    background-color: #D9D9D9;
    padding: 5px 10px;
    border-radius: 5px;
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