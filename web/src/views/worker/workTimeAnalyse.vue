<template>
  <div>
    统计
    <div class="p_c_flexbox">
      <div class="col-3">
        <span>姓名:</span>
        <el-autocomplete class="inline-input" v-model="name" placeholder="请输入内容" :fetch-suggestions="querySearch"
                         :trigger-on-focus="false">
        </el-autocomplete>
      </div>
      <div>
        <el-date-picker
            v-model="date"
            value-format="yyyy-MM-dd"
            type="daterange"
            range-separator="至"
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
import {fmtDateY_M_D} from "@/api/timeUtil";

export default {
  name: "workTimeAnalyse",
  data() {
    return {
      name: '',
      date: this.get_month_day(),
      data: []
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
        date: this.date,
      }
      let result = await this.$get2(WorkTimeAnalyseApi_get_sum_time, 0, data);
      this.data = result.data.data
    },
    async querySearch(queryString, cb) {
      let data = {name: queryString}
      let res = await this.$get2(WorkerApi, 0, data)
      let suggest = []
      for (let i = 0; i < res.data.data.length; i++) {
        suggest.push({
          value: res.data.data[i].name
        })
      }
      cb(suggest)
    },
  },
  created() {
    this.init();
  },
}
</script>

<style scoped>

</style>