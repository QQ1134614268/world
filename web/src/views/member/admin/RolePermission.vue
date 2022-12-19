<template>
  <div>
    <el-table :data="tableData">
      <el-table-column prop="role" label="角色"></el-table-column>
      <el-table-column prop="permission" label="权限"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "RolePermission",
  data() {
    return {
      tableData: [],
    }
  }
}
</script>

<style scoped>

</style>