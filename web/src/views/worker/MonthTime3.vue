<template>
  <div>
    <div>
      日期:
      <el-date-picker
          v-model="date"
          type="date"
          format="yyyy 年 MM 月 dd 日"
          value-format="yyyy-MM-dd"
          placeholder="选择日期">
      </el-date-picker>
      选择工人:
      <el-select v-model="worker_id" placeholder="请选择">
        <el-option
            v-for="item in workers"
            :key="item.id"
            :label="item.name"
            :value="item.id">
        </el-option>
      </el-select>
      <el-button @click="save">确定</el-button>
    </div>
    <div>
      <el-checkbox-group v-model="checkboxGroup2" size="medium">
        <el-checkbox-button v-for="worker in options" :label="worker.value" :key="worker.value">
          {{ worker.value }}
        </el-checkbox-button>
      </el-checkbox-group>
    </div>
  </div>
</template>

<script>
export default {
  name: "MonthTime",
  data() {
    return {
      checkboxGroup2: [],
      workers: [],
      date: new Date().getFullYear() + "-" + (new Date().getMonth() + 1) + "-" + new Date().getDate(),
      worker_id: "",
      options: [
        {value: '上午', label: '上午'},
        {value: '下午', label: '下午'},
        {value: '全天', label: '全天'},
        {value: '中午', label: '中午'},
        {value: '晚上', label: '晚上'},
      ]
    }
  },
  methods: {
    async init2() {
      let url = '/api/work_api/WorkerApi';
      let response = await this.$get(url);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.workers = response.data.data
    },
    async save() {
      let url = '/api/work_api/WorkerTimeApi';
      let data = {
        worker_id: this.worker_id,
        date: this.date,
        type: this.checkboxGroup2
      }
      let response = await this.$postJson(url, data);
      if (response.data.code != 1) {
        this.$message(response.data.data);
      } else {
        this.$message('success');
      }
    },
  },
  created() {
    this.init2()
  }
}
</script>

<style scoped>

</style>