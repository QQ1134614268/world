<template>
  <div>
    每日报表
    <el-table :data="data">
      <el-table-column prop="time" sortable label="工作时间"></el-table-column>
      <el-table-column prop="name" sortable label="姓名"></el-table-column>
      <el-table-column prop="area" sortable label="地点"></el-table-column>
      <el-table-column prop="content" sortable label="工作内容"></el-table-column>
      <el-table-column prop="hours" sortable label="时长"></el-table-column>
    </el-table>
    总工时--{{ total }}小时
  </div>
</template>

<script>
import {WorkTimeAnalyseApi_get_day_report} from "@/api/api";
import {get2} from "@/api/http";

export default {
  name: "workTimeReport",
  data() {
    return {
      data: [],
      total: 0
    }
  },
  methods: {
    async init() {
      let data = {
        name: this.name,
        dateType: this.dateType,
        date: this.date,
      }
      let result = await get2(WorkTimeAnalyseApi_get_day_report, 0, data);
      this.data = result.data.data

      this.total = this.data.map((x) => {
        return x.time
      }).reduce((a, b) => {
        return a + b
      })
    },
  },
  created() {
    this.init();
  },
}
</script>

<style scoped>

</style>