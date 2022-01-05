<template>
  <div class="p_c_flexbox_row">
    <div v-if="user">
      <el-dropdown @command="handleCommand">
        <span class="el-dropdown-link">
          <el-avatar :src="FilePathApi+user.avatar" :key="user.avatar"></el-avatar>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="a">退出登录</el-dropdown-item>
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
import jwt_decode from "jwt-decode";
import {FilePathApi} from "@/api/api";
import {userLogout} from "@/api/user";

export default {
  name: "TreeUserIcon",
  data() {
    return {
      FilePathApi
    }
  },
  methods: {

    async login() {

    },
    async register() {

    },
    async logout() {
      await userLogout(this)
    },
    handleCommand(command) {
      this.$message('click on item ' + command);
    }
  },
  computed: {
    user() {
      if (this.$store.state.token) {
        let user = jwt_decode(this.$store.state.token)
        return user
      }
    }
  },
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