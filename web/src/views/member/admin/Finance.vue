<template>
  <div>
    统计
    <div class="p_c_flexbox">
      <div>
        <el-date-picker v-model="dateRange" :value-format=DATE_FMT type="daterange" range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
        </el-date-picker>
      </div>
      <el-button type="primary" v-on:click="init">查询</el-button>
    </div>
    <div>
      <el-table :data="data" style="width: 100%">
        <el-table-column prop="name" label="姓名" width="180"></el-table-column>
        <el-table-column prop="days" label="工时(天)"></el-table-column>
        <el-table-column prop="money" label="成本"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import {WorkerApi, WorkTimeAnalyseApi_get_sum_time} from "@/api/api";
import {fmtDateY_M_D, querySearch} from "@/api/util";
import {DATE_FMT} from "@/api/config";

export default {
  name: "Finance",
  data() {
    return {
      name: '',
      dateRange: this.get_month_day(),
      data: [],
      DATE_FMT
    }
  },
  methods: {
    get_month_day() {
      let date = new Date(), y = date.getFullYear(), m = date.getMonth();
      return [fmtDateY_M_D(new Date(y, m, 1)), fmtDateY_M_D(new Date(y, m + 1, 0))];
    },
    async init() {
      let data = {
        name: this.name,
        startDate: this.dateRange && this.dateRange.length > 0 ? this.dateRange[0] : "",
        endDate: this.dateRange && this.dateRange.length > 1 ? this.dateRange[1] : "",
      }
      let result = await this.$get2(WorkTimeAnalyseApi_get_sum_time, 0, data);
      this.data = result.data.data
    },
    async querySearch(queryString, cb) {
      let data = {name: queryString}
      await querySearch(data, cb, WorkerApi)
    },
  },
  created() {
    this.init();
  },
}
</script>

<style scoped>

</style>