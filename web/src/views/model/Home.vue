<template>
  <div>
    <div class="title">
      title--希洛之书
    </div>
    <div v-for="(item,k)  in tableList">
      <div>
        <span>{{ k }}</span>
        .
        <span>
        {{ item }}
         </span>
      </div>
      1. 论点1
      1.1 论证
      1.2 推理现象
      1.2.1 图,文字,故事,短视频

      # tag 继承 --协议实现
      # es 辅助建立 知识图谱
    </div>
    <div>
      2. xxx
    </div>
    <div>
      3. xxx
    </div>
  </div>

</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      tableList: []
    }
  },
}
</script>

<style scoped>

</style>