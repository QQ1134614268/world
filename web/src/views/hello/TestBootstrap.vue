<template>
  <div>
  </div>
</template>


<style scoped>
/* 假设你使用了 webpack 并且安装了 bootstrap */
/* @import "~bootstrap/dist/css/bootstrap.min.css";  */
/* 或者直接链接 CDN，但这通常不是局部引入的方式 */
@import url('https://cdn.staticfile.net/twitter-bootstrap/5.1.1/css/bootstrap.min.css');
</style>
<script>
export default {
  name: 'Home',
  data() {
    return {
      webSite: 'world',
      msg: 'Hello world',
    }
  }
}
</script>
