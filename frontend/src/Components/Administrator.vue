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

                    <div class="AdminProfile" v-if="thenPage === 'profile'">
                        <div class="rootBox">
                            <h2 class="root">Должность: Администратор</h2>
                        </div>
                        
                        <h3>Номер телефона</h3>
                        <div class="content_profile">
                            <h3>{{ $store.state.administrator.Phone }}</h3>
                            <button @click="editPhone=true">Изменить</button>
                            <input v-model="newPhone" v-if="editPhone" placeholder="Введите новый номер..."/>
                            <button @click="updatePhone" v-if="editPhone">подтвердить</button>
                        </div>
                        <h3>Электронная почта</h3>
                        <div class="content_profile">
                            <h3>{{ $store.state.administrator.Mail }}</h3>
                            <button @click="editMail=true">Изменить</button>
                            <input  v-model="newMail" v-if="editMail" placeholder="Введите новую почту..."/>
                            <button @click="updateMail" v-if="editMail">подтвердить</button>
                        </div>
                        <div class="exitBox">
                            <button @click="unAuthorizarion" class="exit">Выход</button>
                        </div>
                    </div>                       
                    <div class="AllDoctors" v-if="thenPage === 'doctors'">

                        <named-bar :names="['ФИО', 'Телефон', 'Участок', 'Стаж']"/>
                        <doctor-bar @SelectDoctor="SelectDoctor"  v-if="doctors.length >= 1" v-for="doctor in doctors" 
                        :doctor="doctor"
                        :selected="{
                            true: info.view && info.object_view === 'doctor' && info.doctor.id === doctor.id
                        }"/>
                        <h3 class="empty" v-else>Докторов нет</h3>

                    </div>
                    <div class="AllPatients" v-else-if="thenPage === 'patients'">
                        
                        <named-bar :names="['ФИО', 'Телефон', 'Возраст', 'Пол']"/>
                        <patient-bar @SelectPatient="SelectPatient" v-if="patients.length >= 1" v-for="patient in patients" 
                        :patient="patient"
                        :selected="{
                            true: info.view && info.object_view === 'patient' && info.patient.id === patient.id
                        }"/>
                        <h3 class="empty" v-else>Пациентов нет</h3>

                    </div>
                    <div class="AllOsmotrs" v-else-if="thenPage === 'osmotrs'">
                        
                        <osmotr-bar 
                        v-if="osmotrs.length >= 1"
                        v-for="osmotr in osmotrs" 
                        :osmotr="osmotr"
                        @SelectOsmotr="SelectOsmotr"
                        :selected="{
                            true: info.view && info.object_view === 'osmotr' && info.osmotr.id === osmotr.id
                        }"/>
                        <h3 class="empty" v-else>Осмотров нет</h3>

                    </div>
                    
                </div>
            </div>
            
            
        </form>

        <form class="info" @submit.prevent v-if="info.view">
            
            <div class="closeBox">
                <Button @="closeView" class="close">X</Button>
            </div>

            <patient-info :info="info" v-if="info.object_view === 'patient'"/>
            <doctor-info :info="info" v-if="info.object_view === 'doctor'"/>
            <osmotr-info :info="info" v-if="info.object_view === 'osmotr'"/>

        </form>
    </div>

</template>


<script>

    export default {
        data() {
            return {
                thenPage: "profile",
                editPhone: false,
                editMail: false,
                newPhone: '',
                newMail: '',
                limit: 10,
                page: 1,
                doctors: [
                    {
                        id: 1,
                        Fio: "Nikolay Pobelov Homonaft",
                        Phone: "8 999 999 99-99",
                        Place: 1,
                        Stage: 1
                    },
                    {
                        id: 2,
                        Fio: "Nikolay Pobelov Homonaft",
                        Phone: "8 999 988 99-99",
                        Place: 2,
                        Stage: 4
                    }
                ],
                patients: [
                    {
                        id: 1,
                        Fio: "Haruton ebrog Afomon",
                        Phone: "8 888 099 73-89",
                        Address: "UUlice 88",
                        Gender: "М",
                        Age: 6
                    },
                    {
                        id: 2,
                        Fio: "Haruton ebrog Afomon",
                        Phone: "8 888 099 73-89",
                        Address: "hoolersire h. 57",
                        Gender: "М",
                        Age: 38
                    }

                ],
                osmotrs: [
                    {
                        id: 1,
                        doctor: {
                            id: 1,
                            Fio: "Nikolay Pobelov Homonaft",
                            Phone: "8 999 999 99-99",
                            Place: 1,
                            Stage: 1
                        },
                        patient: {
                            id: 1,
                            Fio: "Haruton ebrog Afomon",
                            Phone: "8 888 099 73-89",
                            Address: "moletare 17"
                        },
                        place: "Hospital",
                        Date_this: "11.11.11",
                        Time_this: "11:11"
                    },
                    {
                        id: 2,
                        doctor: {
                            id: 2,
                            Fio: "Nikolay Pobelov Homonaft",
                            Phone: "8 999 988 99-99",
                            Place: 2,
                            Stage: 4
                        },
                        patient: {
                            id: 2,
                            Fio: "Haruton ebrog Afomon",
                            Phone: "8 888 099 73-89",
                            Address: "hoolersire h. 57"
                        },
                        place: "Home",
                        Date_this: "11.11.11",
                        Time_this: "11:66"
                    }
                ],
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
        methods: {
            unAuthorizarion() {
                this.$router.push('/')
                this.$store.commit('updateAdministrator', null)
            },
            updatePhone() {
                if (this.newPhone < 9){
                    alert("Номер слишком короткий")
                    return
                }

                if (confirm("Вы уверены что хотите поменять номер " + this.$store.state.administrator.Phone + " на новый " + this.newPhone)) {
                    this.$store.state.administrator.Phone = this.newPhone
                }

                this.newPhone = ''
                this.editPhone = false

            },
            updateMail() {
                if (this.newMail.split('@').length < 2){
                    alert("Не корректная почта")
                    return
                }

                if (confirm("Вы уверены что хотите поменять почту " + this.$store.state.administrator.Mail + " на новую " + this.newMail)) {
                    this.$store.state.administrator.Mail = this.newMail
                }

                this.newMail = ''
                this.editMail = false
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
            closeView() {
                this.info.view = false
            }
        }
    }

</script>


<style scoped>


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

</style>