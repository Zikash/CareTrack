<template>

    <form @submit.prevent>
        
        <div>
            <h2 class="name">{{ Name }}</h2>
            <br/>
            <div class="main">
                <slot></slot>
            </div>
        </div>
        

    </form>

</template>


<script>

    export default {
        name: 'my-form',
        props: {
            Name: {
                Type: String,
                require: true
            }
        }
    }

</script>


<style scoped>

    .name {
        background-color: white;
    }

    br {
        height: 0px;
    }

    .main slot{
        background-color: white;
    }

</style>