<template>
  <div>
    考勤打卡
    <div>
      <span>日期:</span>
      <el-date-picker v-model="date" value-format="yyyy-MM-dd" type="date"></el-date-picker>
      <el-select v-model="time" placeholder="请选择">
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
      </el-select>
    </div>
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="name" label="位置">
        <template slot-scope="scope">
          <el-select v-model="scope.row.area" placeholder="请选择">
            <el-option v-for="item in config1" :key="item.value" :label="item.code" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column prop="name" label="工作内容">
        <template slot-scope="scope">
          <el-select v-model="scope.row.content" placeholder="请选择">
            <el-option v-for="item in config2" :key="item.value" :label="item.code" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column label="签到">
        <template slot-scope="scope">
          <el-checkbox @change="change(scope.row)" v-model="scope.row.flag" :true-label="1"
                       :false-label="0"></el-checkbox>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {getDateY_M_D} from "@/api/timeUtil";
import {ConfigApi, WorkerApi, WorkerTimeApi} from "@/api/api";

export default {
  name: "workTimeRecord",
  data() {
    return {
      data: [],
      date: getDateY_M_D(),
      time: "",
      config1: [],
      config2: [],
      options: [
        {value: 'morning', label: '上午'},
        {value: 'noon', label: '中午'},
        {value: 'afternoon', label: '下午'},
        {value: 'night', label: '晚上'},
      ],
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
    async initArea() {
      let data = {"group_code": "BUILD"}
      let res = await this.$get2(ConfigApi, 0, data)
      this.config1 = res.data.data
    },
    async initWorkContent() {
      let data = {"group_code": "WORK_TYPE"}
      let res = await this.$get2(ConfigApi, 0, data)
      this.config2 = res.data.data
    },
    async get() {
      let myDate = new Date();
      let myHour = myDate.getHours(); //获取当前小时数(0-23)
      if (myHour <= 12) {
        this.time = "morning"
      } else if (12 < myHour && myHour <= 14) {
        this.time = "noon"
      } else if (14 < myHour && myHour <= 18) {
        this.time = "afternoon"
      } else if (18 < myHour && myHour <= 24) {
        this.time = "night"
      }
    },
    async change(row) {
      let data = {
        'worker_id': row.id,
        date: this.date,
        type: this.time,
        area: row.area,
        content: row.content,
        flag: row.flag,
      }
      let response = await this.$putJson2(WorkerTimeApi, 0, data)
    },
  },

  created() {
    this.init()
    this.get()
    this.initArea()
    this.initWorkContent()
  },
}
</script>

<style scoped>

</style>