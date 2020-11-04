<template>
  <section>
    <div id="Card" @click="openModal">
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

  methods: {
    openModal() {
      this.$emit('open-modal');
    },
  },
};
</script>

<style scoped>
/* .percentage {
  margin-top: 40px;
} */
#Card {
  /* display: block;
  background-color: blue;
  width: 100%;
  padding-top: 100%; */
}
</style>
