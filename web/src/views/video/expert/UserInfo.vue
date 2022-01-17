<template>
  <div class="col-12">
    <div class="p_c_flexbox">
      <div v-for="o in tableData" class="ratio_box block">
        <div class="ratio_box_img">
          <img :src="FilePathApi+o.thumbnail">
        </div>
        <div class="p_c_long_txt_hidden">
          {{ o.describe }}
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
import {FilePathApi, WorksListApi} from "@/api/api";

export default {
  name: "UserInfo",
  data() {
    return {
      user_id: this.$route.query.user_id,
      search: this.$route,
      currentPage: 1,
      pageSize: 10,
      FilePathApi,
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

@media screen and (max-width: 480px) {
  .ratio_box {
    width: 100%;
  }

  .ratio_box_img {
    width: 100%;
    height: 0;
    padding-bottom: 75%;
    overflow: hidden;
  }
}

@media screen and (min-width: 480px) {
  .ratio_box {
    width: 20%;
  }

  .ratio_box_img {
    width: 100%;
    height: 0;
    padding-bottom: 75%;
    /*border: #42b983 1px solid;*/
    overflow: hidden;
  }
}
</style>