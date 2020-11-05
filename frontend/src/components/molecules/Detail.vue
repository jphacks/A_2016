<template>
  <dialog open id="Dialog">
    <h1>詳細</h1>
    <button @click="close">閉じる</button>
  </dialog>
</template>

<script>
export default {
  name: 'Detail',

  methods: {
    close() {
      this.$emit('close-modal');
    },
  },
};
</script>

<style scoped>
#Dialog {
  width: 80%;
  height: 300px;
  border: 1px solid #111;
}
</style>
