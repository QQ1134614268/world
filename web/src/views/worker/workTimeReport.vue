<template>
  <div>
    每日报表
    <!--    todo 优化(数据量巨大),整理合并 发邮件 -->
    <el-table :data="data">
      <el-table-column prop="area" sortable label="地点"></el-table-column>
      <el-table-column prop="content" sortable label="工作内容"></el-table-column>
      <el-table-column prop="name" sortable label="人员"></el-table-column>
      <el-table-column prop="time" sortable label="工作时间"></el-table-column>
      <!--      todo 时间,总人数统计-->
      <!--      <el-table-column prop="value" label="时间(小时)"></el-table-column>-->
      <!--      <el-table-column prop="value" label="总人数"></el-table-column>-->
    </el-table>
    总工时--x 小时
  </div>
</template>

<script>
import {WorkTimeAnalyseApi_get_day_report} from "@/api/api";

export default {
  name: "workTimeReport",
  data() {
    return {data: []}
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