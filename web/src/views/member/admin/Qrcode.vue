<template>
  <div>
    <el-button>增加</el-button>
    <el-table :data="tableDate">
      <el-table-column label="桌号" prop="table_id"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button>编辑</el-button>
          <el-button>删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" style="padding: 1rem">
        <el-form-item label="取值">
          <el-input v-model="form.value"></el-input>
        </el-form-item>
        <el-form-item label="分组">
          <el-input v-model="form.group_code"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即创建</el-button>
          <el-button type="primary" @click="onCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import {QrCodeApi} from "@/api/api";

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
    init() {
      let res = this.$get2(QrCodeApi, 0, {})
      this.tableDate = res.data.data
    },
    onSubmit() {
    },
    onCancel() {
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>