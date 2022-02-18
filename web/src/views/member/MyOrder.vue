<template>
  <div>
    订单(搜索) (商家, 后台, 用户)
    <el-table :data="tableData">
      <el-table-column prop="name" label="商品名" width="180"></el-table-column>
      <el-table-column prop="price" label="商品价格"></el-table-column>
      <el-table-column prop="num" label="商品数量"></el-table-column>
      <el-table-column prop="state" label="状态"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import {OrderApi} from "@/api/api";
import {getUserIdByToken} from "@/api/user";

export default {
  name: "Order",
  data() {
    return {
      url: "",
      tableData: [],
    }
  },
  methods: {
    async init() {
      let data = {user_id: getUserIdByToken}
      let res = await this.$get2(OrderApi, 0, data)
      if (res.data.code != 1) {
        this.$message('服务器异常');
        return
      }
      this.tableData = res.data.data
    }
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>