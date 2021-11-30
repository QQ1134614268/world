<template>
  <div>
    <el-date-picker
        value-format="yyyy-MM-dd"
        v-model="month"
        type="month"
        format="yyyy 年 MM 月"
        placeholder="选择月"
        @change="init">
    </el-date-picker>
    <el-select v-model="workerId" placeholder="请选择" @change="init">
      <el-option
          v-for="item in workers"
          :key="item.id"
          :label="item.name"
          :value="item.id">
      </el-option>
    </el-select>
    <el-table stripe :data="workerTime" style="width: 100%" height="400">
      <el-table-column label="时间" prop="date"></el-table-column>
      <el-table-column label="姓名" prop="name"></el-table-column>
      <el-table-column label="上午" prop="morning"></el-table-column>
      <el-table-column label="中午" prop="noon"></el-table-column>
      <el-table-column label="下午" prop="afternoon"></el-table-column>
      <el-table-column label="晚上" prop="night"></el-table-column>
      <el-table-column label="备注" prop="note"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "MonthTime",
  data() {
    return {
      month: new Date().getFullYear() + "-" + (new Date().getMonth() + 1) + "-" + new Date().getDate(),
      work_name: null,
      workerTime: [],
      workerId: "",
      workers: []
    }
  },
  methods: {
    async init() {
      let url = '/api/work_api/WorkerTimeApi';
      let data = {
        month: this.month,
        workerId: this.workerId
      }
      let response = await this.$get(url, data);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.workerTime = response.data.data
    },
    async init2() {
      let url = '/api/work_api/WorkerApi';
      let response = await this.$get(url);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.workers = response.data.data
    },
    dateFtt(date, fmt) { //author: meizz
      let o = {
        "M+": date.getMonth() + 1,     //月份
        "d+": date.getDate(),     //日
        "h+": date.getHours(),     //小时
        "m+": date.getMinutes(),     //分
        "s+": date.getSeconds(),     //秒
        "q+": Math.floor((date.getMonth() + 3) / 3), //季度
        "S": date.getMilliseconds()    //毫秒
      };
      if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1, (date.getFullYear() + "").substr(4 - RegExp.$1.length));
      for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
          fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
      return fmt;
    }
  },
  created() {
    this.init()
    this.init2()
  }
}
</script>

<style scoped>

</style>