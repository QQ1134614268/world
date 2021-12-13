<template>
  <div>
    <div class="p_c_flexbox">
      <div class="col-3">
        <span>姓名:</span>
        <el-autocomplete class="inline-input" v-model="name" placeholder="请输入内容" :fetch-suggestions="querySearch"
                         :trigger-on-focus="false">
        </el-autocomplete>
      </div>
      <div class="col-3">
        <span>日期:</span>
        <el-date-picker v-model="date" type="date" value-format="yyyy-MM-dd" placeholder="选择日期"></el-date-picker>
      </div>
      <div class="col-3">
        <el-button @click="init">搜索</el-button>
      </div>
    </div>
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="morning" label="上午"></el-table-column>
      <el-table-column prop="noon" label="中午"></el-table-column>
      <el-table-column prop="afternoon" label="下午"></el-table-column>
      <el-table-column prop="night" label="晚上"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {getDateY_M_D} from "@/api/timeUtil";
import {WorkerApi, WorkerTimeApi} from "@/api/api";

export default {
  name: "workTimeInfo",
  data() {
    return {
      name: "",
      date: getDateY_M_D(),
      data: [],
    }
  },
  methods: {
    async init() {
      let data = {
        date: this.date,
        name: this.name
      }
      let res = await this.$get2(WorkerTimeApi, 0, data)

      if (res.data.code != 1) {
        this.$message('服务器异常');
        return
      }
      this.data = res.data.data
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
    handleSelect() {

    },
    handleEdit() {

    },
    handleDelete() {

    },
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>