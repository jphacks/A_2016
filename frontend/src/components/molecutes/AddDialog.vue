<template>
  <dialog open id="Dialog">
    <h1>デバイスを追加</h1>
    <form>
      <input type="text" label="上に置くものの名前" />
      <input type="text" label="deviceId" />
      <input />
      <input />
      <input />
    </form>
  </dialog>
</template>

<script>
export default {
  name: 'AddDialog',
};
</script>

<style scoped>
#Dialog {
  width: 80%;
  height: 300px;
  border: 1px solid #111;
}
</style>