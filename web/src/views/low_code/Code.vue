<template>
  <div style="display: flex;">
    <div style="width: 20%;border-left: #0a53be">
      <div>
        <div>最近操作</div>
        top,折叠
      </div>
      <div>搜索</div>
      <h1>所有表</h1>
      <div v-for="(item,index) in treeData" :key="item.SCHEMA_NAME">
        <div>
          {{ item.SCHEMA_NAME }}
          <div v-for="(item2, index2) in item.table_list" :key="index" class="table">
            {{ item2.TABLE_NAME }}
          </div>
        </div>
      </div>
    </div>
    <div style="display: flex">
      <div>
        <el-form :model="formData" ref="formData" label-width="100px">
          <el-form-item prop="name" label="表名">
            <el-input v-model="formData.tableName"></el-input>
          </el-form-item>
          <el-form-item prop="name" label="名称">
            <el-input v-model="formData.name"></el-input>
          </el-form-item>
          <el-form-item prop="path" label="路径">
            <el-input v-model="formData.path"></el-input>
          </el-form-item>
          <el-form-item prop="group" label="分组">
            <el-input v-model="formData.group"></el-input>
          </el-form-item>
          <el-form-item prop="group" label="动态显示的列">
            <el-input v-model="formData.cols"></el-input>
          </el-form-item>
        </el-form>
        <el-table ref="multipleTable" @selection-change="handleSelectionChange" :data="colData">
          <el-table-column prop="NUMERIC_SCALE" label="NUMERIC_SCALE"></el-table-column>

          <!--          <el-table-column prop="NUMERIC_SCALE" label="jsForm example">-->
          <!--            <template slot-scope="scope">-->
          <!--              {{ scope.row.example }}-->
          <!--            </template>-->
          <!--          </el-table-column>-->
          <!--          <el-table-column prop="NUMERIC_SCALE" label="jsForm example">-->
          <!--            <template slot-scope="scope">-->
          <!--              {{ scope.row.example }}-->
          <!--            </template>-->
          <!--          </el-table-column>-->

        </el-table>
      </div>
      <div>
        <div>
          <el-tabs>
            <el-tab-pane label="update">
              <div>
                Para
                <Fmt></Fmt>
              </div>
              <div>
                DTO
                <Fmt></Fmt>
              </div>
            </el-tab-pane>
            <el-tab-pane label="select">
              <div style="border-bottom: #0a53be solid 2px">
                Para
                <Fmt></Fmt>
              </div>
              <div>
                DTO
                <Fmt></Fmt>
              </div>
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>
      <!--      <el-table :data="resultData"></el-table>-->
    </div>
  </div>
</template>

<script>
import {getJson3} from "@/api/http";
import Fmt from "@/views/low_code/Fmt.vue";

let get_dbs = "/api/code_api/get_dbs"
let get_tables = "/api/code_api/get_tables"
let get_table_cols = "/api/code_api/get_table_cols"
let get_table_tree = "/api/code_api/get_table_tree"
let get_data = "/api/code_api/get_data"
export default {
  name: "Code",
  components: {
    Fmt
  },
  data() {
    return {
      treeData: [],
      colData: [],
      javaColData: [],

      multipleSelection: [],
      resultData: [],

      formData: {},
    };
  },
  methods: {
    async init() {
      let res = await getJson3(get_table_tree)
      this.treeData = res.data.data
    },
    async getTableCols(tableName) {
      this.formData.tableName = tableName
      let res2 = await getJson3(get_table_cols, {tableName: tableName})
      this.colData = res2.data.data
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;

    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
.table{
  margin-left: 2rem;
}
</style>