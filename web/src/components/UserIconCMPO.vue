<template>
  <div>
    <img alt="加载失败">
    <!--    todo 需要刷新 使用vuex 等 ,溢出改变同步全局-->
    <el-button @click="logout"></el-button>
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
  },
  methods: {
    async logout() {

    }
  }
}
</script>

<style scoped>

</style>