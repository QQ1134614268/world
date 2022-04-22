<template>
  <div>
    <el-table :data="tableData">
      <el-table-column label="用户" prop="username"></el-table-column>
      <el-table-column label="主题" prop="describe"></el-table-column>
      <el-table-column label="视频" prop="thumbnail">
        <template slot-scope="scope">
          <router-link :to="{path:VideoUrl,query: {video_id: scope.row.id}}">
            <el-image :src="scope.row.thumbnail" class="img"></el-image>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-select v-model="scope.row.state" placeholder="请选择" @change="handleEdit(scope.row.id, scope.row.state)">
            <el-option v-for="(item,index) in ReviewEnum" :key="index" :label="item.value" :value="item.code"></el-option>
          </el-select>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {ReviewWorksApi} from "@/api/api";
import {getEnum} from "@/api/enum_api";
import {REVIEW_ENUM} from "@/api/config";
import {VideoUrl} from "@/views/video";

export default {
  name: "Approve",
  data() {
    return {
      tableData: [],
      ReviewEnum: [],
      VideoUrl
    }
  },
  methods: {
    async init() {
      let res = await this.$get2(ReviewWorksApi)
      this.tableData = res.data.data
      this.ReviewEnum = await getEnum({group_code: REVIEW_ENUM})
    },
    async handleEdit(id, state) {
      await this.$putJson2(ReviewWorksApi, id, {state: state})
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
.img{
  width: 5rem;
}
</style>
