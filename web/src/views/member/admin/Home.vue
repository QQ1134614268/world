<template>
  <div>
    <h3 class="header">会员管理系统</h3>
    <main class="p_c_flexbox_row">
      <el-menu router :default-active="this.$route.fullPath" active-text-color="#409EFF">
        <el-menu-item :index="item.menuPath" v-for="(item, index) in menuList" :key="index">
          <template slot="title">
            <i :class="item.menuIcon"></i>
            <span>
                {{ item.menuName }}
              </span>
          </template>
        </el-menu-item>
      </el-menu>
      <router-view class="p_c_flex_1"></router-view>
    </main>

  </div>
</template>

<script>
import {Finance, GoodsList, Order, Qrcode, RolePermission, UserAdmin, UserRole} from "@/views/member";

export default {
  name: "Home",
  data() {
    return {
      GoodsList,
      UserAdmin,
      Qrcode,
      UserRole,
      RolePermission,
      Finance,
      menuList: [
        {
          menuName: "菜单",
          menuPath: GoodsList,
          menuIcon: "el-icon-connection",
        },
        {
          menuName: "订单",
          menuPath: Order,
          menuIcon: "el-icon-connection",
        },
        {
          menuName: "二维码",
          menuPath: Qrcode,
          menuIcon: "el-icon-connection",
        },
        {
          menuName: "用户管理",
          menuPath: UserAdmin,
          menuIcon: "el-icon-connection",
        },
        {
          menuName: "角色管理",
          menuPath: UserRole,
          menuIcon: "el-icon-connection",
        },
        {
          menuName: "权限管理",
          menuPath: RolePermission,
          menuIcon: "el-icon-connection",
        },
        {
          menuName: "财务管理",
          menuPath: Finance,
          menuIcon: "el-icon-connection",
        },
      ]
    }
  }
}
</script>
<style scoped>
.header {
  text-align: center;
}
</style>