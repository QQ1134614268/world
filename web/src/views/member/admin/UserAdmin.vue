<template>
  <div>
    <el-table :data="tableData">
      <el-table-column prop="name" label="姓名"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import {StoreMemberApi} from "@/api/api";

export default {
  name: "UserAdmin",
  data() {
    return {
      tableData: [],
    }
  },
  methods: {
    async init() {
      let res = await this.$get2(StoreMemberApi)
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