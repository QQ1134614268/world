<template>
  <div>
    <router-link :to=url>登录</router-link>
  </div>
</template>

<script>
import {SYS_LOGIN} from '@/api/const.js'

export default {
  name: "UserIconCOMPO",
  data() {
    return {
      url: SYS_LOGIN
    }
  }
}
</script>

<style scoped>

</style>