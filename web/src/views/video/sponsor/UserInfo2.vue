<template>
  <div>
    <div class="p_c_box-flex">
      <div class="col-9">
        <div v-for="o in tableData">
          <div class="art_title">
            {{ o.title }}
          </div>
          <div class="art_body">
            {{ o.content }}
          </div>
        </div>
        <div>
          <el-pagination @size-change="handleSizeChange"
                         @current-change="handleCurrentChange"
                         :current-page="currentPage"
                         :page-sizes="[5, 10, 20, 50]"
                         :page-size="pageSize"
                         layout="prev, pager, next"
                         :total="totalNum">
          </el-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import UserAvatarIComponent from "@/views/video/component/UserAvatarIComponent";
import {MarketTargetListApi} from "@/api/api";
import {TargetInfoUrl, VideoUrl} from "@/api/routerUrl";

export default {
  name: "UserInfo2",
  data() {
    return {
      user_id: this.$route.query.user_id,
      VideoUrl: VideoUrl,
      search: "",
      tableData: [],
      currentPage: 1,
      pageSize: 5,
      totalNum: 0,
      target_url: TargetInfoUrl,
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }
  },
  components: {
    UserAvatarIComponent,
  },
  methods: {
    async init() {
      let data = {
        page: this.currentPage,
        pageSize: this.pageSize,
        user_id: this.user_id,
        search: this.search
      }
      let result = await this.$get2(MarketTargetListApi, 0, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message('失败');
      }
    },
    handleSizeChange(val) {
      console.log('每页' + val + '条');
      this.pageSize = val;
      this.init();
    },
    handleCurrentChange(val) {
      console.log('当前页:' + val);
      this.currentPage = val;
      this.init();
    },
  },
  watch: {
    search: function (val, oldVal) {
      this.init();
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>