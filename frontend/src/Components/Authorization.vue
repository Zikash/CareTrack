<template>
        
    <form class="form" @submit.prevent>
        
        <div class="main">
            <div class="headbar">
                <h2 @click="$store.commit('updateAuth', 'reg')" class="name reg">Регистрация</h2>
                <h2 class="name auth">Авторизация</h2>
            </div>
            
        
            <div class="main__view">

                <h3 class="info_">{{ info }}</h3>

                <div class="main__content">
                    <ul class="content">
                        <li class="content__element">
                            <h3>Логин</h3>
                            <input v-model="login" class="surname_input input" type="text">

                        </li>
                        <li class="content__element">
                            <h3>Пароль</h3>
                            <input v-model="password" class="password__input input" type="password">
                        </li>
                    </ul>

                </div>

                <div class="wrapper">
                    <button @click="Auth($router)" class="btn">Авторизоваться</button>
                </div>

                
            </div>
        </div>
        
        
    </form>

</template>



<script>
import { initCustomFormatter } from 'vue';

export default {
data() {
    return {
        login: "",
        password: "",
        info: ""
    }
},
methods: {
    Auth(router) {

        

        //Сюда свойство авторизации

        if (this.login == 'doctor' && this.password == '1111'){
            this.$store.commit("updateDoctor", {
                phone: '8 999 999 99-99',
                Mail: "niPobelov@sss",
                Experience: 1,
                Serviced_area_number: 1,
                job_title: "Пульмонолог"
            })
        }

        if (this.login == 'admin' && this.password == '0000'){
            this.$store.commit("updateAdministrator", {
                phone: '888888888',
                Mail: "dddd@sss"
            })
        }


        alert("Вы успешно авторизовались")


        router.push("/")
        
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

.reg {
box-shadow: -3px -3px 1px 0px rgba(34, 60, 80, 0.2) inset;
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

.content {
    margin-left: auto;
    margin-right: auto;
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