<template>
  <div>
    <div>
      商品列表
      <el-button @click="this.form={}; this.dialogVisible=true"> 新增</el-button>
    </div>
    <div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="name" label="商品图片" width="180"></el-table-column>
        <el-table-column prop="name" label="商品名" width="180"></el-table-column>
        <el-table-column prop="price" label="商品价格"></el-table-column>
        <el-table-column prop="describe" label="商品描述"></el-table-column>
        <el-table-column prop="create_time" label="上架时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <el-dialog :title="this.form.id?'编辑':'新增'" :visible="dialogVisible">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="商品图片">
          <el-upload>
            <el-input v-model="form.name"></el-input>
          </el-upload>
        </el-form-item>
        <el-form-item label="商品名">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="商品价格">
          <el-input v-model="form.price" :value="null"></el-input>
        </el-form-item>
        <el-form-item label="商品描述">
          <el-input v-model="form.describe"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">完成</el-button>
          <el-button @click="cancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>

export default {
  name: "Goods",
  data() {
    return {
      dialogVisible: false,
      form: {},
      tableData: []
    };
  },
  methods: {
    async init() {
      let url = "/api/goods_api/GoodsApi"
      let data = {
        storeId: 1
      }
      let response = await this.$get2(url, 1, data);
      this.data = response.data.data
    },
    async handleEdit(index, row) {
      this.form = row
      this.dialogVisible = true
    },
    async handleDelete(index, row) {
      let url = "api/goods" + "/" + row.id
      let response = await this.$deleteJson(url);
      if (response.data.code != 1) {
        return
      }
      this.tableData.splice(index, 1)
    },
    async onSubmit() {
      let url = "api/goods"
      this.form.store_id = this.store_id
      let response = await this.$ppJson(url, this.form.id, this.form);
      if (response.data.code != 1) {
        this.$message('操作失败');
      } else {
        this.$message('操作成功');
      }
      await this.getGoodsList()
      this.form = {}
    },
    cancel() {

    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>