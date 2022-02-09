<template>
  <div>
    会员列表
    <div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="img" label="头像"></el-table-column>
        <el-table-column prop="username" label="用户名" width="180"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div>
      <!--      <el-dialog>-->
      <!--      </el-dialog>-->
    </div>
  </div>
</template>

<script>

import {StoreMemberListApi} from "@/api/api";

export default {
  name: "Member",
  data() {
    return {
      tableData: [],
      dialogVisible: "",
    };
  },
  methods: {
    async getStoreMember() {
      let data = {
        store_id: this.store_id,
      }
      let response = await this.$get2(StoreMemberListApi, 0, data);
      if (response.data.code != 1) {
        return
      }
      this.tableData = response.data.data
    },
  },
  created() {
    this.getStoreMember()
  }
}
</script>

<style scoped>

</style>