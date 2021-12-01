<template>
  <div style="margin-bottom: 1.6rem" v-if="user">
    <AvatarComponentBase001
        :username="user.username"
        :avatar="user.avatar"
        :width="'4.8rem'"
        :height="'4.8rem'"
    ></AvatarComponentBase001>
    <div style="font-size: 1.6rem;margin-bottom: 0.6rem">微信号: {{user.wechat_number}}</div>
    <div style="font-size: 1.6rem;margin-bottom: 0.6rem">抖音号: {{user.tiktok_number}}</div>
  </div>
</template>

<script>
import AvatarComponentBase001 from "./AvatarComponentBase001"

export default {
  name: "HeaderComponent",
  components: {AvatarComponentBase001},
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