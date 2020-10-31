<template>
    <section id="AddDevice">
        <AddButton @open-modal="openModal" />
        <AddDialog v-if="isOpened"/>
    </section>
</template>

<script>
import AddButton from './molecutes/AddButton'
import AddDialog from './molecutes/AddDialog'

export default {
    name: 'AddDevice',
    components: {
        AddButton,
        AddDialog
    },

    data () {
        return {
            isOpened: false
        }
    },

    methods: {
        openModal () {
            this.isOpened= true
        }
    }
}
</script>

<style scoped>
#AddDevice {
    width: 200px;
    height: 300px;
    border: 2px dotted #111;
    border-radius: 30px;
}
</style>