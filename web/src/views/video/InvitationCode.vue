<template>
  <div>
    我的邀请码:
    <div>{{ code }}</div>
    <div>
      <el-button @click="init"> 再生成一个</el-button>
    </div>
    快去邀请朋友吧!
    <div>note: 一周有效</div>
  </div>
</template>

<script>
import {InvitationCodeApi} from "@/api/api";

export default {
  name: "InvitationCode",
  data() {
    return {
      code: [],
    }
  },
  methods: {
    async init() {
      let data = {}
      let res = await this.$get2(InvitationCodeApi, 0, data)
      if (res.data.code != 1) {
        this.$message('服务器异常');
        return
      }
      this.code = res.data.data
    }
  },
  created() {
  },

}
</script>

<style scoped>

</style>