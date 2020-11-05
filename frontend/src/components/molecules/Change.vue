<template>
  <dialog open id="Dialog">
    <h1>Id:{{ changeItemId }}の用途変更</h1>
    <p><label>用途</label><input v-model="item" type="text" /></p>
    <p><label>最大容量</label><input v-model="max" type="number" /></p>
    <p><label>最小容量</label><input v-model="min" type="number" /></p>
  </dialog>
</template>

<script>
export default {
  name: 'Change',

  props: {
    changeItemId: {
      type: String,
      required: true,
    },
  },

  data() {
    return {};
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
