<template>
  <div class="codePage">
    <div class="nav">
      <div>最近操作|top,折叠|搜索</div>
      <div v-for="(item,index) in treeData" :key="item.TABLE_NAME">
        <div @click="tableData=item.children">
          {{ item.TABLE_NAME }}
        </div>
      </div>
    </div>
     <el-table :data="tableData" class="table">
        <el-table-column prop="COLUMN_NAME" label="COLUMN_NAME"></el-table-column>
        <el-table-column prop="COLUMN_TYPE" label="COLUMN_TYPE"></el-table-column>
        <el-table-column prop="IS_NULLABLE" label="IS_NULLABLE"></el-table-column>
        <el-table-column prop="COLUMN_COMMENT" label="COLUMN_COMMENT"></el-table-column>
      </el-table>
  </div>
</template>

<script>
import {getJson, getJson3} from "@/api/http";
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
      tableData: [],
      colData: [],
      javaColData: [],

      multipleSelection: [],
      resultData: [],

      formData: {},
    };
  },
  methods: {
    async init() {
      let res2 = await getJson(get_table_tree)
      this.treeData = res2.data
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped lang="less">
.codePage {
  display: flex;

  .nav {
    width: 20%;
    border-left: #0a53be;
  }
  .table{

  }
}

.table {
  margin-left: 2rem;
}
</style>
