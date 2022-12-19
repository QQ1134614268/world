<template>
  <div>
    反馈,回复反馈,项目组
    <el-input v-model="content">
    </el-input>
  </div>
</template>

<script>
export default {
  name: "FeedBack",
  data() {
    return {
      content: '优化',
    }
  },
  methods: {
    async save() {
      let url = ""
      let data = {}
      await this.post(url, 0, data)
    }
  }

}
</script>

<style scoped>

</style>