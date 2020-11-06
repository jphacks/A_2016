<template>
  <div>
    <v-card class="dialog">
      <v-card-title class="headline grey lighten-2">{{
        item.item
      }}</v-card-title>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="secondary" @click="onClickDelete" small icon
          ><v-icon dark> mdi-delete </v-icon></v-btn
        >
        <v-btn color="secondary" text @click="change">変更</v-btn>
        <v-btn color="secondary" text @click="close">閉じる</v-btn>
      </v-card-actions>
    </v-card>
    <v-row justify="center">
      <v-dialog v-model="isOpenChange">
        <AddDialog
          @close-add-modal="closeChangeModal"
          :deviceIdFromURL="item.device_id"
          title="デバイスを変更"
        />
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import { deleteItem } from '../../toServer/main';
import AddDialog from './AddDialog';

export default {
  name: 'Detail',

  components: {
    AddDialog,
  },

  props: {
    item: {
      required: true,
      type: Object,
    },
  },

  data() {
    return {
      isOpenChange: false,
    };
  },

  methods: {
    close() {
      this.$emit('close-detail-modal');
    },

    change() {
      this.$emit('close-detail-modal');
      this.isOpenChange = true;
    },

    closeChangeModal() {
      this.isOpenChange = false;
    },

    async onClickDelete() {
      try {
        await deleteItem(this.item.device_id);
        this.close();
      } catch (err) {
        console.error(err);
      }
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
