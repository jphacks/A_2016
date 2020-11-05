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

<style scoped>
/* .percentage {
  margin-top: 40px;
} */
#Card {
  /* display: block;
  background-color: blue;
  width: 100%;
  padding-top: 100%; */
}
</style>
