<template>
  <div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="店铺名">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password" :value="null"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">登陆</el-button>
        <el-button type="primary" @click="onSubmit">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

import {StoreApi} from "@/api/api";

export default {
  name: "Store",
  data() {
    return {
      form: {},
    };
  },
  methods: {
    async createStore() {
      let response = await this.$postJson2(StoreApi,0, this.form);
      if (response.data.code != 1) {
        return
      }
      this.store = response.data.data
      await this.$router.push({path: '/member/StoreList'})
    },
    async onSubmit() {
      let response = await this.$ppJson(StoreApi, this.form.id, this.form);
      if (response.data.code != 1) {
        this.$message('操作失败');
      } else {
        this.$message('操作成功');
      }
      this.form = {}
    },
  },
  created() {
    this.getStoreList()
  }
}
</script>

<style scoped>


</style>
