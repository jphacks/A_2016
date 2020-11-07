<template>
  <div>
    <v-card>
      <h2 class="text-center pt-7 font-weight-bold">
        {{ title || 'デバイスを追加' }}
      </h2>
      <ValidationObserver ref="observer" v-slot="{ invalid }">
        <form>
          <div class="card-items">
            <v-card-text>
              <ValidationProvider v-slot="{ errors }" rules="required">
                <v-text-field
                  v-model="item.item"
                  :error-messages="errors"
                  label="名前"
                />
              </ValidationProvider>
              <ValidationProvider v-slot="{ errors }" rules="required">
                <v-text-field
                  v-model="item.device_id"
                  :error-messages="errors"
                  label="デバイスID"
                />
              </ValidationProvider>
              <ValidationProvider v-slot="{ errors }" rules="required">
                <v-text-field
                  v-model="item.max"
                  :error-messages="errors"
                  label="最大容量"
                />
              </ValidationProvider>
              <ValidationProvider v-slot="{ errors }" rules="required">
                <v-text-field
                  v-model="item.min"
                  :error-messages="errors"
                  label="最小容量"
                />
              </ValidationProvider>
              <ValidationProvider rules="required">
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
                  <v-dialog v-model="menu" max-width="400px" hide-overlay>
                    <v-date-picker
                      v-model="item.expiration_date"
                      @input="menu = false"
                    ></v-date-picker>
                  </v-dialog>
                </v-menu>
              </ValidationProvider>
              <ValidationProvider rules="required">
                <label>色</label>
                <v-color-picker
                  v-model="item.color"
                  class="color"
                ></v-color-picker>
              </ValidationProvider>
            </v-card-text>
          </div>
        </form>
        <p
          v-if="!canModify"
          class="caption text-right mt-10 mr-3 font-weight-light"
        >
          デモ用のデバイスは変更できません。
        </p>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="secondary"
            text
            @click="register"
            :disabled="invalid || !canModify"
            >登録</v-btn
          >
          <v-btn color="secondary" text @click="close">閉じる</v-btn>
        </v-card-actions>
      </ValidationObserver>
    </v-card>
  </div>
</template>

<script>
import { ValidationObserver, ValidationProvider, extend } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';
import { register } from '../../toServer/main';
import { devicesStore } from '../../store/devices';

extend('required', {
  ...required,
  message: '空欄です.',
});

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

  components: {
    ValidationObserver,
    ValidationProvider,
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
    deviceId: {
      required: false,
      type: String,
    },
  },

  computed: {
    canModify() {
      return !devicesStore.state.adminIds.includes(this.item?.device_id);
    },
  },

  mounted() {
    if (this.deviceIdFromURL) {
      this.item.device_id = this.deviceIdFromURL;
    }
    if (this.deviceId) {
      this.item.device_id = this.deviceId;
    }
  },

  watch: {
    deviceId: function (val) {
      this.item.device_id = val;
    },
  },

  methods: {
    async register() {
      const isValid = this.$refs.observer.validate();
      if (isValid) {
        var color = this.item.color;
        color = color.slice(0, 7);
        this.item.color = color;
        console.log(this.item);
        const res = register(this.item);
        this.$emit('close-add-modal', res);
      }
      // this.$emit('close-add-modal',this.item)
    },

    close() {
      this.$emit('close-add-modal', this.item);
    },
  },
};
</script>

<style scoped lang="scss">
.v-card {
  color: #777777 !important;
  font-family: 'Exo', sans-serif;
}

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

.v-dialog {
  -webkit-box-shadow: 0 0 0;
  box-shadow: 0 0 0;
  border-radius: 10px;
  border: 1px solid #c3c3c3;
}
</style>
