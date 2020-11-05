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
      <Change v-if="isOpenedChange" :changeItemId="changeItem.device_id" />
      <AddDevice class="listCard" @add="add" />
      <div v-for="(list, i) in lists" :key="i" class="listCard">
        <!-- // TODO:  listCardでstylingされてるのに、onclickは上半分でしか反応しない -->
        <Card :info="list" @open-detail-modal="openDetailModal" />
      </div>
    </section>
  </section>
</template>

<script>
import Card from './molecules/Card';
import AddDevice from './AddDevice';
import Detail from '../components/molecules/Detail';
import { hello } from '../toServer/main';

export default {
  name: 'List',

  components: {
    Card,
    AddDevice,
    Detail,
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
  },
};
</script>

<style scoped>
#lists {
  /* display: block; */
  width: 80%;
  background-color: pink;
  margin: 0 auto;
  padding-top: 10px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
}

.listCard {
  background-color: whitesmoke;
  margin: 10px auto;
  width: 80%;
  height: 150px;
  border-radius: 12px;
  border: 1px solid #111;
  cursor: pointer;
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
    grid-template-columns: 1fr 1fr 1fr;
    width: 95%;
  }
  .listCard {
    width: 90%;
    height: 110px;
  }
}
</style>
