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
        <span>时间:</span>
        <el-select v-model="dateType" placeholder="请选择">
          <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
          </el-option>
        </el-select>
        <el-date-picker
            v-model="date"
            :type="dateType"
            value-format="yyyy-MM-dd"
            placeholder="选择时间">
        </el-date-picker>
      </div>
      <el-button type="primary" v-on:click="init">查询</el-button>
    </div>
    <div>
      <el-table :data="data" style="width: 100%">
        <el-table-column prop="name" label="姓名" width="180"></el-table-column>
        <el-table-column prop="hours" label="工时"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import {WorkerApi, WorkTimeAnalyseApi_get_sum_time} from "@/api/const";
import {getDateY_M_D} from "@/api/timeUtil";

export default {
  name: "workTimeAnalyse",
  data() {
    return {
      name: '',
      date: getDateY_M_D(),
      dateType: 'date',
      options: [
        {value: 'year', label: '年'},
        {value: 'month', label: '月'},
        {value: 'date', label: '日'},
      ],
      data: []
    }
  },
  methods: {
    async init() {
      let data = {
        name: this.name,
        dateType: this.dateType,
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