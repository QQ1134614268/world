<template>
  <div class="p_c_box-flex_center p_c_HolyGrail-body">
    <div>
      <el-button @click="update"> 生成我的邀请码</el-button>
    </div>
    <div class="block">{{ code }}</div>
    <div v-if="code">
      <div>快去邀请朋友吧!</div>
      <!--      <div>note: 一周有效</div>-->
    </div>
  </div>
</template>

<script>
import {InvitationCodeApi} from "@/api/api";

export default {
  name: "InvitationCode",
  data() {
    return {
      code: '',
    }
  },
  methods: {
    async update() {
      let data = {}
      let res = await this.$putJson2(InvitationCodeApi, 0, data)
      if (res.data.code != 1) {
        this.$message.error('服务器异常');
        return
      }
      this.code = res.data.data
    }
  },
}
</script>

<style scoped>

</style>