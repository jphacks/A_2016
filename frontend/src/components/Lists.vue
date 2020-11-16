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
                ? 170
                : 150 - (item && item.percentage * 1.5)
            }px;animation-name:wave${
              Math.abs(
                item && item.item.split('').reduce((a, b) => {
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
              item && item.percentage >= 100
                ? 150
                : item && item.percentage * 1.5 - 10
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
  </section>
</template>

<script>
import Card from './molecules/Card';
import Detail from '../components/molecules/Detail';

import { devicesStore } from '../store/devices';

export default {
  name: 'List',

  components: {
    Card,
    Detail,
  },

  data() {
    return {
      isOpenedDetail: false,
      detailItem: {},
      changeItem: {},
      loading: true,
    };
  },

  created() {
    this.fetchDevices();
    setInterval(() => {
      this.fetchDevices();
    }, 3000);
  },

  mounted() {
    this.loading = true;
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
            device_id: device.device_id,
            item: device.item,
            weight: device.weight,
            percentage: percentage,
            color: device.color,
            expiration_date: device.expiration_date,
          };
        });
    },
  },

  methods: {
    openDetailModal(item) {
      this.isOpenedDetail = true;
      this.detailItem = item;
    },

    async closeDetailModal() {
      this.isOpenedDetail = false;
      this.fetchDevices();
    },

    fetchDevices() {
      devicesStore.dispatch('fetchDevices').then(() => {
        this.loading = false;
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
  width: 80%;
  max-width: 950px;
  margin: 0 auto;
  padding-top: 10px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  .listCard {
    background-color: white;
    margin: 10px auto;
    width: 80%;
    max-width: 150px;
    max-height: 150px;
    height: 150px;
    overflow: hidden;
    box-shadow: 0 0 0 1px #c3c3c3;
    border-radius: 9px;
    cursor: pointer;
    position: relative;
    // mix-blend-mode: hue;
    .percentage {
      position: absolute;
      top: 3px;
      left: 6px;
      mix-blend-mode: difference;
    }
    .name {
      position: absolute;
      bottom: 3px;
      left: 6px;
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
.wave {
  position: absolute;
  transform: translateY(calc(-50% - 0px)) scale(1, -1);
  left: 0;
  overflow-y: hidden;
  // animation: wave;
  animation-duration: 4s;
  animation-name: wave2;
  animation-iteration-count: infinite;
  animation-direction: normal;
  animation-timing-function: linear;
  width: 280%;
  height: 40%;
  // mix-blend-mode: hue;
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
  .listCard {
    width: 90%;
    height: 150px;
    max-width: 110px;
  }
}
@media screen and (max-width: 767px) {
  #lists {
    grid-template-columns: 1fr 1fr 1fr;
    width: 95%;
  }
  .listCard {
    width: 90%;
    height: 150px;
    max-width: 110px;
  }
}

.v-dialog {
  -webkit-box-shadow: 0 0 0;
  box-shadow: 0 0 0;
  border-radius: 10px;
  border: 1px solid #c3c3c3;
}
</style>
