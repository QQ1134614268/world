<template>
  <div>
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

export default {
  name: "Member",
  data() {
    return {
      tableData: [],
      dialogVisible: "",
    };
  },
  methods: {
    showCtl(arg = "a") {
      this.ctl = {}
      this.ctl[arg] = true
    },
    async handleDelete(index, row) {
      let url = "api/goods" + "/" + row.id
      let response = await this.$deleteJson(url);
      if (response.data.code != 1) {
        return
      }
      this.tableData.splice(index, 1)
    },
    async getStoreMember() {
      let url = "/api/member/StoreMemberListApi"
      let data = {
        store_id: this.store_id,
      }
      let response = await this.$get(url, data);
      if (response.data.code != 1) {
        alert("2")
        return
      }
      this.tableData = response.data.data
    },
    async addStoreMember() {
      this.$route.params
      let url = "/api/member/StoreMemberApi"
      let data = {
        user_id: this.userVO.id,
        store_id: this.store_id,
      }
      let response = await this.$postJson(url, data);
      this.userVO = response.data.data
      this.dialogVisible = false
    },
    async searchUser() {
      let url = "/api/user_api/getUserByName"
      let data = {
        username: this.user_name,
      }
      let response = await this.$get(url, data);
      if (response.data.code == 1) {
        this.userVO = response.data.data
        this.dialogVisible = true
      } else {
        this.$message("没有该用户")
      }

    },
  },
  created() {
    this.getStoreMember()
  }
}
</script>

<style scoped>

</style>