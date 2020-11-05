<template>
  <h1 @click="openModal">追加する</h1>
</template>

<script>
export default {
  methods: {
    openModal() {
      console.log('emmitted');
      this.$emit('open-modal');
    },
  },
};
</script>
