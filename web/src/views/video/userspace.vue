<template>
  <div style="display:flex; align-items:center ; flex-direction: column; ">
    <div class="block">
      <router-link to="Setting">编辑</router-link>
    </div>
    <el-avatar :src="form.avatar" :key="form.avatar"></el-avatar>
    <div> 签名: {{ form.describe }}</div>
    <div> 手机号: {{ form.phone }}</div>
    <div> 微信号: {{ form.wechat_number }}</div>
  </div>
</template>

<script>
import {UserApi} from "@/api/api";
import {get2, putJson2} from "@/api/http";

export default {
  name: "video_user",
  data() {
    return {
      user_id: this.$route.query.user_id,
      form: {},
      rules: {
        phone: [{required: true, message: '手机号不能为空', trigger: 'blur'}],
      },
      dialogVisible: false,
    }
  },

  methods: {
    async init() {
      let result = await get2(UserApi, this.user_id)
      if (result.data.code === 1) {
        this.form = result.data.data
      } else {
        this.$message.success('操作成功');
      }
    },
    async save() {
      let result = await putJson2(UserApi, this.form.id, this.form)
      if (result.data.code === 1) {
        this.$message.success('操作成功');
      } else {
        this.$message.error('');
      }
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
</style>