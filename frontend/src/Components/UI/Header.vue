<template>

    <div>
        <header class="header">
        
            <div class="logo" @click="$router.push('/')">
                <div class="icon">
                </div>
                <div class="name">
                    <h1>Медицина</h1>
                </div>
            </div>

            <ul class="wrapps">
                <li class="wrapps__element">
                    <h3>Врачи</h3>
                </li>
                <li class="wrapps__element">
                    <h3>Новости</h3>
                </li>
                <li class="wrapps__element">
                    <h3>Дополнительная информация</h3>
                </li>
            </ul>
        </header>

        <div class="auth" v-if="Auth">
            <div>
                <btn-auth @click="swapAuth" class="btn"><h3>Профиль</h3></btn-auth>   
            </div>
        </div>
        <div class="nauth" v-else>
            <div>
                <btn-auth @click="swapAuth" class="btn join"><h3>Войти</h3></btn-auth>
                <btn-auth @click="$router.push('/registration')" class="btn reg"><h3>Зарегистрироваться</h3></btn-auth>
            </div>
        </div>
    </div>
    
</template>


<script>

    export default {
        name: "my-header",
        data() {
            return {
                Auth: true
            }
        },
        methods: {
            swapAuth() {
                this.Auth = !this.Auth
            }
        }
    }

</script>


<style scoped>
    * {
        color: black
    }

    ul, li {
        list-style: none;
    }

    .header {
        top: 0;
        height: 60px;
        background-color: #009933;
        display: flex;
        position: sticky;
    }

    .logo {
        align-self: center;
        display: flex;
    }

    .icon {
        margin-left: 6px;
        align-self: center;
        background: red;
        height: 40px;
        width: 40px;
    }

    .name {
        margin-left: 10px;
        align-self: center;
    }

    .wrapps {
        margin: auto;
        display: flex;
        align-self: center;
        justify-self: center;
    }

    .wrapps__element {
        margin-left: 60px;
    }


    .auth {
        height: 50px;
        margin-top: 0px;
        padding-top: 0px;
        display: flex;
    }

    .nauth {
        height: 50px;
        margin-top: 0px;
        padding-top: 0px;
        display: flex;
    }

    .auth div {
        margin-top: 0px;
        padding-top: 0px;
        margin-left: auto;
        display: flex;
    }

    .nauth div {
        margin-top: 0px;
        padding-top: 0px;
        margin-left: auto;
        display: flex;
    }

    .nauth div {
        width: auto;
        margin-right: auto;
    }

    .auth div {
        width: 100px;
        margin-right: 25%;
    }

    .auth .btn {
        min-width: 100%;
    }

    .nauth .btn.join {
        width: 100px;
    }

    .nauth .btn.reg {
        width: 200px;
    }

    .btn:hover {
        background: #007527;
        padding-top: 5px;
    }

</style>
