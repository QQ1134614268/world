<template>
  <div>
    <el-tabs :tab-position="'left'" style="height: 200px;">
      <el-tab-pane label="商品列表">
        <Goods></Goods>
      </el-tab-pane>
      <el-tab-pane label="会员列表">
        <Member></Member>
      </el-tab-pane>
      <el-tab-pane label="订单列表">
        <order></order>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import Goods from "@/views/member/Goods";
import Order from "@/views/member/order";
import Member from "@/views/member/Member";

export default {
  name: "Store",
  components: {Member, Order, Goods},
  data() {
    return {};
  },
  methods: {},
}
</script>

<style scoped>


</style>
