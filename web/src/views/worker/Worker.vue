<template>
  <div>
    <div>
      <el-button @click="add">增加</el-button>
      <el-button @click="deleteItem">删除</el-button>
      <el-button @click="save">保存</el-button>
    </div>
    <el-table :data="dataList" style="width: 100%" height="500" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column fixed prop="date" label="姓名">
        <template slot-scope="scope">
          <el-input v-model="scope.row.name" placeholder="请输入内容"
                    @change="handleEdit(scope.$index, scope.row)"></el-input>
        </template>
      </el-table-column>
      <el-table-column fixed prop="date" label="身份证号码">
        <template slot-scope="scope">
          <el-input v-model="scope.row.id_card_number" placeholder="请输入内容"
                    @change="handleEdit(scope.$index, scope.row)"></el-input>
        </template>
      </el-table-column>
      <el-table-column fixed prop="date" label="性别">
        <template slot-scope="scope">
          <el-select v-model="scope.row.sex" placeholder="请选择">
            <el-option v-for="item in options"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
            </el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column fixed prop="date" label="薪资">
        <template slot-scope="scope">
          <el-input v-model="scope.row.pay" placeholder="请输入内容"
                    @change="handleEdit(scope.$index, scope.row)"></el-input>
        </template>
      </el-table-column>
      <el-table-column fixed prop="date" label="入职时间">
        <template slot-scope="scope">
          <el-date-picker
              v-model="scope.row.start_time"
              type="date"
              format="yyyy 年 MM 月 dd 日"
              value-format="yyyy-MM-dd"
              placeholder="选择日期">
          </el-date-picker>
        </template>
      </el-table-column>
      <el-table-column fixed prop="date" label="联系电话">
        <template slot-scope="scope">
          <el-input v-model="scope.row.phone" placeholder="请输入内容"
                    @change="handleEdit(scope.$index, scope.row)"></el-input>
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
      let response = await this.$get(url);
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
    async deleteItem() {
      let val = this.multipleSelection
      let url = '/api/work_api/WorkerApi';
      let data = []
      let data2 = this.dataList
      val.forEach(function (item, index) {
        data.push(item.id)
      })
      let response = await this.$deleteJson(url, data);
      if (response.data.code != 1) {
        this.$message('网站出错了');
        return
      }
      // 如果选中数据存在
      if (val) {
        // 将选中数据遍历
        val.forEach(function (item, index) {
          // 遍历源数据
          data2.forEach(function (itemI, indexI) {
            if (item.id === itemI.id) {
              data2.splice(indexI, 1)
            }
          })
        })
      }
      // // 清除选中状态
      // this.$refs.multipleTable.clearSelection()
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    handleEdit(index, row) {

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
