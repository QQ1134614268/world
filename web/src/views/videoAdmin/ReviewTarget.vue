<template>
  <div>
    <div class="p_c_flexbox">
      <div class="col-3">
        <span>用户:</span>
        <el-autocomplete class="inline-input" v-model="user_name" placeholder="请输入用户名">
        </el-autocomplete>
      </div>
      <div class="col-6">
        <span>发布时间:</span>
        <el-date-picker :value-format=DATE_FMT v-model="dateRange"
                        type="daterange" range-separator="至 " start-placeholder="开始日期" end-placeholder="结束日期">
        </el-date-picker>
      </div>
      <div class="col-3">
        <span>状态:</span>
        <el-select v-model="state">
          <el-option v-for="(item,index) in ReviewEnum" :key="index" :label="item.value" :value="item.code"></el-option>
        </el-select>
      </div>
      <div class="col-3">
        <el-button type="primary" @click="init">搜索</el-button>
      </div>
    </div>
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
      <el-table-column label="时间" prop="create_time"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-select v-model="scope.row.state" placeholder="请选择" @change="handleEdit(scope.row.id, scope.row.state)">
            <el-option v-for="(item,index) in ReviewEnum" :key="index" :label="item.value"
                       :value="item.code"></el-option>
          </el-select>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {ReviewTargetApi} from "@/api/api";
import {getEnum} from "@/api/enum_api";
import {DATE_FMT, REVIEW_ENUM} from "@/api/config";
import {TargetInfoUrl} from "@/views/video";
import {getDateY_M_D} from "@/api/util";
import {putJson2} from "@/api/http";

export default {
  name: "ReviewTarget",
  data() {
    return {
      tableData: [],
      ReviewEnum: [],
      TargetInfoUrl,
      DATE_FMT,
      dateRange: [getDateY_M_D(), getDateY_M_D()],
      state: "NONE",
      user_name: ""
    }
  },
  methods: {
    async init() {
      let data = {
        user_name: this.user_name,
        state: this.state,
        startDate: this.dateRange && this.dateRange.length > 0 ? this.dateRange[0] : "",
        endDate: this.dateRange && this.dateRange.length > 1 ? this.dateRange[1] : "",
      }
      let res = await get2(ReviewTargetApi, 0, data)
      this.tableData = res.data.data
      this.ReviewEnum = await getEnum({group_code: REVIEW_ENUM})
    },
    async handleEdit(id, state) {
      await putJson2(ReviewTargetApi, id, {state: state})
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>