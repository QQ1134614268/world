<template>
  <div>
    <div class="p_c_box-flex">
      <div class="col-9">
        <div v-for="o in tableData">
          <div>
            <a href="/video/video">
              <div>
                <img :src="file_url2+o.thumbnail" style="width: 25rem;height: 14rem;object-fit: cover;">
              </div>
            </a>
            <div>
              {{ o.describe }}
            </div>
            <div>
              {{ o.avatar }}-{{ o.username }}
            </div>
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

export default {
  name: "UserInfo2",
  data() {
    return {
      user_id: parseInt(this.$route.query.user_id),
      search: "",
      activeName: "first",
      tableData: [],
      currentPage: 1,
      pageSize: 5,
      totalNum: 0,
      url: MarketTargetListApi,
      target_url: "/video/TargetInfo",
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
      let result = await this.$get2(this.url, 0, data)
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