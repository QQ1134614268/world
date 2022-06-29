<template>
  <div>
    <el-tree :data="treeData" style="height: 20rem">
    </el-tree>
    <el-table :data="tableData" style="height: 20rem; overflow-y: scroll">
      <el-table-column prop="TABLE_NAME" label="TABLE_NAME"></el-table-column>
      <el-table-column prop="TABLE_COMMENT" label="TABLE_COMMENT"></el-table-column>
    </el-table>
    <el-table :data="colData" style="height: 20rem; overflow-y: scroll">
      <el-table-column prop="COLUMN_NAME" label="COLUMN_NAME"></el-table-column>
      <el-table-column prop="COLUMN_COMMENT" label="COLUMN_COMMENT"></el-table-column>
      <el-table-column prop="DATA_TYPE" label="DATA_TYPE"></el-table-column>
      <el-table-column prop="COLUMN_TYPE" label="COLUMN_TYPE"></el-table-column>
      <el-table-column prop="IS_NULLABLE" label="IS_NULLABLE"></el-table-column>
      <el-table-column prop="TABLE_NAME" label="TABLE_NAME"></el-table-column>
      <el-table-column prop="ORDINAL_POSITION" label="ORDINAL_POSITION"></el-table-column>
      <el-table-column prop="NUMERIC_PRECISION" label="NUMERIC_PRECISION"></el-table-column>
      <el-table-column prop="NUMERIC_SCALE" label="NUMERIC_SCALE"></el-table-column>
    </el-table>

    <el-table :data="javaColData" style="height: 20rem; overflow-y: scroll">
      <el-table-column prop="COLUMN_NAME" label="COLUMN_NAME"></el-table-column>
      <el-table-column prop="COLUMN_COMMENT" label="COLUMN_COMMENT"></el-table-column>
      <el-table-column prop="DATA_TYPE" label="DATA_TYPE"></el-table-column>
      <el-table-column prop="COLUMN_TYPE" label="COLUMN_TYPE"></el-table-column>
      <el-table-column prop="IS_NULLABLE" label="IS_NULLABLE"></el-table-column>
      <el-table-column prop="TABLE_NAME" label="TABLE_NAME"></el-table-column>
      <el-table-column prop="ORDINAL_POSITION" label="ORDINAL_POSITION"></el-table-column>
      <el-table-column prop="NUMERIC_PRECISION" label="NUMERIC_PRECISION"></el-table-column>
      <el-table-column prop="NUMERIC_SCALE" label="NUMERIC_SCALE"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import {getJson2} from "@/api/http";

let get_tables = "/api/code_api/code_blueprint_api/get_tables"
let get_table_cols = "/api/code_api/code_blueprint_api/get_table_cols"
let get_data = "/api/code_api/code_blueprint_api/get_data"
export default {
  name: "Code",
  data() {
    return {
      treeData: [],
      tableData: [],
      colData: [],
      javaColData: [],
    };
  },
  methods: {
    async init() {
      // this.treeData = getJson2()
      let res = await getJson2(get_tables)
      this.tableData = res.data.data
      let res2 = await getJson2(get_table_cols, {tableName: "user"})
      this.colData = res2.data.data
      // this.javaColData = getJson2(get_data)
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>