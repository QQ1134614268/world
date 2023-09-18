<template>
  <div>
    订单(搜索) (商家, 后台, 用户)
    <el-table :data="tableData">
      <el-table-column prop="create_time" label="时间" width="180">
        <template slot-scope="scope">
          <router-link :to="{path:OrderInfo,query:{'order_code':scope.row.order_code}}">{{ scope.row.create_time }}
          </router-link>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {OrderApi} from "@/api/api";
import {FoodInfo} from "@/views/member/index";

export default {
  name: "Order",
  data() {
    return {
      url: "",
      store_id: 1,
      tableData: [],
      OrderInfo: FoodInfo
    }
  },
  methods: {
    async init() {
      let data = {
        store_id: this.store_id
      }
      let res = await this.$get2(OrderApi, 0, data)
      if (res.data.code !== 1) {
        this.$message.error('服务器异常');
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