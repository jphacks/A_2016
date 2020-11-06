<template>
  <v-card open>
    <v-card-title class="headline grey lighten-2">{{
      title || 'デバイスを追加'
    }}</v-card-title>
    <div class="card-items">
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
          <v-dialog v-model="menu" max-width="400px">
            <v-date-picker
              v-model="item.expiration_date"
              @input="menu = false"
            ></v-date-picker>
          </v-dialog>
        </v-menu>
      </p>
      <p class="inputs">
        <label>色</label>
        <v-color-picker v-model="item.color" class="color"></v-color-picker>
      </p>
    </div>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="secondary" text @click="register">登録</v-btn>
      <v-btn color="secondary" text @click="close">閉じる</v-btn>
    </v-card-actions>
  </v-card>
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
      menu: false,
    };
  },

  props: {
    deviceIdFromURL: {
      required: false,
      type: String,
    },
    title: {
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
      var color = this.item.color;
      color = color.slice(0, 7);
      this.item.color = color;
      console.log(this.item);
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
.color {
  margin: 0 auto;
}
.card-items {
  margin: 30px 0;
}
.addDevice {
  margin-top: 0;
}
.inputs {
  display: flex;
  flex-direction: column;
  font-size: 14px;
  padding: 0 30px;
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
