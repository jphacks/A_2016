<template>
  <section @click="openModal" class="itemCard">
    <p class="name">{{ info.item }}</p>
    <h1 class="percentage">{{ Math.round(info.percentage) }}<span> %</span></h1>
    <div class="triangle"></div>
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
  font-size: 16px;
  font-weight: 500;
  // font-family: 'Shrikhand', cursive;
  span {
    font-size: 12px;
  }
}
.triangle {
  position: absolute;
  border-right: 8px solid transparent;
  border-bottom: 8px solid #6c6c6c;
  border-left: 8px solid transparent;
  transform: rotate(135deg);
  bottom: 4px;
  right: 0px;
}
.name {
  font-size: 15px !important;
}
</style>
