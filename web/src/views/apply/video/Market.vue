<template>
  <div class="p_c_flexbox">
    <div class="col-9 ">
      <div class="p_c_box-flex_row-center">
        <el-input v-model="search" prefix-icon="el-icon-search" :clearable=true class="col-6 p_c_box_padding"
                  placeholder="请输入搜索内容">
        </el-input>
      </div>
      <div class="p_c_flexbox">
        <div v-for="o in tableData" class="col-3">
          <VideoCard :username="o.username" :user_id="o.user_id" :create_time="o.create_time" :thumbnail="o.thumbnail"
                     :avatar="o.avatar" :describe="o.describe" :id="o.id">
          </VideoCard>
        </div>
      </div>
      <div class="col-12 ">
        <el-pagination @size-change="handleSizeChange"
                       @current-change="handleCurrentChange"
                       :current-page="currentPage"
                       :page-size="pageSize"
                       layout=" prev, pager, next"
                       :total="totalNum"
        >
        </el-pagination>
      </div>
    </div>
    <div class="col-3">
      <div style="line-height: 3">
        热度榜
      </div>
      <div v-for="(item,index) in rankData" class="p_c_flexbox_row">
        <div :class="_getRankCls(index)">
          {{ index + 1 }}
        </div>
        <div style="width: 80%" class="p_c_long_txt_hidden ">
          <router-link :to="{name:'/video/Video',query: {video_id: item.id}}" class="p_c_space">
            {{ item.describe }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VideoCard from "./component/VideoCard"

export default {
  name: "market",
  data() {
    return {
      search: "",
      currentPage: 1,
      pageSize: 6,
      video_url: "/video/Video",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      tableData: [],
      totalNum: 0,
      url2: '/api/video_api/MarketWorksListApi',
      url3: '/api/video_api/WorksRankListApi',
      rankData: [],
    }
  },
  components: {
    VideoCard,
  },
  methods: {
    _getRankCls(index) {
      if (index <= 2) {
        return `rank_base rank_${index}`
      } else {
        return 'rank_base'
      }
    },
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, search: this.search}
      let result = await this.$get2(this.url2, 0, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message('失败');
      }
      let result3 = await await this.$get2(this.url3, 0)
      this.rankData = result3.data.data
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.init();
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.init();
    },
    async findUser(user_id) {
      await this.$router.push({path: '/video/UserInfo', params: {user_id: user_id}})
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
.rank_base {
  width: 2.4rem;
  height: 2.4rem;
  background-size: 25px 24px;
  color: #c1abab;
}

/*rank_base rank_0*/
.rank_0 {
  color: #f30303;
}

.rank_1 {
  color: #cb2e59;
}

.rank_2 {
  color: #ac4d60;
}

</style>