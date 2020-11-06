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
        >
        <div
          class="colorBox"
          :style="`height: ${item && item.percentage * 1.5}px backgroundColor:${
            item ? (item.color ? item.color : gold) : gold
          }`"
        >
          <!-- <div
          class="colorBox"
          :style="`height: ${item && item.percentage * 1.5}px`"
        > -->
          {{ 's ' }}
          <!-- <svg
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            version="1.1"
            viewBox="0 0 100 100"
            preserveAspectRatio="none"
            id="svg-bg"
          >
            <path
              d="M0,0 v50 q10,10 20,0 t20,0 t20,0 t20,0 t20,0 v-50 Z"
              fill="#3eba90"
            ></path>
          </svg> -->
        </div>
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
    console.log(this.listsß);
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

.colorBox {
  // background-color: blue;
  position: absolute;
  top: 0;
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
