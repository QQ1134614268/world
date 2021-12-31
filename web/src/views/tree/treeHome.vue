<template>
  <div style="min-height: 100%">
    <div class="p_c_box-flex_row-center " style="height: 10rem">
      <div>真实之树</div>
    </div>
    <div id="body">
      <router-view/>
      <!--      <router-view  name="tree"/>-->
    </div>
    <div id="footer" class="p_c_box-flex_row-center">
      <a href="http://www.beian.miit.gov.cn" target="_blank" style="color: #e7e3e3">皖ICP备20002024号-1</a>
    </div>
  </div>
</template>

<script>

export default {
  name: "treeHome",
}
</script>
<style>

#header {
  display: flex;
  justify-content: space-around;
  height: 10%;
}

#body {
  min-height: 80%
}

#footer {
  text-align: center;
  height: 10%;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 1;
  }
  50.01% {
    opacity: 0;
  }
  /* 注意这里定义50.01%立刻透明度为０，可以设置闪烁效果 */
  100% {
    opacity: 0;
  }
}

.blink {
  animation: blink .75s linear infinite;
  /* 其它浏览器兼容性前缀 */
  -webkit-animation: blink .75s linear infinite;
  -moz-animation: blink .75s linear infinite;
  -ms-animation: blink .75s linear infinite;
  -o-animation: blink .75s linear infinite;
  color: #dd4814;
}
</style>
