<template>
<div>
  <h1 style="text-align: center">人人影后台系统</h1>
  <div class="p_c_box-flex">
    <el-menu router class="menu" @open="handleOpen" @close="handleClose" :collapse="isCollapse"
             :default-active="this.$route.fullPath" active-text-color="#3B9DFC">
      <el-menu-item :index="item.menuPath" v-for="(item, index) in menuList" :key="index">
        <i :class="item.menuIcon"></i>
        {{ item.menuName }}
      </el-menu-item>
    </el-menu>
    <div class="p_c_HolyGrail-body">
      <router-view></router-view>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      isCollapse: true,
      menuList: [
        {
          menuName: "审批作品",
          menuPath: "/videoAdmin/ReviewWorks",
          menuIcon: "el-icon-location",
        },
        {
          menuName: "审批发布消息",
          menuPath: "/videoAdmin/ReviewTarget",
          menuIcon: "el-icon-location",
        },
        // {
        //   menuName: "设置",
        //   menuPath: "/videoAdmin/Setting",
        //   menuIcon: "el-icon-location",
        // }
      ],
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  }
}
</script>

<style scoped>
.menu{
  width: 10rem;
}
</style>