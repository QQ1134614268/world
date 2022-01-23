<template>
  <div class="p_c_box-flex">
    <el-menu router class="p_c_HolyGrail-nav col-2 " @open="handleOpen" @close="handleClose" :collapse="isCollapse"
             :default-active="this.$route.fullPath" active-text-color="#3B9DFC">
      <el-menu-item :index="item.menuPath" v-for="(item,index) in menuList">
        <i :class="item.menuIcon"></i>
        {{ item.menuName }}
      </el-menu-item>
    </el-menu>
    <div class="p_c_HolyGrail-body">
      <router-view></router-view>
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
          menuName: "审批",
          menuPath: "/admin/Approve",
          menuIcon: "el-icon-location",
        },
        {
          menuName: "设置",
          menuPath: "/admin/Setting",
          menuIcon: "el-icon-location",
        }
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

</style>