<template>
  <div>
    <header>会员管理系统</header>
    <main class="p_c_flexbox_row">
      <nav class="col-1">
        <li>
          <router-link :to=GoodsList>菜单列表</router-link>
        </li>
        <li>
          <router-link :to=Qrcode>二维码</router-link>
        </li>
        <li>
          <router-link :to=UserAdmin>用户管理</router-link>
        </li>
        <li>
          <router-link :to=UserRole>角色管理</router-link>
        </li>
        <li>
          <router-link :to=RolePermission>权限管理</router-link>
        </li>
        <li>
          <router-link :to=Finance>财务管理</router-link>
        </li>
      </nav>
      <router-view></router-view>
    </main>

  </div>
</template>

<script>
import {Finance, GoodsList, Qrcode, RolePermission, UserAdmin, UserRole} from "@/views/member";

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
    }
  }
}
</script>

<style scoped>

</style>