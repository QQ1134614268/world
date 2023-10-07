<template>
  <div>
    <el-button @click="form={};dialogVisible=true">增加</el-button>
    <el-table :data="tableDate">
      <el-table-column label="桌号" prop="table_id"></el-table-column>
      <el-table-column label="二维码" prop="qr_code"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button>编辑</el-button>
          <el-button>删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" style="padding: 1rem">
        <el-form-item label="桌号">
          <el-input v-model="form.table_id"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button type="primary" @click="onCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import {QrCodeApi} from "@/api/api";
import {get2, ppJson} from "@/api/http";

export default {
  name: "Qrcode",
  data() {
    return {
      tableDate: [],
      QrCodeApi,
      form: {},
      dialogVisible: false,
    }
  },
  methods: {
    async init() {
      let res = await get2(QrCodeApi, 0, {})
      for (let i = 0; i < res.data.data.length; i++) {
        this.tableDate.push(res.data.data[i].url_dic)
      }
    },
    async onSubmit() {
      let res = await ppJson(QrCodeApi, this.form.id, {url_dic: this.form})
      if (res.data.code == 1) {
        this.dialogVisible = false
        // this.$message.info("操作成功")
        this.$message.success('操作成功');
        await this.init()
      }
    },
    onCancel() {
      this.dialogVisible = false
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>