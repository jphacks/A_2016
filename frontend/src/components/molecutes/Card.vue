<template>
  <section id="Card">
    <div>
      <h1 class="percentage">{{ info.percentage }}</h1>
    </div>
  </section>
</template>

<script>
export default {
  name: "Card",

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
  border: 2px solid #111;
  border-radius: 8px;
  background-color: blue;
  margin: 0 auto;
}
.percentage {
  margin-top: 40px;
}
</style>
