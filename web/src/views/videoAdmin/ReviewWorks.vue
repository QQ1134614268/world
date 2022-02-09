<template>
  <div>
    <el-table :data="tableData">
      <el-table-column label="主题" prop="title"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
           <el-select v-model="scope.row.state" placeholder="请选择">
            <el-option v-for="item in ReviewWorksEnum" :key="item.value" :label="item.code" :value="item.value"></el-option>
          </el-select>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {ReviewWorksApi} from "@/api/api";
import {ReviewEnum} from "@/api/config";

export default {
  name: "Approve",
  data() {
    return {
      tableData: [],
      ReviewWorksEnum: ReviewEnum
    }
  },
  methods: {
    async init() {
      let res = await this.$get2(ReviewWorksApi)
      this.tableData = res.data.data
    },
    async handleEdit() {
    }
  }
}
</script>

<style scoped>

</style>
