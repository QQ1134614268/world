<template>
  <el-table :data="tableData">
    <el-table-column label="主题" prop="title"></el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-select v-model="scope.row.state" placeholder="请选择">
          <el-option v-for="item in ReviewTargetEnum" :key="item.value" :label="item.code"
                     :value="item.value"></el-option>
        </el-select>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>

import {ReviewTargetApi} from "@/api/api";
import {ReviewEnum} from "@/api/config";

export default {
  name: "ReviewTarget",
  data() {
    return {
      tableData: [],
      ReviewTargetEnum: ReviewEnum
    }
  },
  methods: {
    async init() {
      let res = await this.$get2(ReviewTargetApi)
      this.tableData = res.data.data
    },
    async handleEdit() {
    }
  }
}
</script>

<style scoped>

</style>