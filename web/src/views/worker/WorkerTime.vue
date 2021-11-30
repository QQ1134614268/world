<template>
  <div>
    <div class="block">
      <el-date-picker
          v-model="date"
          type="date"
          format="yyyy 年 MM 月 dd 日"
          value-format="yyyy-MM-dd"
          placeholder="选择日期"
          @change="init">
      </el-date-picker>
      <el-button @click="save">保存</el-button>
      <el-table stripe :data="workerTime" style="width: 100%" height="400">
        <el-table-column label="姓名" prop="name"></el-table-column>
        <el-table-column label="上午" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.morning" placeholder="请输入内容"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="中午" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.noon" placeholder="请输入内容"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="下午" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.afternoon" type="number" placeholder="请输入内容"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="晚上" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.night" placeholder="请输入内容"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="备注" >
          <template slot-scope="scope">
            <el-input v-model="scope.row.note" placeholder="请输入内容"></el-input>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "worker",
  data() {
    return {
      month: null,
      date: new Date().getFullYear() + "-" + (new Date().getMonth() + 1) + "-" + new Date().getDate(),
      workerTime: [],
      d_date: ""
    }
  },
  methods: {
    async init() {
      let url = '/api/work_api/WorkerTimeApi';
      let data = {
        date: this.date
      }
      let response = await this.$get(url, data);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.workerTime = response.data.data
    },

    async save() {
      let url = '/api/work_api/WorkerTimeApi';
      let data = []
      for (let i = 0; i < this.workerTime.length; i++) {
        let value = this.workerTime[i]
        data.push({
          id: value.id,
          worker_id: value.worker_id,
          morning: value.morning,
          noon: value.noon,
          afternoon: value.afternoon,
          night: value.night,
          note: value.note,
          date: this.date
        })
      }
      let response = await this.$putJson(url, data);
      if (response.data.code != 1) {
        this.$message('操作失败');
      } else {
        this.$message('操作成功');
      }
      await this.init()
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>