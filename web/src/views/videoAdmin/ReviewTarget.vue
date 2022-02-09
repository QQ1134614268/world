<template>
  <div>
    <el-table :data="tableData">
      <el-table-column label="用户" prop="username"></el-table-column>
      <el-table-column label="主题" prop="title"></el-table-column>
      <el-table-column label="内容">
        <template slot-scope="scope">
          <router-link :to="{path:TargetInfoUrl,query: {target_id: scope.row.id}}">
            {{ scope.row.content }}
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="价格" prop="price"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-select v-model="scope.row.state" placeholder="请选择" @change="handleEdit(scope.row.id, scope.row.state)">
            <el-option v-for="item in ReviewEnum" :label="item.value" :value="item.code"></el-option>
          </el-select>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {ReviewTargetApi, ReviewWorksApi} from "@/api/api";
import {getEnum} from "@/api/enum_api";
import {REVIEW_ENUM} from "@/api/config";
import {TargetInfoUrl} from "@/api/routerUrl";

export default {
  name: "ReviewTarget",
  data() {
    return {
      tableData: [],
      ReviewEnum: [],
      TargetInfoUrl
    }
  },
  methods: {
    async init() {
      let res = await this.$get2(ReviewTargetApi)
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

</style>