<template>
  <div>
    <el-table :data="tableData">
      <el-table-column prop="goods_name" label="商品名称"></el-table-column>
      <el-table-column prop="num" label="商品数量"></el-table-column>
      <el-table-column prop="goods_img" label="商品图片">
        <template slot-scope="scope">
          <el-image style="width: 5rem" :src="scope.row.images"/>
        </template>
      </el-table-column>
      <el-table-column prop="cooker_status" label="状态"></el-table-column>
    </el-table>
  </div>
</template>
<script>
import {FileApi, get_cooker_order} from "@/api/api";
import {getJson3} from "@/api/http";

export default {
  name: "GoodsAdd",
  data() {
    return {
      FileApi,
      form: {images: ''},
      tableData: [],
      store_id: this.$route.query.store_id,
    };
  },
  methods: {
    async init() {
      let data = {
        store_id: 1
      }
      let response = await getJson3(get_cooker_order, data);
      this.tableData = response.data.data
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>