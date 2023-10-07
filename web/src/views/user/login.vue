<template>
  <div style="width: 36rem;margin: auto;">
    <div>
      <span style="width: 120rem">账号</span>
      <el-input placeholder="请输入内容" v-model="username" clearable style="width: 20em"></el-input>
    </div>
    <div>
      <span>密码</span>
      <el-input placeholder="请输入内容" v-model="password" clearable style="width: 20em" show-password></el-input>
    </div>
    <div class="p_c_para">
      <el-button type="primary" @click="login">登陆</el-button>
      <router-link :to="{path:this.SYS_REGISTER_URL}">
        <el-button>注册</el-button>
      </router-link>
    </div>
  </div>
</template>

<script>
import errDialog from "@/components/err.vue"
import {SYS_HOME, SYS_REGISTER_URL} from "@/views/sys";
import {userLogin} from "@/api/user";

export default {
  name: "login",
  components: {
    errDialog
  },
  data() {
    return {
      SYS_REGISTER_URL,
      from: this.$route.query.from || SYS_HOME,
      err_message: "",
      err_flag: false,
      username: "",
      password: "",
    }
  },
  methods: {
    async login() {
      let data = {
        "username": this.username,
        "password": this.password,
      }
      let result = await userLogin(data)
      if (result.data.code === 1) {
        this.$message.success('登录成功');
        await this.$router.back()
      } else {
        this.$message.error('登陆失败,请重新检查账号密码');
      }
    }
  }
}
</script>

<style scoped>

</style>
