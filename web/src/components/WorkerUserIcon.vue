<template>
  <div class="p_c_flexbox_row">
    <div v-if="user">
      <el-dropdown>
        <span class="el-dropdown-link">
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>
            <a @click="logout">退出登录</a>
          </el-dropdown-item>
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
import {USER_LOGIN_URL, USER_REGISTER_URL} from "@/views/user";

export default {
  name: "WorkerUserIcon",
  data() {
    return {}
  },
  methods: {

    async login() {
      await this.$router.push({path: USER_LOGIN_URL})
    },
    async logout() {
      await userLogout()
      this.$message.success('退出登录');
    },
    async register() {
      await this.$router.push({path: USER_REGISTER_URL})
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