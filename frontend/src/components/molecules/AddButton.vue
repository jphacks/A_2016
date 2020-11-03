<template>
  <button @click="openModal">
    <span class="add">+</span>
    <h1>追加する</h1>
  </button>
</template>

<script>
export default {
  methods: {
    openModal() {
      console.log('emmitted');
      this.$emit('open-modal');
    },
  },
};
</script>

<style scoped>
.add {
  margin-top: 30px;
  font-size: 80px;
}
</style>
