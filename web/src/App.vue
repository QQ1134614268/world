<template>
  <div id="app" class="d-flex flex-column min-vh-100 ">
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

.view {
  width: 100%;
  height: 100%;
}
</style>
