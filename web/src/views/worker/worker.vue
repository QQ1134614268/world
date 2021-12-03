<template>
  <div>
    todo excel  导入 导出 修改 修改 排序 筛选 分页
    <el-table :data="dataList" style="width: 100%" height="500">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="id_card_number" label="身份证"></el-table-column>
      <el-table-column prop="sex" label="性别"></el-table-column>
      <el-table-column prop="pay" label="薪资"></el-table-column>
      <el-table-column prop="birthday" label="入职时间"></el-table-column>
      <el-table-column prop="phone" label="联系电话"></el-table-column>
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
export default {
  name: "MyWorker",
  data() {
    return {
      dataList: [],
      multipleSelection: "",
      options: [{
        value: '男',
        label: '男'
      }, {
        value: '女',
        label: '女'
      },]
    }
  },
  methods: {
    async init() {
      let url = '/api/work_api/WorkerApi';
      let response = await this.$get2(url, 0);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.dataList = response.data.data
    },
    async save() {
      let url = '/api/work_api/WorkerApi';
      let response = await this.$putJson(url, this.dataList);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.$message('success');
    },
    async add() {
      this.dataList.push(
          {
            name: "",
            birthday: null,
            id_card_number: "",
            sex: null,
            pay: "",
            start_time: null
          }
      )
    },

    async exportExcel() {
      let url = '/api/work_api/WorkerApi';
      let response = await this.$get(url);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.dataList = response.data.data
    },
    async importExcel() {
      let url = '/api/work_api/WorkerApi';
      let response = await this.$get(url);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.dataList = response.data.data
    },

    handleEdit(index, row) {

    },
    async handleDelete(index, row) {
      let url = '/api/work_api/WorkerApi';
      let data = [index]
      let response = await this.$deleteJson(url, data);
    }
  }
  ,
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>
