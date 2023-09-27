<template>
  <div id="app">
    <router-view class="view"/>
  </div>
</template>
<script>

export default {
  name: "App",
  // computed: {
  //   token() {
  //     return this.$store.state.token
  //   }
  // },
  // watch:{
  //   token: function (val, oldVal) {
  //
  //   }
  // }
}
</script>
<style>
#app {
  width: 100%;
  height: 100%;
  /*页面文字可复制*/
  -webkit-user-select: text;
}

.view {
  width: 100%;
  height: 100%;
}
</style>
