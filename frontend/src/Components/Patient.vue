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
                            <h3>{{ $store.state.patient.Fio }}</h3>
                        </div>
                        <h3>Номер телефона</h3>
                        <div class="content_profile">
                            <h3>{{ $store.state.patient.Phone }}</h3>
                            <button @click="editPhone=true">Изменить</button>
                            <input v-model="newPhone" v-if="editPhone" placeholder="Введите новый номер..."/>
                            <button @click="updatePhone" v-if="editPhone">подтвердить</button>
                        </div>
                        
                            <div class="content_profile1">
                                <h3 style="margin-right: 15px;">Пол: </h3>
                                <h3 style="background-color: #D9D9D9; padding: 5px 10px; border-radius: 5px;">{{ $store.state.patient.Gender }}</h3>
                            </div>
                        <h3>Электронная почта</h3>
                        <div class="content_profile">
                            <h3>{{ $store.state.patient.Mail }}</h3>
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
                        <doctor-bar  v-if="doctors.length >= 1" v-for="doctor in doctors" 
                        :doctor="doctor"/>
                        <h3 class="empty" v-else>Докторов нет</h3>

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
        methods: {
            unAuthorizarion() {
                this.$router.push('/')
                this.$store.commit('updatePatient', null)
            },
            updatePhone() {
                if (this.newPhone < 9){
                    alert("Номер слишком короткий")
                    return
                }

                if (confirm("Вы уверены что хотите поменять номер " + this.$store.state.patient.Phone + " на новый " + this.newPhone)) {
                    this.$store.state.patient.Phone = this.newPhone
                }

                this.newPhone = ''
                this.editPhone = false

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

</style>