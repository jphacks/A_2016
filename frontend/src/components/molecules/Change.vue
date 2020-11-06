<template>
  <dialog open id="Dialog">
    <h1>Id:{{ changeItemId }}の用途変更</h1>
    <p><label>用途</label><input v-model="item" type="text" /></p>
    <p><label>最大容量</label><input v-model="max" type="number" /></p>
    <p><label>最小容量</label><input v-model="min" type="number" /></p>
    <p><label>色</label><input v-model="color" type="text" /></p>
    <p><label>期限</label><input v-model="expiration_date" type="text" /></p>
    <p class="inputs"><button @click="change">変更</button></p>
    <p class="inputs"><button @click="close">閉じる</button></p>
  </dialog>
</template>

<script>
import { register } from '../../toServer/main';
export default {
  name: 'Change',

  props: {
    changeItemId: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      item: '',
      max: 0,
      min: 0,
      color: '',
      expiration_date: '',
    };
  },

  methods: {
    async change() {
      const res = await register({
        item: this.item,
        device_id: this.changeItemId,
        max: this.max,
        min: this.min,
        color: this.color,
        expiration_date: this.expiration_date,
      });
      this.$emit('change-list', res);
      this.$emit('close-change-modal');
    },

    close() {
      this.$emit('close-change-modal');
    },
  },
};
</script>

<style scoped>
#Dialog {
  z-index: 10000;
  width: 80%;
  height: 300px;
  border: 1px solid #111;
}
</style>
