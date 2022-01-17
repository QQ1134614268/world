<template>
  <div class="p_c_box-flex_row-center col-12">
    <el-form ref="form" :model="form" label-width="8rem">
      <el-form-item label="账号">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password" type="password" :show-password=true></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {VideoUserApi} from "@/api/api";
import {get_salt_pwd} from "@/api/const";

export default {
  name: "Home",
  data() {
    return {
      form: {},
    }
  },
  methods: {
    async onLogin() {
      // this.form.password = get_salt_pwd(this.form.password)
      let result = await this.$get2(VideoUserApi, 0, this.form)
      if (result.data.code === 1) {
        localStorage.setItem("token", result.data.data);
        this.$store.commit('receiveUserInfo', {
          token: result.data.data
        })
        await this.$router.push({path: '/video/Market'})
      } else {
        this.$message('登陆失败,请重新检查账号密码');
      }
    },
  }
}
</script>

<style scoped>

</style>