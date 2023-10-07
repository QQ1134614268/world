<template>
  <div style="width: 50%;margin: auto;">
    <table>
      <tr>
        <td>用户名</td>
        <td>
          <el-input placeholder="请输入内容" v-model="username" clearable style="width: 20em"></el-input>
        </td>
      </tr>
      <tr>
        <td>密码</td>
        <td>
          <el-input placeholder="请输入内容" v-model="password" clearable show-password style="width: 20em"></el-input>
        </td>
      </tr>
      <tr>
        <td>验证码</td>
        <td>
          <el-input placeholder="请输入内容" size="small" v-model="code" clearable style="width: 5rem"></el-input>
          <img :src="url" @click="updateCode" alt="验证码" title="点击换一张" style="width: 6rem ;height: 2rem">
        </td>
      </tr>
      <tr>
        <td>
          <el-button type="primary" @click="register" style="width: 6rem">注册</el-button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import {UserApi_get_verify_code} from "@/api/api";
import {userRegister} from "@/api/user";

export default {
  name: "register",
  data() {
    return {
      username: "",
      password: "",
      code: "",
      url: UserApi_get_verify_code
    }
  },
  methods: {
    async updateCode() {
      this.url = UserApi_get_verify_code + "?t=" + Math.random()
    },
    async register() {
      let data = {
        username: this.username,
        password: this.password,
        code: this.code,
      }
      await userRegister(data)
      this.$message.success("注册成功")
      this.$router.back()
    },
    // async init() {
    //   let url = "/api/hello_api/test_base64_img"
    //   let data = await get2(url)
    //   this.url = data.data
    // },
  },
  // created() {
  //   this.updateCode()
  // }
}
</script>

<style scoped>

</style>
