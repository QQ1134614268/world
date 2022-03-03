<template>
  <div class="box">
    <div class="p_c_word-break"> 主题: {{ video.describe }}</div>
    <video id="myVideo" class="video-js vjs-default-skin vjs-big-play-centered" muted autoplay controls preload loop>
      <source :src="video.file" type="video/mp4">
    </video>
  </div>
</template>

<script>
import {UserApi, WorksApi} from "@/api/api";

export default {
  name: "Video",
  data() {
    return {
      video_id: this.$route.query.video_id,
      video: {},
      user: {},
    }
  },
  methods: {
    async init() {
      let result = await this.$get2(WorksApi, this.video_id)
      if (result.data.code == 1) {
        this.video = result.data.data
        document.title = this.video.describe
      } else {
        this.$message('失败');
      }
      let result2 = await this.$get2(UserApi, this.video.user_id)
      if (result.data.code == 1) {
        this.user = result2.data.data
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
.box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  align-items: center;
  align-self: center;
}
</style>