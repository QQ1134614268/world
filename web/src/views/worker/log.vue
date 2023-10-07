<template>
  <div>
    操作日志
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="create_time" label="时间"></el-table-column>
      <el-table-column prop="message" label="操作"></el-table-column>
    </el-table>
    <el-pagination hide-on-single-page
                   :current-page="currentPage" :page-size="pageSize" :total="totalNum"
                   layout=" prev, pager, next">
    </el-pagination>
  </div>
</template>

<script>
import {LogApi} from "@/api/api";
import {get2} from "@/api/http";

export default {
  name: "log",
  data() {
    return {
      url: "",
      data: [],
      //分页
      currentPage: 1,
      pageSize: 6,
      totalNum: 0,
    }
  },
  methods: {
    async init() {
      let data = {
        page: this.currentPage,
        pageSize: this.pageSize,
      }
      let res = await get2(LogApi, 0, data)
      if (res.data.code != 1) {
        this.$message.error('服务器异常');
        return
      }
      this.data = res.data.data
    }
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>