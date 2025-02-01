<template>
    <div class="namedBar">
        <div class="main">
            <h3 v-for="Name in names">{{ Name }}</h3>
        </div>
    </div>
</template>


<script>

    export default {
        name: 'named-bar',
        props: {
            names: {
                Type: Array,
                required: true
            }
        }
    }

</script>


<style scoped>

    .namedBar {
        padding-bottom: 10px;
    }

    .main {
        background-color: #D9D9D9;
        display: flex;
        padding: 5px;
        border-radius: 5px;

        h3 {
            margin: auto;
            padding: 5px 15px;
        }
    }
    

</style>