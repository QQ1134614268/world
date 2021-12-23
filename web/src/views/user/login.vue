<template>
  <div style="width: 50rem;margin: auto;">
    <div>
      <span style="width: 200rem">账号</span>
      <el-input placeholder="请输入内容" v-model="username" clearable style="width: 20em"></el-input>
    </div>
    <div>
      <span>密码</span>
      <el-input placeholder="请输入内容" v-model="password" clearable style="width: 20em" show-password></el-input>
    </div>
    <div class="p_c_para">
      <el-button type="primary" @click="login">登陆</el-button>
      <router-link :to="{path:this.registerUrl,query: {from: this.from}}">
        <el-button>注册</el-button>
      </router-link>
    </div>
  </div>
</template>

<script>
// <!--    页面跳转 https://blog.csdn.net/qi_dabin/article/details/82454588  -->
import errDialog from "@/components/err.vue"
import Axios from 'axios'
import {SYS_HOME, SYS_REGISTER} from "@/api/routerUrl";
import {sys_api_login} from "@/api/api";

export default {
  name: "login",
  components: {
    errDialog
  },
  data() {
    return {
      registerUrl: SYS_REGISTER,
      from: this.$route.query.from,
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
      let result = await this.$postJson(sys_api_login, data)

      if (result.data.code == 1) {
        Axios.defaults.headers.common['token'] = result.data.data
        localStorage.setItem("token", result.data.data);
        this.$message('登录成功');
        // await this.$router.go({path: '/user/UserSpace'}) todo
        // 弹框式登录
        if (this.from != null) {
          await this.$router.push(this.from)
        } else {
          await this.$router.push({path: SYS_HOME})
        }
      } else {
        this.$message('登陆失败,请重新检查账号密码');
      }
    }
  }
}
</script>

<style scoped>

</style>
