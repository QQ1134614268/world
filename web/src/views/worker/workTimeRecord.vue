<template>
  <div>
    考勤打卡
    <div>
      <span>日期:</span>
      <el-date-picker v-model="date" :value-format=DATE_FMT type="date"></el-date-picker>
      <el-select v-model="time" placeholder="请选择" @change="init">
        <el-option v-for="(item,index) in options" :label="item.label" :value="item.value" :key="index"></el-option>
      </el-select>
    </div>
    <el-table :data="data" style="width: 100%">
      <!--      todo 设计 一天的( 优化), 取消点击flag(触发保存?),  测试
                    api 优化(连表的数据,单独接口)
                        log记录修改
                        当天数据与上一个有数据的(每次点击获取? 根据时间button触发最大日期),
                        微信扫码,记录工作内容
      -->
      <el-table-column key="name" prop="name" label="姓名"></el-table-column>
      <el-table-column key="morning_area" label="位置" v-if='this.time=="morning"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.morning_area" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config1" :key="index" :label="item.code" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="morning_content" label="工作内容" v-if='this.time=="morning"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.morning_content" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config2" :label="item.code" :value="item.value" :key="index"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="morning" label="工作时长(小时)" v-if='this.time=="morning"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.morning" filterable allow-create default-first-option placeholder="请选择"
                     @change="change(scope.row)">
            <el-option v-for="item in time1" :key="item.label" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="noon_area" label="位置" v-if='this.time=="noon"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.noon_area" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config1" :key="index" :label="item.code" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="noon_content" label="工作内容" v-if='this.time=="noon"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.noon_content" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config2" :label="item.code" :value="item.value" :key="index"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="noon" label="工作时长(小时)" v-if='this.time=="noon"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.noon" filterable allow-create default-first-option placeholder="请选择"
                     @change="change(scope.row)">
            <el-option v-for="item in time1" :key="item.label" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="afternoon_area" label="位置" v-if='this.time=="afternoon"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.afternoon_area" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config1" :key="index" :label="item.code" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="afternoon_content" label="工作内容" v-if='this.time=="afternoon"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.afternoon_content" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config2" :label="item.code" :value="item.value" :key="index"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="afternoon" label="工作时长(小时)" v-if='this.time=="afternoon"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.afternoon" filterable allow-create default-first-option placeholder="请选择"
                     @change="change(scope.row)">
            <el-option v-for="item in time1" :key="item.label" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="afternoon" label="位置" v-if='this.time=="night"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.night_area" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config1" :key="index" :label="item.code" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="night_content" label="工作内容" v-if='this.time=="night"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.night_content" placeholder="请选择" @change="change(scope.row)">
            <el-option v-for="(item,index) in config2" :label="item.code" :value="item.value" :key="index"></el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column key="night" label="工作时长(小时)" v-if='this.time=="night"'>
        <template slot-scope="scope">
          <el-select v-model="scope.row.night" filterable allow-create default-first-option placeholder="请选择"
                     @change="change(scope.row)">
            <el-option v-for="item in time1" :key="item.label" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {ConfigApi, WorkerTimeApi} from "@/api/api";
import {getDateY_M_D} from "@/api/util";
import {DATE_FMT} from "@/api/config";
import {get2, putJson2} from "@/api/http";

export default {
  name: "workTimeRecord",
  data() {
    return {
      data: [],
      date: getDateY_M_D(),
      DATE_FMT,
      time: "",
      config1: [],
      config2: [],
      options: [
        {value: 'morning', label: '上午'},
        {value: 'noon', label: '中午'},
        {value: 'afternoon', label: '下午'},
        {value: 'night', label: '晚上'},
      ],
      time1: [
        {
          value: '4.5',
          label: '4.5'
        },
        {
          value: '2',
          label: '2'
        },
        {
          value: '0',
          label: '0'
        },
      ],
      time2: [
        {
          value: '2',
          label: '2'
        },
        {
          value: '4.5',
          label: '4.5'
        },
        {
          value: '0',
          label: '0'
        },
      ]
    }
  },
  methods: {
    async init() {
      let data = {
        date: this.date
      }
      let res = await get2(WorkerTimeApi, 0, data)
      if (res.data.code != 1) {
        this.$message.error('服务器异常');
        return
      }
      this.data = res.data.data
    },
    async initArea() {
      let data = {"group_code": "BUILD"}
      let res = await get2(ConfigApi, 0, data)
      this.config1 = res.data.data
    },
    async initWorkContent() {
      let data = {"group_code": "WORK_TYPE"}
      let res = await get2(ConfigApi, 0, data)
      this.config2 = res.data.data
    },
    async getTime() {
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
      row.date = this.date
      let response = await putJson2(WorkerTimeApi, 0, row)
    },
  },

  created() {
    this.init()
    this.getTime()
    this.initArea()
    this.initWorkContent()
  },
}
</script>

<style scoped>

</style>