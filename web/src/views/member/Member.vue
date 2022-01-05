<template>
  <div style="display: flex;">
    <div style="width: 20rem">
      <div>
        <el-button @click="showCtl('a')"> 会员列表</el-button>
      </div>
      <div>
        <el-button @click="showCtl('add')"> 添加会员</el-button>
      </div>
      <div>
        <!--        todo-->
        <a href=""> 上一级 </a>
      </div>
    </div>
    <div style="width: 100rem">
      <div v-if="ctl.a">
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
      <div v-if="ctl.b">
      </div>
      <div v-if="ctl.add">
        <input v-model.number="user_name"></input>
        <el-button type="success" @click="searchUser">查找用户</el-button>
        <div v-if="dialogVisible">
          {{ this.userVO.username }}
          <el-button type="success" @click="addStoreMember">添加会员</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";

export default {
  name: "Member",
  data() {
    return {
      ctl: {
        a: true
      },
      tableData: [],
      user_name: "",
      userVO: "",
      dialogVisible: "",
      store_id: this.$route.query.store_id
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