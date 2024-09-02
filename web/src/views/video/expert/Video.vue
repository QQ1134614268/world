<template>
  <div class="box">
    <div class="p_c_word-break"> 主题: {{ video.describe }}</div>
    <video preload="true" controls v-if="video.file">
      <source :src="video.file" :key="video.file" type="video/mp4">
      您的浏览器不支持 HTML5 video 标签 。
    </video>
  </div>
</template>

<script>
import {UserApi, WorksApi} from "@/api/api";
import {get2} from "@/api/http";

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
      let result = await get2(WorksApi, this.video_id)
      if (result.data.code === 1) {
        this.video = result.data.data
        document.title = this.video.describe
      } else {
        this.$message.error('失败');
      }
      let result2 = await get2(UserApi, this.video.user_id)
      if (result.data.code === 1) {
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
.box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  align-items: center;
  align-self: center;
  height: 75%;
}
.p_c_word-break {
    white-space: normal;
    word-break: break-all;
    overflow: hidden;
}

</style>