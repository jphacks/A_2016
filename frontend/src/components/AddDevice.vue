<template>
  <section id="AddDevice">
    <AddDialog @close-modal="closeModal" v-if="isOpened" />
    <section>
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

    closeModal(res) {
      console.log('close');
      this.$emit('add', res);
      this.isOpened = false;
    },
  },
};
</script>

<style scoped>
#AddDevice {
  width: 100%;
  padding-top: 100%;
}
</style>
