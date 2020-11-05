<template>
  <section>
    <section id="lists">
      <Detail v-if="isOpened" @close-modal="closeModal" />
      <AddDevice class="listCard" @add="add" />
      <div v-for="(list, i) in lists" :key="i" class="listCard">
        <Card :info="list" @open-modal="openModal" />
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
      isOpened: false,
      lists: [],
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

    openModal() {
      this.isOpened = true;
    },

    closeModal() {
      this.isOpened = false;
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
  border-radius: 7px;
  border: 1px solid #111;
}

@media screen and (max-width: 375px) {
  #lists {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
</style>
