<template>
  <div>
    开启传送门
    <router-link :to=order>订单</router-link>
    <router-link :to=order>优惠券</router-link>

    我的资源
    <el-tree :data="treeData">
    </el-tree>
  </div>
</template>

<script>
import {order} from "@/views/member/index";

export default {
  name: "UserSpace",
  data() {
    return {
      order,
      treeData: []
    }
  }
}
</script>

<style scoped>

</style>