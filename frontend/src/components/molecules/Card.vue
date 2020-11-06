<template>
  <section @click="openModal" class="itemCard">
    <h1 class="percentage">id: {{ info.percentage }}</h1>
    <h1 class="name">{{ info.item }}</h1>
  </section>
</template>

<script>
export default {
  name: 'Card',

  props: {
    info: {
      type: Object,
      required: true,
    },
  },

  methods: {
    openModal() {
      this.$emit('open-detail-modal', this.info);
    },
  },
};
</script>

<style scoped lang="scss"></style>
