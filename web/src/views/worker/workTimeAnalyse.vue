<template>
  <div>
    统计 ( 月度,成本 个人维度,姓名模糊搜索 )
    <div class="p_c_flexbox">
      <div class="col-3">
        <span>姓名:</span>
        <el-input class="col-6" v-model="name"></el-input>
      </div>
      <div>
        <span>时间(年-月-日):</span>
        <el-cascader
            v-model="value"
            :options="options"
            @change="handleChange"></el-cascader>
      </div>
      <el-button type="primary" v-on:click="init">查询</el-button>
    </div>
    <div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="name" label="姓名" width="180"></el-table-column>
        <el-table-column prop="hours" label="工时"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Time",
  data() {
    return {
      year: 2020,
      month: 7,
      day: 1,
      yearList: [],
      monthList: [],
      dayList: [],
      tableData: [],
    }
  },
  methods: {
    async init() {
    },

    handleChange() {
    },
    //  循环年
    //  可以给定自己想要年份的范围，我这里给的是现在年份的后十年
    initYearList() {
      let year = new Date().getFullYear()
      for (let i = 5; i >= 0; i--) {
        this.yearList.push({
          "label": year - i,
          "value": year - i
        })
      }
    },
    //循环月
    //一年只有12个月  没有特别的
    initMonthList() {
      for (let i = 1; i <= 12; i++) {
        this.monthList.push({
          "label": i,
          "value": i
        })
      }
    },
    initDayList() {
      this.dayList = []
      let day = new Date(this.year, this.month, 0).getDate()
      for (let i = 1; i <= day; i++) {
        this.dayList.push({
          "label": i,
          "value": i
        })
      }
    },
    async getDataByDate() {
      let data = {
        year: this.year,
        month: this.month,
        day: this.day,
      }
      let result = await this.$get('/api/work_api2/get_date', data);
      this.tableData = result.data.data
    }
  },
  created() {
    this.initYearList();
    this.initMonthList();
    this.initDayList();
  },
}
</script>

<style scoped>

</style>