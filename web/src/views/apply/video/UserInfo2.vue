<template>
  <div>
    <div class="p_c_box-flex">
      <div class="col-9">
        <HeaderComponent :user_id="user_id"></HeaderComponent>
        <div v-for="o in tableData">
          <TargetComponent :username="o.username" :user_id="o.user_id" :avatar="o.avatar"
                           :title="o.title" :content="o.content" :price="o.price" :target_id="o.id"
          >
          </TargetComponent>
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
import HeaderComponent from "./component/avatar/HeaderComponent"
import TargetComponent from "./component/TargetComponent"

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
      url: "/api/video_api/MarketTargetListApi",
      target_url: "/video/TargetInfo",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }
  },
  components: {
    HeaderComponent,
    TargetComponent
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