<template>
  <div class="p_c_box_margin p_c_box-shadow">
    <ThumbnailComponent :describe="describe" :thumbnail="thumbnail" :id="id">
    </ThumbnailComponent>
    <div class="box">
      <a :href="user_url+'?user_id='+user_id">
        <div class="p_c_flexbox_row  p_c_box-flex_row-col-center">
          <el-avatar :src="file_url2+avatar"></el-avatar>
          <span>
            {{ username }}
          </span>
        </div>
      </a>
    </div>
  </div>
</template>

<script>

import ThumbnailComponent from "@/views/video/component/ThumbnailComponent";
import {VideoUrl} from "@/api/routerUrl";

export default {
  name: "VideoCard",
  data() {
    return {
      user_url: "/video/UserInfo",
      video_url: VideoUrl,
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }
  },
  components: {
    ThumbnailComponent
  },
  props: {
    avatar: {
      type: String,
      default: ""
    },
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