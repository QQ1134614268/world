<template>
  <div class="p_c_flexbox">
    <div class="col-9 ">
      <div class="p_c_box-flex_row-center">
        <el-input v-model="search" prefix-icon="el-icon-search" :clearable=true class="col-6 p_c_box_padding"
                  placeholder="请输入搜索内容">
        </el-input>
      </div>
      <div class="p_c_flexbox">
        <div v-for="o in tableData">
          <div class="block">
            <router-link :to="{path:VideoUrl,query: {video_id: o.id}}">
              <div>
                <img :src="'/api/file/FileApi2?path='+o.thumbnail" style="width: 20rem;height: 11.25rem;object-fit: cover;">
              </div>
            </router-link>
            <div class="p_c_long_txt_hidden" style="width: 10rem">
              {{ o.describe }}
            </div>
            <div>
              <router-link :to="{path:UserInfoUrl,query: {video_id: o.user_id}}" class="p_c_box-flex_row-col-center ">
                <el-avatar size="small" :src="FilePathApi+o.avatar"></el-avatar>
                <span class="p_c_long_txt_hidden" style="width: 10rem">{{ o.username }}</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
      <div class="col-12 ">
        <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage"
                       :page-size="pageSize" layout=" prev, pager, next" :total="totalNum"></el-pagination>
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
          <router-link :to="{path:VideoUrl,query: {video_id: item.id}}" class="p_c_space">
            {{ item.describe }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {UserInfoUrl, VideoUrl} from "@/api/routerUrl";
import {FilePathApi, MarketWorksListApi, WorksRankListApi} from "@/api/api";

export default {
  name: "market",
  data() {
    return {
      search: "",
      currentPage: 1,
      pageSize: 10,
      totalNum: 0,

      VideoUrl: VideoUrl,
      UserInfoUrl: UserInfoUrl,

      FilePathApi,
      tableData: [],
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
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, search: this.search}
      let result = await this.$get2(MarketWorksListApi, 0, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message('失败');
      }
      let result3 = await this.$get2(WorksRankListApi, 0)
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