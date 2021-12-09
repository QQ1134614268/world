<template>
  <div>
    考勤打卡 ( 待开发todo 楼栋 工作内容 楼栋长 )
    <div>
      <span>日期:</span>
      <el-date-picker v-model="date" disabled type="date"></el-date-picker>
    </div>
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="name" :label="time">
        <template slot-scope="scope">
          <el-checkbox v-model="scope.row.flag" @change="change(scope.row)">标志</el-checkbox>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {WorkerApi, WorkerTimeApi} from "@/api/const";
import {getDateY_M_D} from "@/api/timeUtil";

export default {
  name: "workTimeRecord",
  data() {
    return {
      data: [],
      date: getDateY_M_D(),
      time: "",
      attr: ''
    }
  },
  methods: {
    async init() {
      let data = {}
      let res = await this.$get2(WorkerApi, 0, data)
      if (res.data.code != 1) {
        this.$message('服务器异常');
        return
      }
      this.data = res.data.data
    },
    async get() {
      let myDate = new Date();
      let myHour = myDate.getHours(); //获取当前小时数(0-23)
      if (myHour <= 12) {
        this.time = "上午"
        this.attr = "morning"
      } else if (12 < myHour && myHour <= 14) {
        this.time = "中午"
        this.attr = "noon"
      } else if (14 < myHour && myHour <= 18) {
        this.time = "下午"
        this.attr = "afternoon"
      } else if (18 < myHour && myHour <= 24) {
        this.time = "晚上"
        this.attr = "night"
      }
    },
    async change(row) {
      let attr = this.attr
      if (this.time == "上午") {
        attr = 'morning'
      }
      let data = {
        'worker_id': row.id,
        date: this.date
      }
      data[attr] = row.flag
      debugger
      let response = await this.$putJson2(WorkerTimeApi, 0, data)
    }
  },

  created() {
    this.init()
    this.get()
  },
}
</script>

<style scoped>

</style>