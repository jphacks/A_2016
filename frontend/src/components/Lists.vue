<template>
  <section>
    <div v-for="(list, i) in lists" :key="i">
      <Card :info="list" class="lists" />
    </div>
  </section>
</template>

<script>
import Card from './molecutes/Card';

export default {
  name: 'List',

  components: {
    Card,
  },

  data() {
    return {
      lists: [
        {
          device_id: '5CDCD567',
          item: '牛乳',
          weight: 500,
          percentage: 52,
        },
        {
          device_id: '5CDCD568',
          item: 'コーヒー牛乳',
          weight: 500,
          percentage: 52,
        },
      ],
    };
  },
};
</script>

<style scoped>
.lists {
  float: left;
  margin: 10px;
}
</style>
