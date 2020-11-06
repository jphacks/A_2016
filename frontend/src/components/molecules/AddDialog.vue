<template>
  <dialog open id="Dialog">
    <h2 class="addDevice">デバイスを追加</h2>
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
      <v-menu
        v-model="menu"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="100px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="item.expiration_date"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="item.expiration_date"
          @input="menu = false"
        ></v-date-picker>
      </v-menu>
    </p>
    <p class="inputs">
      <label>色</label><input type="text" v-model="item.color" />
    </p>
    <p class="inputs">
      <button @click="register" class="register">登録</button>
    </p>
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
        expiration_date: '',
        color: '',
      },
      menu: false
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
    async register() {
      console.log(this.item)
      await this.item.expiration_date.toISOString()
      const res = register(this.item);
      this.$emit('close-add-modal', res);
      // this.$emit('close-add-modal',this.item)
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
#Dialog {
  z-index: 100000;
  width: 95%;
  max-width: 500px;
  border: 1px solid #111;
  height: 500px;
  text-align: left;
  border-radius: 10px;
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
