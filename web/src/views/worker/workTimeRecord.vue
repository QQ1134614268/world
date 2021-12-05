<template>
  <div>
    考勤打卡 ( 待开发todo 楼栋 工作内容 楼栋长 )
    <div>
      <span>日期:</span>
      <el-date-picker v-model="value1" disabled type="date"></el-date-picker>
    </div>
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="name" :label="time">
        <template slot-scope="scope">
          <el-radio v-model="scope.row.flag" @change="change" label="2" border size="medium">标志(上下午 todo)</el-radio>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "workTimeRecord",
  data() {
    return {
      url: "/api/work_api/WorkerApi",
      data: [],
      value1: new Date(),
      time: ""
    }
  },
  methods: {
    async init() {
      let data = {}
      let res = await this.$get2(this.url, 0, data)
      if (res.data.code != 1) {
        this.$message('服务器异常');
        return
      }
      this.data = res.data.data
    },
    async get() {
      //todo  抽取 后端配置
      let myDate = new Date();
      let myHour = myDate.getHours(); //获取当前小时数(0-23)
      if (myHour <= 12) {
        this.time = "上午"
      } else if (12 < myHour && myHour <= 14) {
        this.time = "中午"
      } else if (14 < myHour && myHour <= 18) {
        this.time = "下午"
      } else if (18 < myHour && myHour <= 24) {
        this.time = "晚上"
      }
    },
    change() {
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