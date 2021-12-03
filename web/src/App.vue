<template>
  <div id="app" style="min-height: 100%">
    <router-view/>
  </div>
</template>
<script>

export default {
  name: "App",
}
</script>
<style>
#app {
  margin: auto;
  max-width: 100rem;
  height: 100%;
  /*页面文字可复制*/
  -webkit-user-select: text;
}
</style>
