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
        v-for="(list, i) in devices"
        :key="i"
        class="listCard"
        @click="openDetailModal(list)"
      >
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

import { devicesStore } from '../store/devices';

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
      detailItem: {},
      changeItem: {},
    };
  },

  async created() {
    this.fetchDevices();
  },

  computed: {
    devices() {
      return devicesStore.state.devices;
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

    async fetchDevices() {
      await devicesStore.dispatch('fetchDevices');
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
