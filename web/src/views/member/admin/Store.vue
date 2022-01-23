<template>
  <div class="p_c_flexbox">
    <el-menu router :default-active="this.$route.fullPath" active-text-color="#409EFF">
      <el-menu-item :index="item.menuPath" v-for="item in menuList">
        <template slot="title">
          <i :class="item.menuIcon"></i>
          <span>
                {{ item.menuName }}
          </span>
        </template>
      </el-menu-item>
    </el-menu>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Goods from "@/views/member/admin/Goods";
import Order from "@/views/member/admin/order";
import Member from "@/views/member/admin/Member";

export default {
  name: "Store",
  components: {Member, Order, Goods},
  data() {
    return {
      menuList: [
        {
          menuName: "商品列表",
          menuPath: "/member/Store/Goods",
          menuIcon: "el-icon-location",
        },
        {
          menuName: "订单列表",
          menuPath: "/member/Store/order",
          menuIcon: "el-icon-location",
        },
        {
          menuName: "会员列表",
          menuPath: "/member/Store/Member",
          menuIcon: "el-icon-location",
        },
      ]
    };
  },
  methods: {},
}
</script>

<style scoped>


</style>
