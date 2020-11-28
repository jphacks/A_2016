<template>
  <v-container>
    <v-card>
      <h2 class="text-center pt-7 font-weight-regular">
        {{ title || 'デバイスを追加' }}
      </h2>
      <v-stepper v-model="currentStep">
        <v-stepper-header>
          <section v-for="(step, i) in steps" :key="i">
            <v-stepper-step
              :complete="currentStep > i + 1"
              :step="i + 1"
              color="#333333"
            >
              {{ step.header }}
            </v-stepper-step>
          </section>
        </v-stepper-header>

        <v-stepper-items>
          <ValidationObserver ref="observer" v-slot="{ invalid }">
            <form>
              <v-stepper-content step="1">
                <v-card-text>
                  <p>デバイスIDを入力</p>
                  <ValidationProvider v-slot="{ errors }" rules="required">
                    <v-text-field
                      v-model="item.device_id"
                      :error-messages="errors"
                      label="デバイスID"
                    />
                  </ValidationProvider>
                  <p style="margin-top: 20px">表示名を入力（必須）</p>
                  <v-text-field v-model="item.item" label="表示名" />
                  <p style="margin-top: 20px">商品を検索・登録（任意）</p>
                      <v-text-field
                        v-model="searchItem"
                        label="検索ワード"
                        append-icon="mdi-magnify"
                        @click:append="search"
                        @input="handleSearchChanged"
                      />
                  <v-list>
                    <v-list-item
                      link
                      v-for="(item, index) in searchItems.slice(0, 9)"
                      :key="index"
                      @click="putUrl(item.itemUrl)"
                    >
                      <v-list-item-avatar>
                        <v-img :src="item.imageUrl"></v-img>
                      </v-list-item-avatar>
                      <v-list-item-content>
                        <v-list-item-title>{{ item.name }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                  <p
                    style="margin-top: 20px; font-size: 100%"
                    @click="goForward"
                  >
                    商品を登録しないで次に進む
                  </p>
                </v-card-text>
              </v-stepper-content>

              <v-stepper-content step="2">
                <v-card-text>
                  <section>
                    <label v-show="isExistedContainer"
                      >容器を選択して下さい</label
                    >
                    <label v-show="!isExistedContainer"
                      >最大容量・最小容量を入力してください</label
                    >
                    <v-row v-show="isExistedContainer">
                      <v-col v-for="(container, i) in containers" :key="i">
                        <div
                          class="container-image"
                          justify="space-around"
                          @click="choiceContainer(container)"
                        >
                          <img :src="container.image" />
                          <p class="container-name">{{ container.name }}</p>
                        </div>
                      </v-col>
                    </v-row>
                  </section>
                  <div v-show="!isExistedContainer">
                    <v-text-field v-model="max" label="最大容量" />
                    <v-text-field v-model="min" label="最小容量" />
                  </div>
                  <p
                    v-show="isExistedContainer"
                    style="margin-top: 20px"
                    @click="isExistedContainer = !isExistedContainer"
                  >
                    容器がない場合
                  </p>
                  <v-spacer />
                  <v-btn color="secondary" text @click="currentStep -= 1"
                    >戻る</v-btn
                  >
                  <v-btn
                    v-if="!isExistedContainer"
                    color="secondary"
                    text
                    @click="putMaxAndMin"
                    >次へ</v-btn
                  >
                </v-card-text>
              </v-stepper-content>

              <v-stepper-content step="3">
                <v-card-text>
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
                    <div class="step3" style="margin-top:30px">
                      <label>色を選択</label>
                      <div style="margin-top:20px">
                        <v-icon class="box" :style="`background-color: ${item.color};border:1px solid #111`" @click="random">mdi-recycle</v-icon>
                        <v-card flat max-width="200px" style="padding-left:10px; margin:10px auto">
                          <v-row>
                            <v-col
                              v-for="(co, i) in colorArr"
                              :key="i"
                              md="4"
                            >
                            <div id="box" :style="`background-color: ${co}; width:30px;height:30px;padding-left:10px;border:1px solid azure`" @click="choiceColor(co)"></div>
                            </v-col>
                          </v-row>
                        </v-card>
                      </div>
                    </div>
                  <!-- <v-btn color="secondary" text @click="currentStep=2">戻る</v-btn> -->
                  <p
                    v-if="!canModify"
                    class="caption text-right mt-10 mr-3 font-weight-light"
                  >
                    デモ用のデバイスは変更できません。
                  </p>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn color="secondary" text @click="currentStep -= 1"
                      >戻る</v-btn
                    >
                    <v-btn
                      color="secondary"
                      text
                      @click="register"
                      :disabled="invalid || !canModify"
                      >登録</v-btn
                    >
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
import {
  getContainers,
  postDevices,
  searchItem,
} from '../../toServer/v2/index';
import { devicesStore } from '../../store/devices';

extend('required', {
  ...required,
  message: '空欄です.',
});

export default {
  name: 'AddDialog',

  data() {
    return {
      colorArr:[
        '#fffafa', '#ffe4c4', '#f0fff0', '#87ceeb', '#3cb371','#ff0000','#ffa500','#d8bfd8','#8a2be2'
      ],
      steps: [
        {
          header: '商品を選択',
        },
        {
          header: '容器を選択',
        },
        {
          header: '色・期限の設定',
        },
      ],
      url: '',
      max: '',
      min: '',
      currentStep: 1,
      dialogContainers: false,
      color: '',
      // colorpicker: false,
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
      lastSearched: 0,
      searching: false,
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
    name: {
      required: false,
      type: String,
    },
    reset: {
      required: false,
      type: Boolean,
    },
  },

  computed: {
    canModify() {
      return !devicesStore.state.adminIds.includes(this.item?.device_id);
    },
  },

  async created() {
    this.containers = await getContainers();
    this.item.url = '';
    this.item.expiration_date = '';
    this.item.color = '';
    this.currentStep = 1;
  },

  mounted() {
    this.isExistedContainer = true;
    if (this.deviceIdFromURL) {
      console.log('a');
      this.item.device_id = this.deviceIdFromURL;
    }
    if (this.deviceId) {
      this.item.device_id = this.deviceId;
    }
    if (this.name) {
      this.item.item = this.name;
    }
    this.currentStep = 1;
  },

  watch: {
    deviceId: function (val) {
      this.item.device_id = val;
    },
    reset: function () {
      this.currentStep = 1;
      this.isExistedContainer = true;
    },
  },

  methods: {
    random() {
      var num = Math.floor(Math.random()*9)
      this.item.color = this.colorArr[num]
    },

    goForward() {
      this.currentStep += 1;
    },

    putUrl(url) {
      this.item.url = url;
      this.goForward();
    },

    putMaxAndMin() {
      this.item.max = this.max;
      this.item.min = this.min;
      this.goForward();
    },

    choiceColor(co) {
      this.color=co
      this.item.color = co
      // this.colorpicker = false
    },

    async handleSearchChanged() {
      if (Date.now() - this.lastSearched > 1000) {
        if (!this.searching) {
          this.lastSearched = Date.now();
          await this.search();
        }
      }
      const q = this.searchItem;
      setTimeout(() => {
        if (q === this.searchItem) {
          console.log(q);
          this.lastSearched = Date.now();
          this.search();
        }
      }, 2000);
    },

    async search() {
      // const isValid = this.$refs.search.validate();
      if (this.searchItem) {
        try {
          this.searchItems = await searchItem(this.searchItem);
        } catch (err) {
          this.searchItems = [];
        }
      }
    },

    choiceContainer(container) {
      console.log('最大容量は' + container.max + '最小容量は' + container.min);
      this.item.max = container.max - 0;
      this.item.min = container.min - 0;
      this.goForward();
    },

    async register() {
      console.log("www")
      const isValid = await this.$refs.observer.validate();
      if (!this.item.item) {
        this.item = this.searchItem;
      }
      console.log(isValid, this.item.max, this.item.min)
      if (isValid && this.item.max) {
        console.log('sss')
        var color = this.item.color;
        this.item.color = color;
        console.log(this.item);
        const res = postDevices(this.item);
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
.box{
  padding-top:-5px;
  padding-bottom: -5px;
  border:1px solid #444;
  border-radius: 5px;
  background-color: indianred;
  width:40px;
  height:40px;
}
.v-stepper {
  box-shadow: none;
}
.v-stepper__header {
  box-shadow: none;
}
.container {
  padding: 0;
  box-shadow: 0px 3px rgb(201, 155, 123);
  user-select: none;
  border-radius: 10px;
}
.container-image {
  height: 70px;
  width: 70px;
  margin: 0 auto;
  padding: 5px;
  border: 1px solid #888888;
  border-radius: 5px;
  img {
    height: 100%;
    object-fit: contain;
  }
  .container-name {
    font-size: 10px;
  }
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
