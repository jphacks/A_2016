<template>
  <section @click="openModal" class="itemCard">
    <h1 class="percentage">
      {{ Math.round(info.percentage) }}<span class="p"> %</span>
    </h1>
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

<style scoped lang="scss">
.percentage {
  font-size: 250%;
  font-weight: 300;
  font-family: 'Exo', sans-serif;
  // font-family: 'Shrikhand', cursive;
}
.p {
  font-size: 1.2rem;
}
.name {
  font-size: 16px !important;
}
</style>
