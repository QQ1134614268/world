<template>
  <div>
    开启传送门
    <div>
      <router-link :to=order>订单</router-link>
    </div>
    <div>
      <router-link :to=order>优惠券</router-link>
    </div>

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