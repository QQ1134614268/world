<template>
  <div>
    <el-table :data="tableData">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="role" label="角色"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "UserRole",
  data() {
    return {
      tableData: [],
    }
  }
}
</script>

<style scoped>

</style>