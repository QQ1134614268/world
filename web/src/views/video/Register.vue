<template>
  <div class="p_c_box-flex_row-center col-12">
    <el-form ref="form" :model="form" label-width="8rem">
      <el-form-item label="账号">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item label="邀请码">
        <el-input v-model="form.code"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">确定</el-button>
        <el-button type="primary" @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

import {postJson2} from "@/api/http";
import {VideoUserApi} from "@/api/api";

export default {
  name: "RegisterComponent",
  data() {
    return {
      form: {}
    }
  },
  methods: {
    async onSubmit() {
      let result = await postJson2(VideoUserApi, 0, this.form)
      if (result.data.code === 1) {
        this.$message.success('注册成功');
        await this.$router.push({path: '/'})
      } else {
        this.$message.error('注册失败');
      }
    },
    async onCancel() {
      await this.$router.push({path: '/'})
    },
  }
}
</script>

<style scoped>
</style>