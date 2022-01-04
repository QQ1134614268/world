<template>
  <div class="col-12">
    <div class="p_c_flexbox">
      <div v-for="o in tableData">
        <div class="block">
          <div>
            <img :src="file_url2+o.thumbnail" style="width: 20rem;height: 11.25rem;object-fit: cover;">
          </div>
          <div class="p_c_long_txt_hidden">
            {{ o.describe }}
          </div>
        </div>
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
import {VideoUrl} from "@/api/routerUrl";
import {WorksListApi} from "@/api/api";

export default {
  name: "UserInfo",
  data() {
    return {
      user_id: this.$route.query.user_id,
      search: this.$route,
      currentPage: 1,
      pageSize: 10,
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      VideoUrl: VideoUrl,
      tableData: [],
      totalNum: 0,
    }
  },
  methods: {
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, user_id: this.user_id}
      let result = await this.$get2(WorksListApi, this.user_id, data)
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