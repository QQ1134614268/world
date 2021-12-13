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
          <el-input placeholder="请输入内容" size="small" v-model="code" clearable style="width: 10em"></el-input>
          <img :src="url" @click="updateCode" alt="验证码" title="点击换一张" style="width: 8rem ;height: 3rem">
        </td>
      </tr>
      <tr>
        <td>
          <el-button type="primary" @click="register" style="width: 10rem">注册</el-button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import {UserApi_get_verify_code, UserApi_register} from "@/api/api";

export default {
  name: "register",
  data() {
    return {
      username: "",
      password: "",
      code: "",
      codeImg: "",
      url: ""
    }
  },
  methods: {
    async updateCode() {
      this.url = process.env.VUE_APP_BASE_URL + UserApi_get_verify_code + "?t=" + Math.random()
    },
    // async get_verify_code() {
    //   let result = await Axios( process.env.VUE_APP_BASE_URL + "/api/sys_api/get_verify_code", {
    //     responseType: "arraybuffer",
    //   })
    //   that.codeImg = 'data:image/png;base64,' + btoa(
    //       new Uint8Array(result.data).reduce((data, byte) => data + String.fromCharCode(byte), '')
    //   );
    // },
    async register() {
      let result = await this.$postJson(UserApi_register, {
        username: this.username,
        password: this.password,
        code: this.code
      });
    },
  },
  created() {
    this.updateCode()
  }
}
</script>

<style scoped>

</style>
