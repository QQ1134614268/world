<template>
  <div class="col-12">
    <HeaderComponent :user_id="user_id"></HeaderComponent>
    <div class="p_c_flexbox">
      <div v-for="o in tableData" class="col-3">
        <VideoCard2 :username="o.username" :user_id="o.user_id" :create_time="o.create_time" :thumbnail="o.thumbnail"
                    :avatar="o.avatar" :describe="o.describe" :id="o.id">
        </VideoCard2>
      </div>
    </div>

    <el-pagination @current-change="handleCurrentChange"
                   :current-page="currentPage"
                   :page-size="pageSize"
                   layout=" prev, pager, next"
                   :total="totalNum">
    </el-pagination>
  </div>

</template>

<script>
import VideoCard2 from "./component/VideoCard2"
import HeaderComponent from "./component/avatar/HeaderComponent"

export default {
  name: "UserInfo",
  data() {
    return {
      user_id: parseInt(this.$route.query.user_id),
      search: this.$route,
      currentPage: 1,
      pageSize: 5,
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      video_url: "/video/Video",
      tableData: [],
      totalNum: 0,
      url2: '/api/video_api/WorksListApi'
    }
  },
  components: {
    VideoCard2, HeaderComponent
  },
  methods: {
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, user_id: this.user_id}
      let result = await this.$get2(this.url2, this.user_id, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message('失败');
      }
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.init();
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>