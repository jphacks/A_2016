<template>
  <section>
    <v-progress-circular
      v-show="loading"
      :size="100"
      class="circle"
      color="#cd853f"
      indeterminate
    ></v-progress-circular>
    <transition name="fade">
      <section v-show="!loading" id="lists">
        <div
          v-for="(item, i) in devices"
          :key="i"
          class="listCard"
          @click="openDetailModal(item)"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            version="1.1"
            viewBox="0 0 100 100"
            preserveAspectRatio="none"
            id="svg-bg"
            class="wave"
            :style="`top:${
              item && item.percentage <= 0
                ? 177
                : 175 - (item && item.percentage * 1.75)
            }px;animation-name:wave${
              Math.abs(
                item &&
                  item.item.split('').reduce((a, b) => {
                    a = (a << 5) - a + b.charCodeAt(0);
                    return a & a;
                  }, 0)
              ) % 5
            };`"
          >
            <path
              d="M0,0 v50 q10,10 20,0 t20,0 t20,0 t20,0 t20,0 v-50 Z"
              :fill="`${item && item.color ? item.color : whitesmoke}`"
            ></path>
          </svg>
          <div
            class="colorBox"
            :style="`height: ${
              item && item.percentage <= 10
                ? 1
                : item && item.percentage * 1.75 - 10
            }px;backgroundColor:${
              item && item.color ? item.color : '#efebe9'
            }; `"
          />
          <Card :info="item" />
        </div>
        <v-row justify="center">
          <v-dialog v-model="isOpenedDetail" max-width="400px" hide-overlay>
            <Detail @close-detail-modal="closeDetailModal" :item="detailItem" />
          </v-dialog>
        </v-row>
      </section>
    </transition>
    <v-btn icon color="white" @click="openAddModal" class="plus">
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <v-row justify="center">
      <v-dialog v-model="isOpenedAdd" max-width="900px" hide-overlay>
        <AddDialog
          @close-add-modal="closeAddModal"
          :deviceIdFromURL="deviceIdFromURL"
          :reset="reset"
        />
      </v-dialog>
    </v-row>
  </section>
</template>

<script>
import Card from './molecules/Card';
import Detail from '../components/molecules/Detail';
import AddDialog from './molecules/AddDialog';
import { devicesStore } from '../store/devices';

export default {
  name: 'List',

  components: {
    Card,
    Detail,
    AddDialog,
  },

  data() {
    return {
      isOpenedDetail: false,
      detailItem: {},
      changeItem: {},
      loading: true,
      isOpenedAdd: false,
      deviceIdFromURL: '',
      reset: false,
    };
  },

  created() {
    this.fetchDevices();
    setInterval(() => {
      this.fetchDevices();
    }, 3000);
  },

  computed: {
    devices() {
      return devicesStore.state.devices
        .sort((a, b) => {
          return a.device_id < b.device_id ? 1 : -1;
        })
        .map((device) => {
          const percentage = Math.min(100, Math.max(0, device.percentage));
          return {
            id: device.id,
            url: device.url,
            item: device.item,
            weight: device.weight,
            percentage: percentage,
            color: device.color,
            expiration_date: device.expiration_date,
          };
        });
    },
  },

  async mounted() {
    this.query = new URLSearchParams(location.search.slice(1));
    this.deviceIdFromURL = this.query?.get('d');
    if (this.deviceIdFromURL) {
      this.isOpenedAdd = true;
    }
  },

  methods: {
    openAddModal() {
      this.isOpenedAdd = true;
      this.reset = !this.reset;
    },

    async closeAddModal() {
      await devicesStore.dispatch('fetchDevices');
      this.isOpenedAdd = false;
      this.deviceIdFromURL = '';
      this.query?.delete('d');
      history.pushState('', '', '?' + this.query?.toString());
    },

    openDetailModal(item) {
      this.isOpenedDetail = true;
      this.detailItem = item;
    },

    async closeDetailModal() {
      this.isOpenedDetail = false;
      this.fetchDevices();
    },

    fetchDevices() {
      devicesStore
        .dispatch('fetchDevices')
        .then(() => {
          this.loading = false;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style lang="scss">
.circle {
  margin-top: 100px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
#Dialog {
  z-index: 100000;
  width: 80%;
  height: 500px;
  border-radius: 10px;
  display: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px;
}

#lists {
  width: 90%;
  max-width: 950px;
  margin: 0 auto;
  padding-top: 10px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 15px;
  .listCard {
    background-color: white;
    margin: 0px auto;
    width: 100%;
    max-width: 200px;
    height: 175px;
    overflow: hidden;
    // border: 1px solid #c3c3c3;
    box-shadow: 0 0 0 1px #c3c3c3;
    border-radius: 7px;
    cursor: pointer;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    // mix-blend-mode: hue;
    .percentage {
      position: absolute;
      transform: translateX(-50%);
      left: 50%;
      bottom: 10px;
      mix-blend-mode: difference;
    }
    .name {
      position: absolute;
      top: 8px;
      left: 8px;
      mix-blend-mode: difference;
      width: calc(100% - 12px);
      font-size: 10px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 1;
      overflow: hidden;
      text-align: left;
      // mix-blend-mode: lighten;
    }
  }
}
.addButton {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white !important;
  border: 1px dashed #c3c3c3 !important;
  h1 {
    border: none !important;
  }
}
.v-btn--icon.v-size--default {
  width: 60px;
  height: 60px;
  background-color: #6c6c6c;
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  bottom: 80px;
  right: 30px;
}
.wave {
  position: absolute;
  transform: translateY(calc(-50% - 0px)) scale(1, -1);
  left: 0;
  animation-duration: 4s;
  animation-iteration-count: infinite;
  animation-direction: normal;
  animation-timing-function: linear;
  width: 280%;
  height: 40%;
}

@keyframes wave1 {
  0% {
    left: 0%;
  }
  100% {
    left: -110%;
  }
}
@keyframes wave2 {
  0% {
    left: -15%;
  }
  100% {
    left: -125%;
  }
}
@keyframes wave3 {
  0% {
    left: -30%;
  }
  100% {
    left: -140%;
  }
}
@keyframes wave4 {
  0% {
    left: -45%;
  }
  100% {
    left: -155%;
  }
}
@keyframes wave0 {
  0% {
    left: -60%;
  }
  100% {
    left: -170%;
  }
}

.colorBox {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
}

.detailCard-enter-active,
.detailCard-leave-active {
  transition: opacity 0.5s;
}

.detailCard-enter,
.detailCard-leave-to {
  opacity: 0;
}

@media screen and (max-width: 375px) {
  #lists {
    grid-template-columns: 1fr 1fr !important;
  }
}
@media screen and (max-width: 767px) {
  #lists {
    grid-template-columns: 1fr 1fr 1fr;
  }
}

.v-dialog {
  -webkit-box-shadow: 0 0 0;
  box-shadow: 0 0 0;
  border-radius: 10px;
  border: 1px solid #c3c3c3;
}
</style>
