<template>
  <div style="display: flex;">
    <div style="width: 20rem">
      <div>
        <el-button @click="showCtl('a')"> 店铺列表</el-button>
      </div>
      <div>
        <el-button @click="showCtl('b')"> 创建店铺</el-button>
      </div>
    </div>
    <div style="width: 100%">
      <div v-if="ctl.a">
        <!--   店铺列表     -->
        <el-table :data="tableData" style="width: 100%">
          <el-table-column prop="name" label="店铺名" width="180"></el-table-column>
          <el-table-column prop="create_time" label="创建时间"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" @click="info(scope.$index, scope.row)">店铺详情</el-button>
              <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div v-if="ctl.b">
        <!--      创建店铺  -->
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="店铺名">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="form.password" :value="null"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">完成</el-button>
            <el-button @click="cancel">取消</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div v-if="ctl.info">
        <div>
          <a :href="'/member/Goods?store_id='+store_id"> 商品传送门</a>
        </div>
        <div>
          <a :href="'/member/Member?store_id='+store_id"> 会员传送门</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Store",
  data() {
    return {
      form: {},
      tableData: [],
      ctl: {
        a: true
      },
      store_id: ""
    };
  },
  methods: {
    showCtl(arg) {
      this.ctl = {}
      this.ctl[arg] = true
    },
    async createStore() {
      let url = "/api/member/StoreApi"
      let response = await this.$postJson(url, this.form);
      if (response.data.code != 1) {
        alert("2")
        return
      }
      this.store = response.data.data
      await this.$router.push({path: '/member/StoreList'})
    },
    async getStoreList() {
      let url = "/api/member/StoreListApi"
      let response = await this.$get(url);
      if (response.data.code != 1) {
        alert("2")
        return
      }
      this.tableData = response.data.data
    },
    info(index, row) {
      this.store_id = row.id
      this.showCtl('info')
    },
    async handleEdit(index, row) {
      this.showCtl('b')
      this.form = row
    },
    async handleDelete(index, row) {
      let url = "/api/member/StoreApi" + "/" + row.id
      let response = await this.$deleteJson(url);
      if (response.data.code != 1) {
        return
      }
      this.tableData.splice(index, 1)
    },
    async onSubmit() {
      let url = "/api/member/StoreApi"
      let response = await this.$ppJson(url, this.form, this.form.id);
      if (response.data.code != 1) {
        this.$message('操作失败');
      } else {
        this.$message('操作成功');
      }
      await this.getStoreList()
      this.showCtl("a")
      this.form = {}
    },
  },
  created() {
    this.getStoreList()
  }
}
</script>

<style scoped>


</style>
