<template>
  <div class="p_c_flexbox">
    <div class="col-9 ">
      <div class="p_c_box-flex_row-center">
        <el-input v-model="search" prefix-icon="el-icon-search" :clearable=true class="col-6 p_c_box_padding"
                  placeholder="请输入搜索内容">
        </el-input>
      </div>
      <div>
        <div v-for="(o, index) in tableData">
          <div class="block">
            <div class="art_title">
              <router-link :to="{path:target_url,query: {target_id: o.id}}">
                {{ o.title }}
              </router-link>
            </div>
            <div class="art_body"> {{ o.content }}</div>
            <div class="art_note">
              <router-link :to="{path:'/video/UserInfo2',query: {user_id: o.user_id}}"
                           class="p_c_box-flex_row-col-center">
                <el-avatar :src="o.avatar"></el-avatar>
                <span class="p_c_long_txt_hidden" style="width: 10rem">{{ o.username }}</span>
              </router-link>
            </div>
          </div>

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
          <router-link :to="{path:TargetInfoUrl,query: {target_id: item.id}}" class="p_c_space">
            {{ item.content }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {MarketTargetListApi, TargetRankListApi} from "@/api/api";
import {TargetInfoUrl} from "@/views/video";

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
      target_url: TargetInfoUrl,
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
      let result = await this.$get2(MarketTargetListApi, 0, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message('失败');
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