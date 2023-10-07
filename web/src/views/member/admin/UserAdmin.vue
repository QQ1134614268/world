<template>
  <div>
    <el-table :data="tableData">
      <el-table-column prop="username" label="姓名"></el-table-column>
      <el-table-column prop="role" label="角色"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import {StoreMemberApi} from "@/api/api";
import {get2} from "@/api/http";

export default {
  name: "UserAdmin",
  data() {
    return {
      tableData: [],
    }
  },
  methods: {
    async init() {
      let res = await get2(StoreMemberApi)
      this.tableData = res.data.data
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>