<template>
  <div>
    <el-form ref="form" :model="form" label-width="5rem">
      <el-form-item label="枚举值">
        <el-input v-model="form.value"></el-input>
      </el-form-item>
      <el-form-item label="枚举值">
        <el-input v-model="form.label"></el-input>
      </el-form-item>
      <el-form-item label="编码">
        <el-input v-model="form.code"></el-input>
      </el-form-item>
      <el-form-item label="父编码">
        <el-input v-model="form.parent_code"></el-input>
      </el-form-item>
      <el-form-item label="备注">
        <el-input v-model="form.comment"></el-input>
      </el-form-item>
      <el-form-item label="分类">
        <el-input v-model="form.group_code"></el-input>
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
import {get2, ppJson} from "@/api/http";

export default {
  name: "GoodsEdit",
  data() {
    return {
      FileApi,
      store_id: this.$route.query.store_id,
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
      this.form.images = res.data;
    },
    async init() {
      let data = {
        store_id: this.store_id
      }
      let response = await get2(GoodsApi, 0, data);
      this.tableData = response.data.data
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