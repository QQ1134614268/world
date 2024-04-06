<template>
  <div>
    <el-form ref="form" :model="form" label-width="5rem">
      <el-form-item label="商品图片">
        <el-upload
            class="avatar-uploader"
            :action="FileApi"
            :show-file-list="false"
            :on-success="uploadFileSuccess"
            style="width:10rem;  height:10rem ">
          <img :key="form.image" v-if="form.image" :src="form.image" style="width:10rem;
                 height:10rem;object-fit: cover">
          <i v-else class="el-icon-plus avatar-uploader-icon" style="width:10rem;  height:10rem "></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="商品名">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="商品价格">
        <el-input v-model="form.price"></el-input>
      </el-form-item>
      <el-form-item label="商品分类">
        <el-select v-model="form.type_id" placeholder="请选择" @change="init">
          <el-option v-for="(item,index) in types" :label="item.label" :value="item.value" :key="index"></el-option>
        </el-select>
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
import {enum_api_page, FileApi, GoodsApi} from "@/api/api";
import {get2, getJson3, ppJson} from "@/api/http";

export default {
  name: "GoodsEdit",
  data() {
    return {
      FileApi,
      store_id: this.$route.query.store_id,
      types: [],
    };
  },
  props: {
    form: {},
    dialogForm: {
      dialogVisible: true,
    },
  },
  methods: {
    uploadFileSuccess(res) {
      this.form.image = res.data;
    },
    async init() {
      let data = {
        store_id: this.store_id
      }
      let response = await get2(GoodsApi, 0, data);
      this.tableData = response.data.data
      let res2 = await getJson3(enum_api_page, {group_code: "FOOD_ENUM"})
      this.types = res2.data.data
    },
    async onSubmit() {
      this.form.store_id = this.store_id
      let response = await ppJson(GoodsApi, this.form.id, this.form);
      if (response.data.code === 1) {
        this.$message.success('操作成功');
        this.cancel()
      } else {
        this.$message.error('服务器异常');
      }
      await this.init()
    },
    cancel() {
      this.form = {}
      this.dialogForm.dialogVisible = false
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>