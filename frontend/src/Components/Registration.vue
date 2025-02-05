<template>

            
            <form class="form" @submit.prevent>
                
                <div class="main">
                    <div class="headbar">
                        <h2 class="name reg">Регистрация</h2>
                        <h2 @click="$store.commit('updateAuth', 'auth')" class="name auth">Авторизация</h2>
                    </div>
                    
                
                    <div class="main__view">

                        <select @change="reg_type = $event.target.value">
                            <option :value="Rpatient">Пациент</option>
                            <option :value="Rdoctor">Врач</option>
                        </select>

                        <h3 class="info_">{{ info }}</h3>

                        <div class="main__content">
                            <div class="main__content" v-if="reg_type === 'Пациент'">
                                <ul class="content__left">
                                    <li class="content__element">
                                        <h3>Фамилия</h3>
                                        <input v-model="patient.surname" class="surname_input input" type="text">

                                    </li>
                                    <li class="content__element">
                                        <h3>Имя</h3>
                                        <input v-model="patient.name" class="name_input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Отчество</h3>
                                        <input v-model="patient.patronymic" class="patronymic_input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Пол</h3>
                                        <input v-model="patient.gender" class="radio__gender" name="gender" type="radio" value="Male"><strong>М</strong>
                                        <input v-model="patient.gender" class="radio__gender" name="gender" type="radio" value="Female"><Strong>Ж</Strong>
                                    </li>
                                    <li class="content__element">
                                        <h3>Возраст</h3>
                                        <input v-model="patient.age" class="age__input" min="0" type="number">
                                    </li>

                                </ul>
                                <ul class="content__right">
                                    <li class="content__element">
                                        <h3>Телефон</h3>
                                        <input v-model="patient.number_phone" class="number__input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Адрес</h3>
                                        <textarea v-model="patient.home_address" class="home_address__input" type="text"></textarea>
                                    </li>
                                    <li class="content__element">
                                        <h3>Логин</h3>
                                        <input v-model.trim="login" class="password__input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Пароль</h3>
                                        <input v-model.trim="password" class="password__input input" type="password">
                                    </li>
                                    <li class="content__element">
                                        <h3>Подтверждение пароля</h3>
                                        <input v-model.trim="double_Password" class="double__password input" type="password">
                                    </li>
                                </ul>
                            </div>
                            <div class="main__content" v-else>
                                <ul class="content__left">
                                    <li class="content__element">
                                        <h3>Фамилия</h3>
                                        <input v-model="doctor.surname" class="surname_input input" type="text">

                                    </li>
                                    <li class="content__element">
                                        <h3>Имя</h3>
                                        <input v-model="doctor.name" class="name_input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Отчество</h3>
                                        <input v-model="doctor.patronymic" class="patronymic_input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Стаж</h3>
                                        <input v-model="doctor.experience" class="age__input" min="0" type="number">
                                    </li>

                                </ul>
                                <ul class="content__right">
                                    <li class="content__element">
                                        <h3>Телефон</h3>
                                        <input v-model="doctor.number_phone" class="number__input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Логин</h3>
                                        <input v-model.trim="login" class="password__input input" type="text">
                                    </li>
                                    <li class="content__element">
                                        <h3>Пароль</h3>
                                        <input v-model.trim="password" class="password__input input" type="password">
                                    </li>
                                    <li class="content__element">
                                        <h3>Подтверждение пароля</h3>
                                        <input v-model.trim="double_Password" class="double__password input" type="password">
                                    </li>
                                </ul>
                            </div>

                        </div>

                        <div class="wrapper">
                            <button @click="AddUser($router, $store)" class="btn">Зарегистрироваться</button>
                        </div>

                        
                    </div>
                </div>
                
                
            </form>

</template>



