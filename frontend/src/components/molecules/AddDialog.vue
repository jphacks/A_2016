<template>
  <v-container>
    <v-card>
      <h2 class="text-center pt-7 font-weight-bold">
        {{ title || 'デバイスを追加' }}
      </h2>

      <v-stepper v-model="currentStep">
        <v-stepper-header>
          <v-stepper-step :complete="currentStep > 1" step="1">
            デバイスID・表示名
          </v-stepper-step>
          <v-divider />
          <v-stepper-step :complete="currentStep > 2" step="2">
            容器を選択
          </v-stepper-step>
          <v-divider />
          <v-stepper-step :complete="currentStep > 3" step="3">
            期限・色の決定
          </v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <ValidationObserver ref="observer" v-slot="{ invalid }">
            <form>

              <v-stepper-content step="1">
                <v-card-text>
                  <ValidationProvider v-slot="{ errors }" rules="required">
                    <v-text-field
                      v-model="item.device_id"
                      :error-messages="errors"
                      label="デバイスID"
                    />
                    <!-- TODO: AMAZONAPIと連携 --->
                    <v-text-field
                      v-model="item.item"
                      :error-messages="errors"
                      label="名前"
                    />
                  </ValidationProvider>
                  <v-spacer />
                  <v-btn color="secondary" text @click="currentStep=2">次へ</v-btn>
                </v-card-text>
              </v-stepper-content>

              <v-stepper-content step="2">
                <v-card-text>
                    <section>
                      <!--TODO: componentに分ける --->
                      <label>容器を選択して下さい</label>
                      <v-row>
                        <v-col v-for="(container, i) in containers" :key="i" md="4" xs="6" >
                          <!-- <div class="container" @click="choice(container)">{{container.image}}</div> -->
                          <v-btn @click="choiceContainer(container, i)">
                            <v-img max-height="50px" max-width="100px" :src="container.image" />
                          </v-btn>
                        </v-col>
                      </v-row>
                    </section>
                    <p v-if="!item.max" color="red">容器を選択してください</p>
                    <v-btn color="secondary" text @click="currentStep=1">戻る</v-btn>
                    <v-btn color="secondary" text @click="currentStep=3">次へ</v-btn>
                </v-card-text>
              </v-stepper-content>

              <v-stepper-content step="3">
                <v-card-text>
                  <ValidationProvider rules="required">
                    <div class="step3">
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
                    </div>
                    <div class="step3">
                    <label>色</label>
                    <v-color-picker
                      v-model="item.color"
                      class="color"
                    ></v-color-picker>
                    </div>
                  </ValidationProvider>
                  <!-- <v-btn color="secondary" text @click="currentStep=2">戻る</v-btn> -->
                  <p v-if="!canModify" class="caption text-right mt-10 mr-3 font-weight-light">
                    デモ用のデバイスは変更できません。
                  </p>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn color="secondary" text @click="currentStep=2">戻る</v-btn>
                    <v-spacer />
                    <v-btn
                      color="secondary"
                      text
                      @click="register"
                      :disabled="invalid || !canModify"
                    >登録</v-btn>
                    <v-btn color="secondary" text @click="close">閉じる</v-btn>
                  </v-card-actions>
                </v-card-text>
              </v-stepper-content>
            </form>
          </ValidationObserver>
        </v-stepper-items>
              <!-- <ValidationProvider v-slot="{ errors }" rules="required">
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
              </ValidationProvider> -->
      </v-stepper>
    </v-card>
  </v-container>
</template>

<script>
import { ValidationObserver, ValidationProvider, extend } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';
import { register } from '../../toServer/main';
import { getContainers } from '../../toServer/main'
import { devicesStore } from '../../store/devices';

extend('required', {
  ...required,
  message: '空欄です.',
});

export default {
  name: 'AddDialog',

  data() {
    return {
      currentStep: 1,
      dialogContainers: false,
      item: {
        item: '',
        device_id: '',
        max: 0,
        min: 0,
        expiration_date: '',
        color: '',
      },
      menu: false,
      containers: [],
      isChoiced: []
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

  async created () {
    this.containers = await getContainers()
    for (let i=0;i<this.containers.length;i++){
      this.isChoiced.push(false)
    }
    // this.item.item = ''
    // this.item.max = 0
    // this.item.min = 0
    // this.item.expiration_date = ''
    // this.item.color = ''
  },

  mounted() {
    if (this.deviceIdFromURL) {
      this.item.device_id = this.deviceIdFromURL;
    }
    if (this.deviceId) {
      this.item.device_id = this.deviceId;
    }
    this.currentStep=1
    this.item.item = ''
    this.item.max = 0
    this.item.min = 0
    this.item.expiration_date = ''
    this.item.color = ''
  },

  watch: {
    deviceId: function (val) {
      this.item.device_id = val;
    },
  },

  methods: {
    choiceContainer (container, num) {
      console.log('最大容量は'+ container.max + '最小容量は'+ container.min)
      this.item.max = container.max
      this.item.min = container.min
      // どこが選択されているかの処理。これに応じてbtnの色を変えるが、いい方法があれば違う方法にする
      for (let i=0;i<this.isChoiced;i++){
        if (this.isChoiced[i] === true ){
          this.isChoiced[i] = false
        }
      }
      this.isChoiced[num] = true
    },  

    async register() {
      const isValid = this.$refs.observer.validate();
      if (isValid && this.item.max && this.item.min) {
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
.container{
  background-color:seashell;
  cursor: pointer;
}
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

// .step3{
//   display: inline;
// }
</style>
