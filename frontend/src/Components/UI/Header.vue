<template>
    <header class="header">
        
        <div class="logo">
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
</template>


<script>

    export default {
        name: "my-header",
    }

</script>


<style>
    * {
        color: black
    }

    ul, li {
        list-style: none;
    }

    .header {
        height: 60px;
        background-color: #009933;
        display: flex;
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
</style>