<template>
  <div>
    考勤 打卡
    <span>日期:</span>
    <el-date-picker v-model="value1" disabled type="date"></el-date-picker>
    <div>上午(自动)</div>
    <el-table :data="data" style="width: 100%" height="500">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="name" label="楼栋"></el-table-column>
      <el-table-column prop="name" label="工作内容"></el-table-column>
      <el-table-column prop="name" label="楼栋长"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "workTimeRecord",
  data() {
    return {
      url: "/api/work_api/WorkerApi",
      data: [],
      value1: new Date(),
    }
  },
  methods: {
    async init() {
      let data = {}
      let res = await this.$get2(this.url, 0, data)
      if (res.data.code != 1) {
        this.$message('服务器异常');
        return
      }
      this.data = res.data.data
    }
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>