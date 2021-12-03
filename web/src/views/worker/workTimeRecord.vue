<template>
  <div>
    todo 选择人名,楼道,内容(内容1,2,3), 配合单独编辑
    日期:
    <el-date-picker
        v-model="date"
        type="date"
        format="yyyy 年 MM 月 dd 日"
        value-format="yyyy-MM-dd"
        placeholder="选择日期">
    </el-date-picker>
    <div>上午(自动)</div>
    <el-table :data="data" style="width: 100%" height="500">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="name" label="楼栋">

      </el-table-column>
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