<template>
  <div>
    报表(待实现 todo)
    <el-table>
      <el-table-column prop="value" label="地点"></el-table-column>
      <el-table-column prop="value" label="工作内容"></el-table-column>
      <el-table-column prop="value" label="人员"></el-table-column>
      <el-table-column prop="value" label="总人数"></el-table-column>
      <el-table-column prop="value" label="工作时间"></el-table-column>
      <el-table-column prop="value" label="时间(小时)"></el-table-column>
      <el-table-column prop="value" label="总人数"></el-table-column>
    </el-table>
    总工时--
  </div>
</template>

<script>
import {WorkTimeAnalyseApi_get_day_report} from "@/api/api";

export default {
  name: "workTimeReport",
  data() {
    return {}
  },
  methods: {
    async init() {
      let data = {
        name: this.name,
        dateType: this.dateType,
        date: this.date,
      }
      let result = await this.$get2(WorkTimeAnalyseApi_get_day_report, 0, data);
      this.data = result.data.data
    },
  },
  created() {
    this.init();
  },
}
</script>

<style scoped>

</style>