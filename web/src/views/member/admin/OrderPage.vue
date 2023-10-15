<template>
  <div class="p_c_HolyGrail-body">
    <el-table :data="page.data">
      <el-table-column prop="user_name" label="用户名"></el-table-column>
      <el-table-column prop="status" label="订单状态"></el-table-column>
      <el-table-column prop="total_price" label="总价"></el-table-column>
      <el-table-column prop="create_time" label="下单时间"></el-table-column>
      <el-table-column label="详情">
        <el-button size="mini" type="danger" @click="init">详情</el-button>
        <el-button size="mini" type="danger" @click="init">删除</el-button>
      </el-table-column>
    </el-table>

    <el-pagination @size-change="init"
                   @current-change="init"
                   :current-page="page.page"
                   :page-size="page.page_size"
                   :total="page.total"
                   layout=" prev, pager, next, total">
    </el-pagination>
  </div>
</template>
<script>
import {orderPage} from "@/api/api";
import {getJson3} from "@/api/http";

export default {
  name: "GoodsAdd",
  data() {
    return {
      page: {
        page: 1,
        page_size: 10,
        data: [],
      },
    };
  },
  methods: {
    async init() {
      let data = {
        store_id: 1
      }
      let res = await getJson3(orderPage, data);
      this.page = res.data
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>