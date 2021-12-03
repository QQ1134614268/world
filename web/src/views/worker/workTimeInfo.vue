<template>
  <div>
    <div>
      批量考勤记录--搜索--编辑
    </div>
    <el-table :data="data" style="width: 100%" height="500">
      <el-table-column prop="date" label="日期"></el-table-column>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="morning" label="上午"></el-table-column>
      <el-table-column prop="noon" label="中午"></el-table-column>
      <el-table-column prop="afternoon" label="下午"></el-table-column>
      <el-table-column prop="night" label="晚上"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "time",
  data() {
    return {
      url: '/api/work_api/WorkerTimeApi',
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