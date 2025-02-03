<template>
    <select :value="modelValue" @change="changeOption">
        <option 
        v-for="user in users"
        :key="user.id"
        :value="user.id">
            {{ user.surname }} {{ user.name }} {{ user.patronymic }}
        </option>

    </select>
</template>


<script>

    export default {
        name: 'select-user',
        props: {
            modelValue: {
                type: Object,
                required: true
            },
            users: {
                Type: Array,
                required: true
            }
        },
        methods: {
            changeOption(event) {
                this.$emit("update:modelValue", event.target.value)
            }
        }
    }

</script>


<style scoped>
</style>