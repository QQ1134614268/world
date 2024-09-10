<template>
  <div class="member_container">
    <h3 class="member_header">会员管理系统</h3>
    <main class="member_body">
      <el-menu router :default-active="this.$route.fullPath" active-text-color="#409EFF" class="menuBox">
        <el-menu-item :index="item.menuPath" v-for="(item, index) in menuList" :key="index">
          <template slot="title">
            <i :class="item.menuIcon"></i>
            <span>
                {{ item.menuName }}
            </span>
          </template>
        </el-menu-item>
      </el-menu>
      <div class="viewBox">
        <router-view/>
      </div>
    </main>
  </div>
</template>

<script>
import {GoodsList, Order, Qrcode} from "@/views/member";

export default {
  name: "HomeComponent",
  data() {
    return {
      GoodsList,
      Qrcode,
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
      ]
    }
  }
}
</script>
<style scoped lang="less">
.member_container {
  width: 100%;
  height: 90%;
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;

  .member_header {
    width: 100%;
    height: 3rem;
    display: flex;
    justify-content: center;
    flex: 0 0 auto;
  }

  .member_body {
    width: 100%;
    height: 100%;
    display: flex;
    flex-shrink: 1;
    /deep/ .menuBox {
      height: 90%;
    }
  }

  .viewBox {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    flex-shrink: 1;
    overflow-y: auto;
  }
}
</style>