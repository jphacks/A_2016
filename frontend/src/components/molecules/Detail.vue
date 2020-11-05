<template>
  <dialog open id="Dialog">
    <h1>詳細</h1>
    <button class="button" @click="change">変更</button>
    <button class="button" @click="close">閉じる</button>
  </dialog>
</template>

<script>
export default {
  name: 'Detail',

  props: {
    item: {
      required: true,
      type: Object,
    },
  },

  methods: {
    close() {
      this.$emit('close-detail-modal');
    },

    change() {
      this.$emit('close-detail-modal');
      this.$emit('open-change-modal', this.item);
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
