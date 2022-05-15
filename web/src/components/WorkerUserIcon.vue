<template>
  <div class="p_c_flexbox_row">
    <div v-if="user">
      <el-dropdown>
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
  name: "WorkerUserIcon",
  data() {
    return {}
  },
  methods: {

    async login() {

    },
    async logout() {
      await userLogout()
      this.$message.success('退出登录');
    },
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