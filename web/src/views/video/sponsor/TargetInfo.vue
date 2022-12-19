<template>
  <div class="p_c_box-flex_row-center">
    <div class="col-6">
      <div class="art_title"> {{ target.title }}</div>
      <div class="art_body"> {{ target.content }}</div>
      <div class="art_note"> 佣金:{{ target.price }}</div>
    </div>
  </div>
</template>

<script>

import {TargetApi, UserApi} from "@/api/api";

export default {
  name: "TargetInfo",
  data() {
    return {
      target_id: this.$route.query.target_id,
      search: "",
      target: {},
      user: "",
    }
  },
  methods: {
    async init() {
      let result = await this.$get2(TargetApi, this.target_id)
      if (result.data.code == 1) {
        this.target = result.data.data
        document.title = this.target.title
      } else {
        this.$message.error('失败');
      }
      let result2 = await this.$get2(UserApi, this.target.user_id)
      if (result.data.code == 1) {
        this.user = result2.data.data
      } else {
        this.$message.error('失败');
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