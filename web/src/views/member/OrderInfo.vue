<template>
  <div>
    <el-table :data="tableData">
      <el-table-column prop="create_time" label="时间" width="180"></el-table-column>
      <el-table-column prop="goods_name" label="商品名" width="180"></el-table-column>
      <el-table-column prop="price" label="商品价格"></el-table-column>
      <el-table-column prop="num" label="商品数量"></el-table-column>
      <el-table-column prop="status" label="状态"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "OrderInfo",
  data() {
    return {
      tableData: []
    }
  }
}
</script>

<style scoped>

</style>