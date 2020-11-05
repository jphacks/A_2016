<template>
  <section @click="openModal" class="itemCard">
    <div id="Card">
      <h1 class="percentage">id: {{ info.device_id }}</h1>
      <h1 class="name">{{ info.item }}</h1>
    </div>
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
