<template>
  <div class="p_c_flexbox">
    <div class="col-1">
      <div>
        <el-avatar :src="userVO.avatar" :key="userVO.avatar"></el-avatar>
        <span>{{ userVO.username }} </span>
      </div>
      <div>
        {{ userVO.describe || '还没有签名呦!' }}
      </div>
      <div>
        <span>微信</span>
        <span v-if="user"> {{ userVO.wechat_number }} </span>
        <span v-else style="color: gainsboro"> 登录后查看 </span>
      </div>
    </div>
    <div class="col-11">
      <div v-for="o in tableData">
        <div class="block">
          <div class="art_title">
            {{ o.title }}
          </div>
          <div class="art_body">
            {{ o.content }}
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
</template>

<script>

import {MarketTargetListApi, UserApi} from "@/api/api";
import {TargetInfoUrl, VideoUrl} from "@/views/video";
import {get2} from "@/api/http";

export default {
  name: "UserInfo2",
  data() {
    return {
      user_id: this.$route.query.user_id,
      userVO: {},
      VideoUrl,
      search: "",
      tableData: [],
      currentPage: 1,
      pageSize: 5,
      totalNum: 0,
      target_url: TargetInfoUrl,
    }
  },
  methods: {
    async init_user() {
      let result = await get2(UserApi, this.user_id, {})
      if (result.data.code) {
        this.userVO = result.data.data
      }
    },
    async init() {
      let data = {
        page: this.currentPage,
        pageSize: this.pageSize,
        user_id: this.user_id,
        search: this.search
      }
      let result = await get2(MarketTargetListApi, 0, data)
      if (result.data.code == 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message.error('失败');
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
  computed: {
    user() {
      return this.$store.state.userInfo
    }
  },
  watch: {
    search: function (val, oldVal) {
      this.init();
    }
  },
  created() {
    this.init()
    this.init_user()
  }
}
</script>

<style scoped>

</style>