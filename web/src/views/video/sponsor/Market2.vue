<template>
  <div class="p_c_flexbox">
    <div class="col-9  p_c_box-flex_col-center">
      <div class="p_c_box-flex_col-center  col-8">
        <el-input v-model="search" prefix-icon="el-icon-search" :clearable=true class="p_c_box_padding"
                  placeholder="请输入搜索内容">
        </el-input>
        <BoxCol class="t_list">
          <BoxCol v-for="(o, index) in tableData" :key="index" class="target">
            <router-link :to="{path:TargetInfoUrl,query: {target_id: o.id}}" class="target_title">
              {{ o.title }}
            </router-link>
            <div class="target_content"> {{ o.content }}</div>
            <router-link :to="{path:UserInfo2,query: {user_id: o.user_id}}"
                         class="p_c_box-flex_row-col-center t_avatar">
              <el-avatar :src="o.avatar" :size=16></el-avatar>
              <span class="p_c_long_txt_hidden name">{{ o.username }}</span>
            </router-link>
          </BoxCol>
        </BoxCol>

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
      <h3> 品牌榜</h3>
      <section class="rank">
        <div v-for="(item,index) in rankData" :key="index" class="p_c_flexbox_row">
        <span class="rank_num">
          {{ index + 1 }}
        </span>
          <div class="p_c_long_txt_hidden " style="width: 80%">
            <router-link :to="{path:TargetInfoUrl,query: {target_id: item.id}}" class="p_c_space">
              {{ item.content }}
            </router-link>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import {MarketTargetListApi, TargetRankListApi} from "@/api/api";
import {TargetInfoUrl, UserInfo2} from "@/views/video";

export default {
  name: "market",
  data() {
    return {
      TargetInfoUrl,
      search: "",
      tableData: [],
      currentPage: 1,
      pageSize: 5,
      totalNum: 0,
      rankData: [],
      UserInfo2
    }
  },
  methods: {
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, search: this.search}
      let result = await this.$get2(MarketTargetListApi, 0, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message.error('失败');
      }
      let result3 = await this.$get2(TargetRankListApi, 0)
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

.t_list {
  width: 100%;
}

.target_title {
  color: black;
  font-size: 1.2rem;
  line-height: 1.8rem;
}

.target_content {
  padding-top: 0.5rem;
}

.target {
  box-shadow: 0 2px 10px 0 rgb(0 0 0 / 10%);
  margin-bottom: 1rem;
  margin-left: 1rem;
  line-height: 1.6rem;
  padding: 1rem;
  border-radius: 0.8rem;
  border-collapse: separate;
}

.t_avatar {
  padding-top: 0.5rem;
}

.name {
  width: 10rem;
  color: black;
}
</style>