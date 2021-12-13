<template>
  <div>
    <router-link :to=url>登录</router-link>
  </div>
</template>

<script>
import {SYS_LOGIN_URL} from "@/api/routerUrl";

export default {
  name: "UserIconCOMPO",
  data() {
    return {
      url: SYS_LOGIN_URL
    }
  }
}
</script>

<style scoped>

</style>