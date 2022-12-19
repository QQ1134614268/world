<template>
  <div class="p_c_HolyGrail-body">
    <BoxRow class="header">
      <h2 class="title">真实之树</h2>
      <TreeUserIcon class="icon"></TreeUserIcon>
    </BoxRow>
    <div class="p_c_HolyGrail-body">
      <router-view/>
      <!--      <router-view  name="tree"/>-->
    </div>
    <div id="footer" class="p_c_box-flex_row-center">
      <a href="http://www.beian.miit.gov.cn" target="_blank" style="color: #e7e3e3">皖ICP备20002024号-1</a>
    </div>
  </div>
</template>

<script>
import TreeUserIcon from "@/components/TreeUserIcon";

export default {
  name: "treeHome",
  components: {
    TreeUserIcon
  },
}
</script>
<style scoped>

.header {
  justify-content: space-between;
  align-items: center;
}

.icon {
  width: 10rem;
}

.title {
  text-align: center;
  flex: 1;
}

#footer {
  text-align: center;
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
</style>
