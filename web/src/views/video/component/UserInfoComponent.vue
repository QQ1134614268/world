<template>
  <div style="margin-bottom: 1.6rem" v-if="user">
    <div class="p_c_box-flex_center">
      <el-avatar :src="file_url2+user.avatar" :style="{width:width,height:height}"></el-avatar>
      <span> {{ user.username }} </span>
    </div>
    <div style="font-size: 1.6rem;margin-bottom: 0.6rem">微信号: {{ user.wechat_number }}</div>
    <div style="font-size: 1.6rem;margin-bottom: 0.6rem">抖音号: {{ user.tiktok_number }}</div>
  </div>
</template>

<script>

export default {
  name: "HeaderComponent",
  data() {
    return {
      video_url: "/video/Video",
      url2: '/api/video_api/VideoUserApi',
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      user: ""
    }
  },
  props: {
    user_id: {
      type: Number,
    },
  },
  methods: {
    async init() {
      let result = await this.$get2(this.url2, this.user_id, {})
      if (result.data.code == 1) {
        this.user = result.data.data
        // await this.$router.push({path: 'video/works'})
      } else {
        this.$message('失败');
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