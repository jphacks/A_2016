<template>
  <v-card open>
    <v-card-title class="headline grey lighten-2">デバイスを追加</v-card-title>
    <p class="inputs">
      <label>上に置くものの名前: </label
      ><input type="text" v-model="item.item" />
    </p>
    <p class="inputs">
      <label>deviceId: </label> <input type="text" v-model="item.device_id" />
    </p>
    <p class="inputs">
      <label>最大容量: </label><input type="number" v-model="item.max" />
    </p>
    <p class="inputs">
      <label>最小容量: </label><input type="number" v-model="item.min" />
    </p>
    <p class="inputs">
      <label>期限</label>
    </p>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="secondary" text @click="register">登録</v-btn>
      <v-btn color="secondary" text @click="close">閉じる</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
// import Datepicker from 'vuejs-datepicker';
// import { ja } from 'vuejs-datepicker/dist/locale';
import { register } from '../../toServer/main';
// import 'vue-awesome/icons';
export default {
  name: 'AddDialog',

  components: {
    // Datepicker
  },

  data() {
    return {
      // DatePickerFormat: 'yyyy-MM-dd',
      // ja: ja,
      item: {
        item: '',
        device_id: '',
        max: 0,
        min: 0,
        expiration_date: '',
        color: '',
      },
    };
  },

  props: {
    deviceIdFromURL: {
      required: false,
      type: String,
    },
  },

  created() {
    if (this.deviceIdFromURL) {
      this.item.device_id = this.deviceIdFromURL;
    }
  },

  methods: {
    register() {
      const res = register(this.item);
      this.$emit('close-add-modal', res);
    },

    close() {
      this.$emit('close-add-modal', this.item);
    },
  },
};
</script>

<style scoped lang="scss">
.addDevice {
  margin-top: 0;
}
.inputs {
  display: flex;
  flex-direction: column;
  font-size: 14px;
  .register {
    background-color: black;
    color: white;
    border: none;
    border-radius: 7px;
    height: 44px;
    margin: 0 auto;
    display: block;
    width: 200px;
    font-weight: bold;
    font-size: 14px;
  }
}
input {
  border: none;
  border-bottom: 1px solid rgb(172, 172, 172);
  height: 30px;
  position: relative;
  &:focus {
    outline: none;
    border-bottom: 1px solid black;
  }
}
</style>
