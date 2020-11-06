<template>
  <div @click="openModal" class="itemCard">
    <section class="card">
      <h1 class="percentage">id: {{ info.device_id }}</h1>
      <h1 class="name">{{ info.item }}</h1>
    </section>
  </div>
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

<style scoped lang="scss">
.itemCard {
  height: 100%;
}
</style>
