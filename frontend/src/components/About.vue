<template>
  <v-card class="about">
    <p class="head">残量を可視化できる!</p>
    <v-spacer></v-spacer>
    <img :src="image_src" />
    <v-spacer></v-spacer>
    <v-card-title>arcana について</v-card-title>
    <p>
      -
      このアプリケーションでは、デバイスに載せる商品の詳細を登録することで、その商品の残量を可視化するものです。
    </p>
    <v-card-title>特徴</v-card-title>
    <p>
      -
      牛乳など冷蔵庫にて保管するものをはじめ、シャンプーや消毒液などを登録させることができます。
    </p>
    <p>- その商品の表示の色や消費期限を登録することができます。</p>
    <p>
      -
      商品を予め登録しておくことで、残量が少なくなったら「購入する」ボタンが出現し、その商品を購入するウェブサイトに遷移します。
    </p>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      image_src: require('../../../images/arcana_logo.png'),
    };
  },
};
</script>

<style scoped lang="scss">
.head {
  text-align: center;
}
.about {
  margin: 0;
  padding: 20px;
  text-align: left;
  img {
    width: 70%;
    max-width: 250px;
    display: block;
    margin: 20px auto;
  }
}
.v-card__title {
  font-weight: bold !important;
  padding: 10px 0 !important;
}
</style>
