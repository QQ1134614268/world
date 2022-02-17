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
import {UserApi_login} from "@/api/api";
import {RECEIVE_TOKEN, TOKEN} from "@/api/config";
import {VIDEO_MARKET} from "@/views/video/index";
import {storeToken} from "@/api/user";

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
      let result = await this.$get2(UserApi_login, 0, this.form)
      if (result.data.code === 1) {
        storeToken(result.data.data)
        await this.$router.push({path:VIDEO_MARKET})
      }
    },
  }
}
</script>

<style scoped>

</style>