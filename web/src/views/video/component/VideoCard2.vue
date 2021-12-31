<template>
  <div class="p_c_box_margin">
    <ThumbnailComponent :describe="describe" :thumbnail="thumbnail" :id="id">
    </ThumbnailComponent>
    <time>{{ create_time }}</time>
  </div>
</template>

<script>

import ThumbnailComponent from "@/views/video/component/ThumbnailComponent";

export default {
  name: "VideoCard2",
  data() {
    return {
      video_url: "/video/Video",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }
  },
  components: {
     ThumbnailComponent
  },
  props: {
    username: {
      type: String,
      default: ""
    },
    user_id: {
      type: Number,
      default: ""
    },
    create_time: {
      type: String,
      default: ""
    },
    thumbnail: {
      type: String,
      default: ""
    },
    describe: {
      type: String,
      default: ""
    },
    id: {
      type: Number,
      default: ""
    },
  }
}
</script>

<style scoped>

</style>