<template>
  <div style="width: 50rem;margin: auto;">
    <div>
      <span style="width: 200rem">账号</span>
      <span>
        <el-input
            placeholder="请输入内容"
            v-model="username"
            clearable
            style="width: 10em"
            size="small"
        >
          </el-input>
      </span>
    </div>
    <div>
      <span>密码</span>
      <span>
        <el-input
            placeholder="请输入内容"
            v-model="password"
            clearable
            style="width: 10em"
            size="small"
            show-password
        >
          </el-input>
      </span>
    </div>
    <div>
      <el-button @click="login">登陆</el-button>
    </div>

  </div>
</template>

<script>
// <!--    页面跳转 https://blog.csdn.net/qi_dabin/article/details/82454588  -->
import errDialog from "@/components/err.vue"
import Axios from 'axios'

export default {
  name: "login",
  components: {
    errDialog
  },
  data() {
    return {
      err_message: "",
      err_flag: false,
      username: "",
      password: "",
    }
  },
  methods: {
    async login() {
      let url = '/api/sys_api/login';
      let data = {
        "username": this.username,
        "password": this.password,
      }
      let result = await this.$postJson(url, data)

      if (result.data.code == 1) {
        Axios.defaults.headers.common['token'] = result.data.data
        localStorage.setItem("token", result.data.data);
        this.$message('登陆成功');
        await this.$router.push({path: '/user/UserSpace'})
      } else {
        this.$message('登陆失败,请重新检查账号密码');
      }
    }
  }
}
</script>

<style scoped>

</style>