<script>
import Data from '@/Mixins/Data';
import { initCustomFormatter } from 'vue';


    export default {

        data() {
            return {
                patient: {
                    surname: "",
                    name: "",
                    patronymic: "",
                    gender: "",
                    age: 1,
                    number_phone: "",
                    home_address: ""
                },
                doctor: {
                    surname: "",
                    name: "",
                    patronymic: "",
                    number_phone: "",
                    experience: 0,
                    serviced_area_number: 0

                },
                reg_type: "Пациент",
                login: "",
                password: "",
                double_Password: "",
                info: ""
            }
        },
        methods: {
            AddUser(router, store) {

                if (this.reg_type == 'Пациент') {
                    this.info = ""

                    if (this.patient.surname.length <= 1){
                        this.info = "Фамилия короткая"
                    }else if (this.patient.name.length <= 1){
                        this.info = "Имя короткое"
                    }else if (this.patient.patronymic.length <= 1){
                        this.info = "Отчество короткое"
                    }else if (this.patient.gender === ""){
                        this.info = "Не выбран пол"
                    }else if (this.patient.number_phone.length < 10){
                        this.info = "Некорректный номер телефона"
                    }else if (this.patient.home_address === ""){
                        this.info = "Не введён адрес"
                    }else if (this.password.length < 8){
                        this.info = "Пароль короткий минимум 8 символов"
                    }else if (this.password != this.double_Password){
                        this.info = "Пароли должны совпадать"
                    }


                    
                    if (this.info === ""){
                        //Сюда свойство регистрации

                        store.commit("updatePatient", this.patient)

                        alert("Аккаунт успешно зарегистрирован")
                        router.push("/")
                    }
                }
                else {
                    this.info = ""

                    if (this.doctor.surname.length <= 1){
                        this.info = "Фамилия короткая"
                    }else if (this.doctor.name.length <= 1){
                        this.info = "Имя короткое"
                    }else if (this.doctor.patronymic.length <= 1){
                        this.info = "Отчество короткое"
                    }else if (this.doctor.number_phone.length < 10){
                        this.info = "Некорректный номер телефона"
                    }else if (this.password.length < 8){
                        this.info = "Пароль короткий минимум 8 символов"
                    }else if (this.password != this.double_Password){
                        this.info = "Пароли должны совпадать"
                    }



                    if (this.info === ""){
                        //Сюда свойство регистрации
                    
                        store.commit("updateDoctor", this.doctor)

                        alert("Аккаунт успешно зарегистрирован")
                        router.push("/")
                    }
                }
                
                
            }
        }
    }
</script>



<style scoped>


*

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
    }

    .headbar {
        display: flex;
    }

    .auth {
        box-shadow: 3px -3px 1px 0px rgba(34, 60, 80, 0.2) inset;
    }

    .name {
        background-color: white;
        width: 40%;
        border-radius: 10px 10px 0 0;
        align-content: center;
        text-align: center;
        padding-top: 10px;
        height: 50px;
    }

    .main__view {
        background-color: white;
        padding: 35px;
        margin-left: auto;
        margin-right: auto;
        border-radius: 0px 10px 10px 10px;
    }

    .main__content {
        background-color: white;
        padding: 15px;
        display: flex;
        margin-left: auto;
        margin-right: auto;
        border-radius: 0px 0px 10px 10px;
    }

    .info_ {
        color: red;
        max-width: 300px;
    }

    .content__left {
        margin-left: 20px;
        margin-right: 100px;
    }

    .content__element {
        list-style-type: none;
        margin-bottom: 10px;
    }

    .content__element h3 {
        margin-bottom: 5px;;
    }


    .wrapper {
        text-align: center;
    }


    .btn {
        margin-left: auto;
        margin-right: auto;
        margin-top: 10px;
        background-color: green;
        text-align: center;
        align-content: center;
        border-radius: 5px;
        font-size: 20px;
        padding: 10px;
    }
    

    strong {
        margin-right: 15px;
    }


    .age__input {
        width: 70px;
        height: 30px;
        font-size: 20px;
    }



    .home_address__input {
        min-width: 200px;
        min-height: 50px;
        font-size: 20px;
    }

    .input {
        min-width: 200px;
        min-height: 25px;
        font-size: 20px;
    }

    



</style>