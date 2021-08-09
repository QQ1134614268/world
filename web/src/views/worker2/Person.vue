<template>
  <div>
    <div>
      <el-select v-model="name" clearable placeholder="请选择">
        <el-option
            v-for="item in nameList"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
      </el-select>
      <el-select v-model="year" clearable placeholder="请选择" v-on:change="initDayList">
        <el-option
            v-for="item in yearList"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
      </el-select>
      <el-select v-model="month" clearable placeholder="请选择" v-on:change="initDayList">
        <el-option
            v-for="item in monthList"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
      </el-select>
      <el-select v-model="day" clearable placeholder="请选择">
        <el-option
            v-for="item in dayList"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
      </el-select>
      <el-button type="primary" v-on:click="get_person">查询</el-button>
    </div>
    <div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="date" label="日期" width="180"></el-table-column>
        <el-table-column prop="hours" label="工时"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Person",
  data() {
    return {
      name: "",
      nameList: [],
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
    //  循环年
    //  可以给定自己想要年份的范围，我这里给的是现在年份的后十年
    async initNameList() {
      let result = await this.$get('/api/work_api2/get_worker');
      for (let value of result.data.data) {
        this.nameList.push({
          "label": value,
          "value": value
        })
      }
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
    async get_person() {
      let data = {
        name: this.name,
        year: this.year,
        month: this.month,
        day: this.day,
      }
      let result = await this.$get('/api/work_api2/get_person', data);
      this.tableData = result.data.data
    }
  },
  created() {
    this.initNameList();
    this.initYearList();
    this.initMonthList();
    this.initDayList();
  },
}
</script>

<style scoped>

</style>