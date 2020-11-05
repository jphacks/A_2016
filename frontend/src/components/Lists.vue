<template>
  <section>
    <Detail v-if="isOpened" />
    <section id="lists">
      <AddDevice class="listCard" />
      <div v-for="(list, i) in lists" :key="i" class="listCard">
        <Card :info="list" />
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
      lists: [{ percentage: 52 }, { percentage: 52 }, { percentage: 52 }],
    };
  },

  created() {
    const res = hello();
    this.lists = res;
  },
};
</script>

<style scoped>
#lists {
  /* display: block; */
  width: 80%;
  background-color: pink;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
}

.listCard {
  background-color: green;
  width: 90%;
  border-radius: 7px;
  border: 1px solid #111;
  margin: 0 auto;
}

@media screen and (max-width: 375px) {
  #lists {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
</style>
