<template>
  <div>
    <div class="p_c_flexbox" style="justify-content: space-between">
      <span>我的发布</span>
      <span>
        <el-button @click="dialogVisible=true;this.form={}">我要发布</el-button>
      </span>
    </div>
    <el-table ref="dormitoryTable" :data="tableData" tooltip-effect="dark" stripe>
      <el-table-column label="主题" prop="title"></el-table-column>
      <el-table-column label="描述" prop="content"></el-table-column>
      <el-table-column label="佣金" prop="price"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" :rules="rules" label-width="8rem" style="padding: 1rem">
        <el-form-item prop="title" label="主题" :required="true">
          <el-input v-model="form.title"></el-input>
        </el-form-item>
        <el-form-item prop="content" label="描述" :required="true">
          <el-input v-model="form.content"></el-input>
        </el-form-item>
        <el-form-item prop="price" label="佣金" :required="true">
          <el-input v-model="form.price" @input="form.price=form.price.replace(/[^\d.]/g,'')"></el-input>
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
import {TargetApi, TargetListApi} from "@/api/api";
import {getUserIdByToken} from "@/api/util";
import {deleteJson2, get2, postJson2, putJson2} from "@/api/http";

export default {
  name: "Target",
  data() {
    return {
      dialogVisible: false,
      user_id: getUserIdByToken(),
      form: {},
      tableData: [],
      rules: {
        title: [
          {required: true, message: '不能为空', trigger: 'blur'}
        ],
        content: [
          {required: true, message: '不能为空', trigger: 'blur'}
        ],
        price: [
          {required: true, message: '不能为空', trigger: 'blur'}
        ],
      }
    }
  },
  methods: {
    async handleDelete(index, row) {
      let result = await deleteJson2(TargetApi, row.id)
      if (result.data.code === 1) {
        this.$message.success('删除成功!');
        this.tableData.splice(index, 1)
      } else {
        this.$message.error('操作失败');
      }
    },
    async onSubmit() {
      let result;
      if (this.form.id) {
        result = await putJson2(TargetApi, this.form.id, this.form)
      } else {
        result = await postJson2(TargetApi, 0, this.form)
      }
      if (result.data.code === 1) {
        this.$message.success('操作成功');
      } else {
        this.$message.error('操作失败');
      }
    },
    onCancel() {
      this.dialogVisible = false
    },
    handleEdit(index, row) {
      this.form = row
      this.dialogVisible = true
    },
    async init() {
      let result = await get2(TargetListApi, 0, {user_id: this.user_id})
      if (result.data.code === 1) {
        this.tableData = result.data.data
      } else {
        this.$message.error('失败');
      }
    },

  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
@media only screen and (max-width: 768px) {
  /deep/ .el-dialog {
    width: 100%;
  }
}
</style>