<template>
  <div>
    <div class="p_c_flexbox">
      <div class="col-3">
        <span>姓名:</span>
        <el-autocomplete class="inline-input" v-model="name" placeholder="请输入内容" :fetch-suggestions="querySearch"
                         :trigger-on-focus="false">
        </el-autocomplete>
      </div>
      <div class="col-6">
        <span>日期:</span>
        <el-date-picker :value-format=DATE_FMT v-model="dateRange"
                        type="daterange" range-separator="至 " start-placeholder="开始日期" end-placeholder="结束日期">
        </el-date-picker>
      </div>
      <div class="col-3">
        <el-button type="primary" @click="init">搜索</el-button>
      </div>
    </div>
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="date" label="日期"></el-table-column>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="morning" label="上午"></el-table-column>
      <el-table-column prop="noon" label="中午"></el-table-column>
      <el-table-column prop="afternoon" label="下午"></el-table-column>
      <el-table-column prop="night" label="晚上"></el-table-column>
      <el-table-column label="合计">
        <template slot-scope="scope">
          {{ ((scope.row.morning + scope.row.noon + scope.row.afternoon + scope.row.night) / 9).toFixed(2) }}
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {WorkerApi, WorkerTimeApi} from "@/api/api";
import {getDateY_M_D} from "@/api/util";
import {DATE_FMT} from "@/api/config";
import {get2} from "@/api/http";

export default {
  name: "workTimeInfo",
  data() {
    return {
      name: "",
      dateRange: [getDateY_M_D(), getDateY_M_D()],
      data: [],
      DATE_FMT
    }
  },
  methods: {
    async init() {
      let data = {
        startDate: this.dateRange && this.dateRange.length > 0 ? this.dateRange[0] : "",
        endDate: this.dateRange && this.dateRange.length > 1 ? this.dateRange[1] : "",
        name: this.name
      }
      let res = await get2(WorkerTimeApi, 0, data)

      if (res.data.code != 1) {
        this.$message.error('服务器异常');
        return
      }
      this.data = res.data.data
    },
    async querySearch(queryString, cb) {
      let data = {name: queryString}
      let res = await get2(WorkerApi, 0, data)
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
    this.init()
  },
}
</script>

<style scoped>

</style>