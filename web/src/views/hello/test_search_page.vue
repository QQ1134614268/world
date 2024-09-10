<template>
  <div class="content">
    <el-row>
      <el-input @keyup.enter.native="search" v-model="searchContent" size="small" placeholder="enter或按钮搜索"></el-input>
      <el-button type="primary" size="small" @click="search">搜索</el-button>
    </el-row>

    <el-row>
      <el-input v-model="watchSearch" placeholder="watch监听搜索" size="small"></el-input>
    </el-row>

    <el-table :data="paginationData" border style="width: 100%;">
      <el-table-column prop="id" label="id" align="center"></el-table-column>
      <el-table-column prop="listOne" label="listOne" align="center"></el-table-column>
      <el-table-column prop="listTwo" label="listTwo" align="center"></el-table-column>
      <el-table-column prop="listThree" label="listThree" align="center"></el-table-column>
      <el-table-column prop="listFour" label="listFour" align="center"></el-table-column>
      <el-table-column prop="listFive" label="listFive" align="center"></el-table-column>
      <el-table-column prop="listSix" label="listSix" align="center"></el-table-column>
    </el-table>

    <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[5, 10, 15, 20]"
        :page-size="pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        style="margin:1rem 0">
    </el-pagination>

  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {id: "1", listOne: "sunny", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "2", listOne: "boy", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "3", listOne: "six", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "4", listOne: "sun", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "5", listOne: "girl", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "5", listOne: "one", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "6", listOne: "two", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "7", listOne: "three", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "8", listOne: "five", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "9", listOne: "six", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "10", listOne: "seven", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "11", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "12", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "13", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "14", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "15", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "16", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "17", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "18", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "19", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
        {id: "20", listOne: "1", listTwo: "2", listThree: "3", listFour: "4", listFive: "5", listSix: "6"},
      ],
      total: 0, //数组总数
      currentPage: 1, //当前页
      paginationData: [], //分页数组
      pagesize: 5, //每页数据
      searchContent: "",//搜索内容
      stashList: [],
      watchSearch: ""
    }
  },
  created() {
    this.getList()
  },
  watch: {
    watchSearch: {
      handler(newValue, oldValue) {
        console.log(newValue, oldValue)
        let self = this
        if (newValue) {
          //这里要从暂存的所有数据中过滤 放到展示的数组中
          self.tableData = self.stashList.filter(item => {
            return item.listOne.includes(newValue)
          })
        } else {
          self.tableData = self.stashList
        }
        self.tableList()
      },
      deep: true
    }
  },
  methods: {
    getList() {
      //一般这里会有一个axios请求
      this.handleCurrentChange(this.currentPage)
      this.stashList = this.tableData  //暂存数组  当搜索为空时候  数组展示所有数据
    },
    handleSizeChange(val) {
      this.pagesize = val
      this.tableList()
    },
    handleCurrentChange(val) {
      this.currentPage = val
      this.tableList()
    },
    tableList() {
      this.paginationData = []  //分页数组  tableData 所有的数据
      for (var j = this.pagesize * (this.currentPage - 1); j < this.pagesize * this.currentPage; j++) {
        if (this.tableData[j]) {
          this.paginationData.push(this.tableData[j])
        }
      }
      this.total = this.tableData.length
    },
    search() {
      if (this.searchContent) {
        this.tableData = this.tableData.filter(item => {
          return item.listOne.includes(this.searchContent)
        })
      } else {
        this.tableData = this.stashList
      }
      this.tableList()
    }
  }
}
</script>
