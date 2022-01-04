<template>
  <div class="p_c_box-flex_row-center">
    <div class="col-6">
      <div class="p_c_box-flex_row-center">
        <video preload="true" controls v-if="video.file">
          <source :src="file_url2+video.file" type="video/mp4">
          您的浏览器不支持 HTML5 video 标签 。
        </video>
      </div>
      <div class="p_c_word-break"> 主题: {{ video.describe }}</div>
    </div>
  </div>
</template>

<script>
import {VideoUserApi, WorksApi} from "@/api/api";

export default {
  name: "Video",
  data() {
    return {
      video_id: this.$route.query.video_id,
      search: "",
      video: {},
      url: WorksApi,
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
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
      let result2 = await this.$get2(VideoUserApi, this.video.user_id)
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

</style>