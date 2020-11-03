<template>
  <section>
    <AddDialog @close-modal="closeModal" v-if="isOpened" />
    <section id="AddDevice">
      <AddButton @open-modal="openModal" />
    </section>
  </section>
</template>

<script>
import AddButton from './molecules/AddButton';
import AddDialog from './molecules/AddDialog';

export default {
  name: 'AddDevice',
  components: {
    AddButton,
    AddDialog,
  },

  data() {
    return {
      isOpened: false,
    };
  },

  methods: {
    openModal() {
      this.isOpened = true;
      console.log(this.isOpened);
    },

    closeModal() {
      console.log('close');
      this.isOpened = false;
    },
  },
};
</script>

<style scoped>
#AddDevice {
  width: 200px;
  height: 300px;
  border: 2px dotted #111;
  border-radius: 30px;
}
</style>
