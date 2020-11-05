<template>
  <section>
    <AddDevice class="lists" />
    <div v-for="(list, i) in lists" :key="i">
      <Card :info="list" class="lists" />
    </div>
  </section>
</template>

<script>
import Card from './molecules/Card';
import AddDevice from './AddDevice';
import { hello } from '../toServer/main';

export default {
  name: 'List',

  components: {
    Card,
    AddDevice,
  },

  data() {
    return {
      lists: [],
    };
  },

  created() {
    const res = hello();
    this.lists = res;
  },
};
</script>

<style scoped>
.lists {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

@media screen and (max-width: 375px) {
}
</style>
