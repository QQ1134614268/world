<template>
  <div class="p_c_flexbox">
    <div class="col-9 ">
      <div class="p_c_box-flex_row-center">
        <el-input v-model="search" prefix-icon="el-icon-search" :clearable=true class="col-6 p_c_box_padding"
                  placeholder="请输入搜索内容">
        </el-input>
      </div>
      <div class="p_c_flexbox container">
        <div v-for="(o, index) in tableData" :key="index" class="ratio_box block">
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
      <h3> 热度榜</h3>
      <section class="rank">
        <div v-for="(item,index) in rankData" :key="index" class="p_c_flexbox_row">
          <span class="rank_num">
            {{ index + 1 }}
          </span>
          <div style="width: 80%" class="p_c_long_txt_hidden ">
            <router-link :to="{path:VideoUrl,query: {video_id: item.id}}" class="p_c_space">
              {{ item.describe }}
            </router-link>
          </div>
        </div>
      </section>
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

      VideoUrl,
      UserInfoUrl,

      tableData: [],
      rankData: [],
    }
  },
  methods: {
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, search: this.search}
      let result = await this.$get2(MarketWorksListApi, 0, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message.error('失败');
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
.rank {

}

.rank_num {
  display: inline-block;
  width: 1.4rem;
  height: 1.4rem;
  background-size: 25px 24px;
  color: #c1abab;
}

.rank > div:nth-child(1) > span {
  color: #f30303;
}

.rank > div:nth-child(2) > span {
  color: #cb2e59;
}

.rank > div:nth-child(3) > span {
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

.container {

}

/*参考 https://blog.csdn.net/lbchenxy/article/details/100654731*/
/* 使用伪元素辅助左对齐 */
.container::after {
  content: '';
  flex: 1;
}

/*.list:last-child {*/
/*    margin-right: auto;*/
/*}*/


/*.list:not(:nth-child(4n)) {*/
/*    margin-right: calc(4% / 3);*/
/*}*/

/*方案4 */
/*!* 如果最后一行是3个元素 *!*/
/*.list:last-child:nth-child(4n - 1) {*/
/*    margin-right: calc(24% + 4% / 3);*/
/*}*/
/*!* 如果最后一行是2个元素 *!*/
/*.list:last-child:nth-child(4n - 2) {*/
/*    margin-right: calc(48% + 8% / 3);*/
/*}*/
</style>