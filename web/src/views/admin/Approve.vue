<template>
  <div>
    <el-table :data="tableData">
      <el-table-column label="主题" prop="title"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "Approve",
  data(){
    return {
      tableData:[]
    }
  }
}
</script>

<style scoped>

</style>
