<template>
    <div class="dialog" @click.stop="$emit('update:show', false)">
        <div @click.stop class="dialog__content">
            <slot></slot>
        </div>
    </div>
</template>


<script>

    export default {
        name: 'my-dialog',
        props: {
            show: {
                Type: Boolean,
                default: false
            }
        }
    }

</script>


<style>

    .dialog {
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(0, 0, 0, 0.5);
        position: fixed;
        display: flex;
    }

    .dialog__content {
        margin: auto;
        background: white;
        border-radius: 12px;
        min-height: 50px;
        min-width: 300px;
        padding: 20px;
    }

</style>