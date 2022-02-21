<template>
  <div class="p_c_flexbox_row">
    <div v-if="user">
      <el-dropdown @command="handleCommand">
        <span class="el-dropdown-link">
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <div v-else>
      <el-button @click="login">登录</el-button>
      <el-button @click="register">注册</el-button>
    </div>
  </div>
</template>

<script>
import {userLogout} from "@/api/user";

export default {
  name: "TreeUserIcon",
  data() {
    return {}
  },
  methods: {

    async login() {

    },
    async register() {

    },
    async logout() {
      await userLogout()
    },
    handleCommand(command) {
      this.$message('click on item ' + command);
    }
  },
  computed: {
    user() {
      return this.$store.state.userInfo
    }
  },
}
</script>

<style scoped>
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
}

</style>