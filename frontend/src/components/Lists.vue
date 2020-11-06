<template>
  <section>
    <section id="lists">
      <Change
        v-if="isOpenedChange"
        :changeItemId="changeItem.device_id"
        @close-change-modal="closeChangeModal"
        @change-list="changeList"
      />
      <div
        v-for="(list, i) in lists"
        :key="i"
        class="listCard"
        @click="openDetailModal(list)"
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
            list && list.percentage == 0
              ? 170
              : 150 - (list && list.percentage * 1.5)
          }px; `"
        >
          <path
            d="M0,0 v50 q10,10 20,0 t20,0 t20,0 t20,0 t20,0 v-50 Z"
            :fill="`${list && list.color ? list.color : whitesmoke}`"
          ></path>
        </svg>
        <div
          class="colorBox"
          :style="`height: ${
            list && list.percentage >= 100
              ? 150
              : list && list.percentage * 1.5 - 10
          }px;backgroundColor:${list && list.color ? list.color : '#efebe9'}; `"
        ></div>

        <Card :info="list" />
      </div>
      <v-row justify="center">
        <v-dialog v-model="isOpenedDetail" persistent max-width="290">
          <Detail
            @close-detail-modal="closeDetailModal"
            @open-change-modal="openChangeModal"
            :item="detailItem"
          />
        </v-dialog>
      </v-row>
    </section>
  </section>
</template>

<script>
import Card from './molecules/Card';
import Detail from '../components/molecules/Detail';
import Change from '../components/molecules/Change';

import { hello } from '../toServer/main';

export default {
  name: 'List',

  components: {
    Card,
    Detail,
    Change,
  },

  data() {
    return {
      isOpenedDetail: false,
      isOpenedChange: false,
      lists: [],
      detailItem: {},
      changeItem: {},
    };
  },

  async mounted() {
    this.lists = await hello();
    console.log(this.lists);
  },

  methods: {
    add(res) {
      console.log(res, 'aaa');
      this.lists.push(res);
    },
    openDetailModal(item) {
      this.isOpenedDetail = true;
      this.detailItem = item;
    },

    async closeDetailModal() {
      this.isOpenedDetail = false;
      this.lists = await hello();
    },

    openChangeModal(item) {
      this.isOpenedChange = true;
      this.changeItem = item;
    },

    closeChangeModal() {
      this.isOpenedChange = false;
    },

    changeList(item) {
      // Todo: 用途を変更したらその時点で画面の物も変更できるようにする
      console.log(item);
    },
  },
};
</script>

<style lang="scss">
#Dialog {
  z-index: 100000;
  width: 80%;
  height: 500px;
  // border: 1px solid #111;
  border-radius: 10px;
  display: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px;
}

#lists {
  /* display: block; */
  width: 80%;
  /* background-color: pink; */
  max-width: 950px;
  margin: 0 auto;
  padding-top: 10px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  .listCard {
    background-color: whitesmoke;
    margin: 10px auto;
    width: 80%;
    max-width: 150px;
    max-height: 150px;
    height: 150px;
    overflow-y: hidden;
    border: 1px solid #c3c3c3;
    cursor: pointer;
    position: relative;
    .percentage {
      position: absolute;
      top: 5px;
      left: 10px;
    }
    .name {
      position: absolute;
      bottom: 5px;
      left: 10px;
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
  animation: wave 5s infinite normal linear;
  width: 200%;
  height: 100%;
}
@keyframes wave {
  0% {
    left: 0%;
  }
  100% {
    left: -80%;
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
    height: 95px !important;
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
    height: 110px;
    max-width: 110px;
  }
}
</style>
