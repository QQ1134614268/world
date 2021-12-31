<template>
  <div class="p_c_box_margin target">
    <div class="art_title"><a :href="target_url+'?target_id='+target_id">{{ title }} </a></div>
    <div class="art_body"> {{ content }}</div>
    <div class="box">
      <a :href="user_url+'?user_id='+user_id">
        <div class="p_c_box-flex_row-col-center">
          <el-avatar :src="file_url2+avatar"></el-avatar>
          <span> {{ username }} </span>
        </div>
      </a>
    </div>
  </div>
</template>
<script>

export default {
  name: "TargetComponent",
  data() {
    return {
      user_url: "/video/UserInfo2",
      search: "",
      activeName: "first",
      tableData: [],
      currentPage: 1,
      pageSize: 5,
      totalNum: 0,
      url: "/api/video_api/MarketTargetListApi",
      target_url: "/video/TargetInfo",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      rankData: [],
    }
  },
  props: {
    title: {
      type: String,
      default: ""
    },
    content: {
      type: String,
      default: ""
    },
    username: "",
    user_id: "",
    avatar: "",
    price: "",
    target_id: "",
  }
}
</script>

<style scoped>
.art_title {
  font-size: 2.4rem;
  font-weight: bold;
  color: red;
  margin-bottom: 0.8rem;
  margin-top: 0.8rem;
}

.target {
  margin-top: 0.8rem;
  margin-bottom: 0.8rem;
  padding: 1.6rem;
  border-radius: 1rem;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.art_body {
  margin-bottom: 0.8rem;
  margin-top: 0.8rem;
  font-size: 1.6rem;
}

.art_note {
  font-size: 1rem;
  color: grey;
}
</style>