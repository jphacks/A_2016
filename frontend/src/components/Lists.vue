<template>
  <section>
    <section id="lists">
      <!-- <transition appear name="detailCard"> -->
      <Detail
        v-if="isOpenedDetail"
        @close-detail-modal="closeDetailModal"
        @open-change-modal="openChangeModal"
        :item="detailItem"
      />
      <!-- </transition> -->
      <Change
        v-if="isOpenedChange"
        :changeItemId="changeItem.device_id"
        @close-change-modal="closeChangeModal"
        @change-list="changeList"
      />
      <AddDialog
        id="Dialog"
        v-if="isOpenedAdd"
        @close-add-modal="closeAddModal"
        :deviceIdFromURL="deviceIdFromURL"
      />
      <section class="listCard addButton">
        <AddButton @open-add-modal="openAddModal" />
      </section>
      <div v-for="(list, i) in lists" :key="i" class="listCard">
        <div
          className="colorBox"
          v-bind:style="{
            height: list.percentage * 1.5 + 'px',
          }"
        ></div>
        <!-- // TODO:  listCardでstylingされてるのに、onclickは上半分でしか反応しない -->
        <Card :info="list" @open-detail-modal="openDetailModal" />
      </div>
    </section>
  </section>
</template>

<script>
import Card from './molecules/Card';
import AddDialog from './molecules/AddDialog';
import AddButton from './molecules/AddButton';
import Detail from '../components/molecules/Detail';
import Change from '../components/molecules/Change';

import { hello } from '../toServer/main';

export default {
  name: 'List',

  components: {
    Card,
    Detail,
    Change,
    AddDialog,
    AddButton,
  },

  data() {
    return {
      isOpenedDetail: false,
      isOpenedChange: false,
      isOpenedAdd: false,
      lists: [],
      detailItem: {},
      changeItem: {},
      deviceIdFromURL: '',
      query: null,
    };
  },

  async mounted() {
    this.query = new URLSearchParams(location.search.slice(1));
    this.deviceIdFromURL = this.query?.get('d');
    this.lists = await hello();
    if (this.deviceIdFromURL) {
      this.isOpenedAdd = true;
    }
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

    closeDetailModal() {
      this.isOpenedDetail = false;
    },

    openChangeModal(item) {
      this.isOpenedChange = true;
      this.changeItem = item;
    },

    closeChangeModal() {
      this.isOpenedChange = false;
    },

    openAddModal() {
      this.isOpenedDetail = false;
      this.isOpenedChange = false;
      this.isOpenedAdd = true;
    },

    closeAddModal(item) {
      this.isOpenedAdd = false;
      this.add(item);
      this.deviceIdFromURL = '';
      this.query?.delete('d');
      history.pushState('', '', '?' + this.query?.toString());
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
  border: 1px solid #111;
  border-radius: 10px;
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
    border-radius: 10px;
    border: 1px solid #111;
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
  border: 1px dashed black !important;
  h1 {
    border: none !important;
  }
}

.colorBox {
  background-color: pink;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;
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
