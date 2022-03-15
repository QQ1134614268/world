<template>
  <div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="商品图片">
        <el-upload
            class="avatar-uploader"
            :action="FileApi"
            :show-file-list="false"
            :on-success="uploadFileSuccess"
            style="width:10rem;  height:10rem ">
          <img :key="form.images" v-if="form.images" :src="form.images" style="width:10rem;
                 height:10rem;object-fit: cover">
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
  </div>
</template>

<script>

import {FileApi, GoodsApi} from "@/api/api";

export default {
  name: "GoodsEdit",
  data() {
    return {
      FileApi,
      dialogVisible: false,
      form: {images: ""},
      tableData: [],
      store_id: 1,
      GoodsApi
    };
  },

  methods: {
    uploadFileSuccess(res) {
      this.form.images = res.data;
    },
    async init() {
      let data = {
        store_id: this.store_id
      }
      let response = await this.$get2(GoodsApi, 0, data);
      this.tableData = response.data.data
    },
    async onSubmit() {
      this.dialogVisible = false
      this.form.store_id = this.store_id
      let response = await this.$ppJson(GoodsApi, this.form.id, this.form);
      if (response.data.code != 1) {
        this.$message.success('操作成功');
      } else {
        this.$message.success('操作成功');
      }
      await this.init()
    },
    cancel() {
      this.dialogVisible = false
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>