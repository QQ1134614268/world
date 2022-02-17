<template>
  <div class="p_c_flexbox">
    <div class="col-9 ">
      <div class="p_c_box-flex_row-center">
        <el-input v-model="search" prefix-icon="el-icon-search" :clearable=true class="col-6 p_c_box_padding"
                  placeholder="请输入搜索内容">
        </el-input>
      </div>
      <div class="p_c_flexbox">
        <div v-for="o in tableData" class="ratio_box block">
          <div class="ratio_box_img p_c_box-flex_col-center">
            <router-link :to="{path:VideoUrl,query: {video_id: o.id}}">
              <img :src="o.thumbnail">
            </router-link>
          </div>
          <div class="p_c_long_txt_hidden">
            {{ o.describe }}
          </div>
          <div>
            <router-link :to="{path:UserInfoUrl,query: {user_id: o.user_id}}" class="p_c_box-flex_row-col-center ">
              <el-avatar size="small" :src="o.avatar"></el-avatar>
              <span class="p_c_long_txt_hidden" style="width: 10rem">{{ o.username }}</span>
            </router-link>
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

import {MarketWorksListApi, WorksRankListApi} from "@/api/api";
import {UserInfoUrl, VideoUrl} from "@/views/video";

export default {
  name: "market",
  data() {
    return {
      search: "",
      currentPage: 1,
      pageSize: 12,
      totalNum: 0,

      VideoUrl: VideoUrl,
      UserInfoUrl: UserInfoUrl,

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
  width: 1.4rem;
  height: 1.4rem;
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