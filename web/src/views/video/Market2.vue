<template>
  <div class="p_c_flexbox">
    <div class="col-9 ">
      <div class="p_c_box-flex_row-center">
        <el-input v-model="search" prefix-icon="el-icon-search" :clearable=true class="col-6 p_c_box_padding"
                  placeholder="请输入搜索内容">
        </el-input>
      </div>
      <div class="col-12">
        <div v-for="o in tableData">
          <TargetComponent :username="o.username" :user_id="o.user_id" :avatar="o.avatar"
                           :title="o.title" :content="o.content" :price="o.price" :target_id="o.id"
          >
          </TargetComponent>
        </div>
      </div>
      <div class=" col-12">
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
    <div class="col-3">
      <div style="line-height: 3">
        品牌榜
      </div>
      <div v-for="(item,index) in rankData" class="p_c_flexbox_row">
        <div :class="_getRankCls(index)">
          {{ index + 1 }}
        </div>
        <div class="p_c_long_txt_hidden " style="width: 80%">
          <router-link :to="{path:'/video/TargetInfo',query: {target_id: item.id}}" class="p_c_space">
            {{ item.content }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import TargetComponent from "@/views/video/component/TargetComponent";

export default {
  name: "market",
  components: {TargetComponent},
  data() {
    return {
      search: "",
      activeName: "first",
      tableData: [],
      currentPage: 1,
      pageSize: 5,
      totalNum: 0,
      url: "/api/video_api/MarketTargetListApi",
      url3: "/api/video_api/TargetRankListApi",
      target_url: "/video/TargetInfo",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      rankData: [],
    }
  },
  methods: {
    _getRankCls(index) {
      if (index <= 2) {
        return `rank_base rank_${index}`
      } else {
        return 'rank_base'
      }
    },
    async findUser(user_id) {
      await this.$router.push({path: '/video/UserInfo2', params: {user_id: user_id}})
    },
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, search: this.search}
      let result = await this.$get2(this.url, 0, data)
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