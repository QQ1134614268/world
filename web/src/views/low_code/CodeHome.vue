<template>
  <div>
      <router-view/>
  </div>
</template>

<script>
import {userLogin} from "@/api/user";

export default {
  name: "Home",
  data() {
    return {
      form: {},
    }
  },
  methods: {
    async onLogin() {
      let res = await userLogin(this.form)
      if (res.data.code === 1) {
        this.$message.success('登录成功');
        await this.$router.back()
      } else {
        this.$message.error('登陆失败,请重新检查账号密码');
      }
    },
  }
}
</script>

<style scoped>

</style>