<template>
  <div id="app">
    <router-view/>
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
  /*页面文字可复制*/
  -webkit-user-select: text;
}
</style>
