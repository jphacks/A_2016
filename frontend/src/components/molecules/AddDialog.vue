<template>
  <v-container>
    <v-card>
      <h2 class="text-center pt-7 font-weight-bold">
        {{ title || 'デバイスを追加' }}
      </h2>
      <v-stepper v-model="currentStep">
        <v-stepper-header>
          <v-stepper-step v-for="(step,i ) in steps" :key="i" :complete="currentStep > i+1" :step="i+1">
            {{step.header}}
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
                  </ValidationProvider>
                  <p>表示名を入力</p>
                  <v-text-field
                    v-model="item.item"
                    label="表示名"
                  />
                  <p>商品を検索</p>
                  <ValidationObserver ref="search" v-slot="{g}">
                  <ValidationProvider v-slot="{ errors }" rules="required">
                    <v-text-field
                      v-model="searchItem"
                      :error-messages="errors"
                    />
                  </ValidationProvider>
                  <v-btn @click="search" :disabled="g">
                    検索
                  </v-btn>
                  </ValidationObserver>
                  <v-row>
                    <v-col v-for="(item, i) in searchItems" :key="i" md="4" xs="6">
                      <v-img :src="item.imageUrl"  @click="putUrl(item.itemUrl)" />
                    </v-col>
                  </v-row>
                  <p style="margin-top:20px" @click="goForward">商品を登録しないで次に進む</p>
                </v-card-text>
              </v-stepper-content>

              <v-stepper-content step="2">
                <v-card-text>
                    <section>
                      <label v-show="isExistedContainer">容器を選択して下さい</label>
                      <label v-show="!isExistedContainer">最大容量・最小容量を入力してください</label>
                      <v-row v-show="isExistedContainer">
                        <v-col v-for="(container, i) in containers" :key="i" md="4" xs="6" >
                          <div class="container" @click="choiceContainer(container)">
                            <v-img :src="container.image" /> 
                          </div>
                        </v-col>
                      </v-row>
                    </section>
                    <div v-show="!isExistedContainer">
                      <v-text-field v-model="max" label="最大容量" />
                      <v-text-field v-model="min" label="最小容量"/>
                    </div>
                    <p v-show="isExistedContainer" style="margin-top:20px" @click="isExistedContainer = !isExistedContainer">容器がない場合</p>
                    <v-spacer />
                    <v-btn color="secondary" text @click="currentStep -=1">戻る</v-btn>
                    <v-btn v-if="!isExistedContainer" color="secondary" text @click="putMaxAndMin">次へ</v-btn>
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
                    <v-btn color="secondary" text @click="currentStep-=1">戻る</v-btn>
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
      </v-stepper>
    </v-card>
  </v-container>
</template>

<script>
import { ValidationObserver, ValidationProvider, extend } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';
import { getContainers, register, searchItem } from '../../toServer/main';
import { devicesStore } from '../../store/devices';

extend('required', {
  ...required,
  message: '空欄です.',
});

export default {
  name: 'AddDialog',

  data() {
    return {
      steps: [
        {
          header:"商品を選択"
        },
        {
          header:"容器を選択"
        },
        {
          header:"色・期限の設定"
        },
      ],
      url: '',
      max: '',
      min: '',
      currentStep: 1,
      dialogContainers: false,
      item: {
        item: '',
        url: '',
        device_id: '',
        max: 0,
        min: 0,
        expiration_date: '',
        color: '',
      },
      searchItem: '',
      searchItems: [],
      menu: false,
      containers: [],
      isChoicedProduct: false,
      isChoicedContainer: [],
      isExistedContainer: true,
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
    this.item.item = ''
    this.item.max = 0
    this.item.min = 0
    this.item.url = ''
    this.item.expiration_date = ''
    this.item.color = ''
  },

  mounted() {
    this.isExistedContainer = true
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
    goForward() {
      this.currentStep +=1
    },

    putUrl (url){
      this.item.url= url
      this.goForward()
    },

    putMaxAndMin () {
      this.item.max = this.max
      this.item.min = this.min
      this.goForward()
    },

    async search () {
      const isValid = this.$refs.search.validate()
      if (isValid && this.searchItem) {
        this.searchItems = await searchItem(this.searchItem)
      }
    },

    choiceContainer (container) {
      console.log('最大容量は'+ container.max + '最小容量は'+ container.min)
      this.item.max = container.max - 0 
      this.item.min = container.min - 0 
      this.goForward()
    },  

    async register() {
      const isValid = this.$refs.observer.validate();
      if (isValid && this.item.max && this.item.min) {
        if(!this.item.item) {
          this.item = this.searchItem 
        }
        var color = this.item.color;
        color = color.slice(0, 7);
        this.item.color = color;
        console.log(this.item);
        const res = register(this.item);
        this.$emit('close-add-modal', res);
      }
    },

    close() {
      this.$emit('close-add-modal', this.item);
    },
  },
};
</script>

<style scoped lang="scss">
p{
  cursor: pointer;
}

.container{
  background-color:seashell;
  cursor: pointer;
  box-shadow: 0px 3px rgb(201, 155, 123);
  user-select: none;
  border-radius: 10px;
}
.container:active{
  box-shadow: none;
  position: relative;
  top:3px
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
