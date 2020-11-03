<template>
  <section id="Card">
    <div>
      <h1 class="percentage">{{ info.percentage }}</h1>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Card',

  props: {
    info: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
#Card {
  width: 200px;
  height: 300px;
  border: 2px solid #111;
}
.percentage {
  margin-top: 40px;
}
</style>
