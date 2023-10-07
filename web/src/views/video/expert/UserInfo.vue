<template>
  <div class="p_c_flexbox">
    <div class="col-1" style="background-color: rgba(238,234,234,0.95); height: 10rem">
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
        <span v-else> 登录后查看 </span>
      </div>
    </div>
    <div class="col-11">
      <div class="p_c_flexbox">
        <div v-for="o in tableData" class="ratio_box block">
          <div class="ratio_box_img">
            <img :src="o.thumbnail">
          </div>
          <div class="p_c_long_txt_hidden">
            {{ o.describe }}
          </div>
        </div>
      </div>
      <el-pagination @current-change="handleCurrentChange"
                     :current-page="currentPage"
                     :page-size="pageSize"
                     layout=" prev, pager, next"
                     :total="totalNum">
      </el-pagination>
    </div>
  </div>

</template>

<script>
import {UserApi, WorksListApi} from "@/api/api";
import {VideoUrl} from "@/views/video";
import {get2} from "@/api/http";

export default {
  name: "UserInfo",
  data() {
    return {
      user: this.$store.state.token,
      user_id: this.$route.query.user_id,
      userVO: {},
      search: this.$route,
      currentPage: 1,
      pageSize: 10,
      VideoUrl,
      tableData: [],
      totalNum: 0,
    }
  },
  methods: {
    async init() {
      let data = {page: this.currentPage, pageSize: this.pageSize, user_id: this.user_id}
      let result = await get2(WorksListApi, this.user_id, data)
      if (result.data.code === 1) {
        this.tableData = result.data.data
        this.totalNum = result.data.total
      } else {
        this.$message.error('失败');
      }
    },
    async init_user() {
      let result = await get2(UserApi, this.user_id, {})
      if (result.data.code) {
        this.userVO = result.data.data
      }
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.init();
    },
  },
  created() {
    this.init()
    this.init_user()
  }
}
</script>

<style scoped>

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