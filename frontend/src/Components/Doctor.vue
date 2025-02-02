<script>
 export default {
        data() {
            return {
                thenPage: "profile",
                editPlace: false,
                newPlace: '',
                limit: 10,
                page: 1,
                patients: [
                    {
                        id: 1,
                        Fio: "Haruton ebrog Afomon",
                        Phone: "8 888 099 73-89",
                        Gender: "М",
                        Age: 6
                    },
                    {
                        id: 2,
                        Fio: "Haruton ebrog Afomon",
                        Phone: "8 888 099 73-89",
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
                ]
                    
            }
        },
        methods:{
            unAuthorizarion() {
                this.$router.push('/')
                this.$store.commit('updateDoctor', null)
            },
            updatePlace(){
                if (this.newPlace.split('@').length > 2){
                    alert("Такого участка нет")
                    return
                }

                if (confirm("Вы уверены что хотите поменять почту " + this.$store.state.doctor.Place + " на новую " + this.newPlace)) {
                    this.$store.state.doctor.Place = this.newPlace
                }

                this.newPlace = ''
                this.editPlace = false
            }
        }
    }
</script>

<template>
<div class="main">
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
                        <h2 class="root">Должность: Пульмонолог</h2>
                    </div>

                    <h3>Номер телефона</h3>
                    <div class="content_profile">
                        <h3>{{ $store.state.doctor.Phone }}</h3>
                    </div>

                    <h3>Электронная почта</h3>
                    <div class="content_profile">
                        <h3>{{ $store.state.doctor.Mail }}</h3>
                    </div>

                    <div class="content_profile2">
                        <h3>Участок: {{ $store.state.doctor.Place }}</h3>
                        <button @click="editPlace=true">Изменить</button>
                        <input  v-model="newPlace" v-if="editPlace" placeholder="Введите новый участок..."/>
                        <button @click="updatePlace" v-if="editPlace">Подтвердить</button>
                    </div>

                    <div class="content_profile2">
                        <h3>Ваш стаж: {{ $store.state.doctor.Stage }}</h3>
                        <h3 v-if="$store.state.doctor.Stage === 1">год</h3>
                        <h3 v-else-if="$store.state.doctor.Stage < 5">года</h3>
                        <h3 v-else-if="$store.state.doctor.Stage > 4">лет</h3>
                    </div>

                    <div class="exitBox">
                        <button @click="unAuthorizarion" class="exit">Выход</button>
                    </div>
                </div>

                <div class="AllPatients" v-if="thenPage === 'patients'">
                    <named-bar :names="['ФИО', 'Телефон', 'Возраст', 'Пол']"/>
                    <patient-bar v-if="patients.length >= 1" v-for="patient in patients" 
                    :patient="patient"/>
                    <h3 class="empty" v-else>Пациентов нет</h3>
                </div>

                <div class="AllOsmotrs" v-if="thenPage === 'osmotrs'">
                        
                    <osmotr-bar 
                    v-if="osmotrs.length >= 1"
                    v-for="osmotr in osmotrs" 
                    :osmotr="osmotr"/>
                    <h3 class="empty" v-else>Осмотров нет</h3>

                </div>
            </div>
        </div>
    </form>
</div>
</template>

<style scoped>
input {
background-color: #F0EEEE;
}

textarea {
background-color: #F0EEEE;
}


.form {
display: flex;
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

.content_profile h3 {
    background-color: #D9D9D9;
    padding: 5px 10px;
    border-radius: 5px;
}

.content_profile2 h3 {
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

.content_profile2 button {
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
</style>