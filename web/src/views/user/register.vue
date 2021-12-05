<template>
  <div style="width: 50%;margin: auto;">
    <table>
      <tr>
        <td>用户名</td>
        <td>
          <el-input
              placeholder="请输入内容"
              v-model="username"
              clearable
              style="width: 20em">
          </el-input>
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
          <el-input placeholder="请输入内容" size="small" v-model="code" clearable style="width: 10em"></el-input>
          <img :src="codeImg" alt="加载图片失败..." style="width: 8rem ;height: 3rem">
          <button @click="get_verify_code()"> 获取验证码</button>
        </td>
      </tr>
      <tr>
        <td>
          <el-button @click="register" style="width: 10rem">注册</el-button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import Axios from 'axios'

export default {
  name: "register",
  data() {
    return {
      input: "",
      err_message: "",
      err_flag: false,
      username: "tt",
      password: "",
      code: "",
      codeImg: ""
    }
  },
  methods: {
    async get_verify_code() {
      let that = this
      let baseURL = process.env.VUE_APP_BASE_URL
      let result = await Axios(baseURL + "/api/sys_api/get_verify_code", {
        responseType: "arraybuffer",
        params: {"username": that.username}
      })
      that.codeImg = 'data:image/png;base64,' + btoa(
          new Uint8Array(result.data).reduce((data, byte) => data + String.fromCharCode(byte), '')
      );
    },
    async register() {
      let url = '/api/sys_api/register';
      let result = await this.$postJson(url, {
        username: this.username,
        password: this.password,
        code: this.code
      });
      this.$worldResult = result
    },
  }
}</script>

<style scoped>

</style>
