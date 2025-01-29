<template>
    <button>
        <slot></slot>
    </button>
</template>


<script>
    export default {
        name: 'btn-auth'
    }
</script>


<style>
    button {
        margin-top: 0px;
        padding-top: 0px;
        border-radius: 0px 0px 15px 15px;
        border-top: 0px;
        background-color: #469C56;
        min-width: 12px;
        min-height: 10px;
    }
</style>