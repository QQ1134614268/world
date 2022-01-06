<template>
  <div>
    <div>
      商品列表
      <el-button @click="form={}; dialogVisible=true"> 新增</el-button>
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
    <el-dialog :title="form.id?'编辑':'新增'" :visible="dialogVisible">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="商品图片">
          <el-upload
              class="avatar-uploader"
              :action="FileApi"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              style="width:10rem;  height:10rem ">
            <!--                          :before-upload="beforeAvatarUpload"-->

            <img :key="imageUrl" v-if="imageUrl" :src="FilePathApi+imageUrl" style="width:10rem;
                 height:10rem ;object-fit: cover"
            >
            <i v-else class="el-icon-plus avatar-uploader-icon" style="width:10rem;  height:10rem "></i>
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
import {FileApi, FilePathApi} from '@/api/api';

export default {
  name: "Goods",
  data() {
    return {
      FileApi,
      FilePathApi,
      dialogVisible: false,
      form: {},
      imageUrl: "",
      tableData: [],
      store_id: 1,
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      this.imageUrl = res.data;
    },
    async init() {
      let url = "/api/goods_api/GoodsApi"
      let data = {
        storeId: 1
      }
      let response = await this.$get2(url, 1, data);
      this.tableData = response.data.data
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
      let url = "/api/goods_api/GoodsApi"
      this.form.store_id = this.store_id
      let response = await this.$ppJson(url, this.form.id, this.form);
      if (response.data.code != 1) {
        this.$message('操作失败');
      } else {
        this.$message('操作成功');
      }
      this.dialogVisible = false
      this.init()
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