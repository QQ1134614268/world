<template>
  <div class="p_c_flexbox_row">
    <el-dropdown>
      <span class="el-dropdown-link">
        <el-avatar src="@assert/avatar.png"></el-avatar>
        <i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>退出登录</el-dropdown-item>
        <el-dropdown-item>设置</el-dropdown-item>
        <el-dropdown-item>用户空间</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <div v-if="userId">
      <el-avatar></el-avatar>
      下拉
      select
      dropdown
      <!--    todo 需要刷新 使用vuex 等 ,溢出改变同步全局-->
    </div>
    <div v-else>
      <el-button @click="login">登录</el-button>
      <el-button @click="login">注册</el-button>
    </div>
    <el-dropdown @command="handleCommand">
  <span class="el-dropdown-link">
    下拉菜单<i class="el-icon-arrow-down el-icon--right"></i>
  </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="a">黄金糕</el-dropdown-item>
        <el-dropdown-item command="b">狮子头</el-dropdown-item>
        <el-dropdown-item command="c">螺蛳粉</el-dropdown-item>
        <el-dropdown-item command="d" disabled>双皮奶</el-dropdown-item>
        <el-dropdown-item command="e" divided>蚵仔煎</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
export default {
  name: "UserIconCOMPO",
  data() {
    return {
      userId: '',
    }
  },
  methods: {
    async logout() {

    },
    async login() {

    },
    handleCommand(command) {
      this.$message('click on item ' + command);
    }
  }
}
</script>

<style scoped>
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
}

.el-icon-arrow-down {
  font-size: 12px;
}

.demonstration {
  display: block;
  color: #8492a6;
  font-size: 14px;
  margin-bottom: 20px;
}
</style>