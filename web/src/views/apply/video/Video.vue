<template>
  <div class="p_c_box-flex_row-center">
    <div class="col-6">
      <HeaderComponent :user_id="this.user.id" v-if="this.user.id" class=""></HeaderComponent>
      <div class="p_c_box-flex_row-center">
        <video  preload="true" controls v-if="video.file">
          <source :src="file_url3+video.file" type="video/mp4">
          您的浏览器不支持 HTML5 video 标签 。
        </video>
      </div>
      <div class="p_c_word-break"> 主题: {{ video.describe }}</div>
    </div>
  </div>
</template>

<script>
import HeaderComponent from "./component/avatar/HeaderComponent"

export default {
  name: "Video",
  data() {
    return {
      video_id: this.$route.query.video_id,
      search: "",
      activeName: "first",
      video: {},
      url: "/api/video_api/WorksApi",
      user_url: "/api/video_api/VideoUserApi",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      file_url3:"/upload_file/",
      user: {},
    }
  },
  components: {HeaderComponent},
  methods: {
    async init() {

      let result = await this.$get2(this.url, this.video_id)
      if (result.data.code == 1) {
        this.video = result.data.data
        document.title = this.video.describe
      } else {
        this.$message('失败');
      }
      let result2 = await this.$get2(this.user_url, this.video.user_id)
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