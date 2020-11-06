<template>
  <v-card class="dialog">
    <v-card-title class="headline grey lighten-2">{{ item.item }}</v-card-title>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary" @click="dialog = false"
        ><v-icon dark> mdi-delete </v-icon></v-btn
      >
      <v-btn color="primary" text @click="change">変更</v-btn>
      <v-btn color="primary" text @click="close">閉じる</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Detail',

  props: {
    item: {
      required: true,
      type: Object,
    },
  },

  methods: {
    close() {
      this.$emit('close-detail-modal');
    },

    change() {
      this.$emit('close-detail-modal');
      this.$emit('open-change-modal', this.item);
    },
  },
};
</script>

<style scoped>
.dialog {
  z-index: 100000;
  border: 1px solid #111;
  border-radius: 10px;
}
</style>
