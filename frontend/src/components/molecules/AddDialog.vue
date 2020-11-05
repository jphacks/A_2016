<template>
  <dialog open id="Dialog">
    <h1>デバイスを追加</h1>
    <p>
      <label>上に置くものの名前: </label
      ><input type="text" v-model="item.item" />
    </p>
    <p>
      <label>deviceId: </label> <input type="text" v-model="item.device_id" />
    </p>
    <p><label>最大容量: </label><input type="number" v-model="item.max" /></p>
    <p><label>最小容量: </label><input type="number" v-model="item.min" /></p>
    <p><button @click="click">登録</button></p>
  </dialog>
</template>

<script>
import { register } from '../../toServer/main';

export default {
  name: 'AddDialog',

  data() {
    return {
      item: {
        item: '',
        device_id: '',
        max: 0,
        min: 0,
      },
    };
  },

  methods: {
    click() {
      const res = register(this.item);
      console.log(res);
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
