<template>
  <!--  发布 招聘信息-- 类似猪八戒  boss  -->
  <div>
    <HeaderComponent :user_id="user_id"></HeaderComponent>
    <el-tabs v-model="activeName">
      <el-tab-pane label="历史发布" name="first">
        <el-table ref="dormitoryTable" :data="tableData" tooltip-effect="dark" stripe>
          <el-table-column label="主题" prop="title"></el-table-column>
          <el-table-column label="描述" prop="content"></el-table-column>
          <el-table-column label="佣金" prop="price"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">编辑
              </el-button>
              <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="发布" name="second">
        <el-form ref="form" :model="form" :rules="rules" label-width="8rem" style="padding: 1rem">
          <el-form-item prop="title" label="主题" :required="true">
            <el-input v-model="form.title"></el-input>
          </el-form-item>
          <el-form-item prop="content" label="描述" :required="true">
            <el-input v-model="form.content"></el-input>
          </el-form-item>
          <el-form-item prop="price" label="佣金2" :required="true">
            <el-input v-model="form.price" @input="form.price=form.price.replace(/[^\d.]/g,'')"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button type="primary" @click="onCancel">取消</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
    <el-dialog title="编辑" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form2" :rules="rules" label-width="8rem" style="padding: 1rem">
        <el-form-item prop="title" label="主题" :required="true">
          <el-input v-model="form2.title"></el-input>
        </el-form-item>
        <el-form-item prop="content" label="描述" :required="true">
          <el-input v-model="form2.content"></el-input>
        </el-form-item>
        <el-form-item prop="price" label="佣金" :required="true">
          <el-input v-model="form2.price" @input="form.price=form.price.replace(/[^\d.]/g,'')"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit2">保存</el-button>
          <el-button type="primary" @click="onCancel2">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import HeaderComponent from "./component/avatar/HeaderComponent"
import jwt_decode from "jwt-decode";

export default {
  name: "Target",
  components: {
    HeaderComponent
  },
  data() {
    return {
      dialogVisible: false,
      user_id: jwt_decode(localStorage.getItem("token"))["id"],
      tables: [],
      TAB_FIRST: "first",
      TAB_SECOND: "second",
      activeName: "first",
      form: {title: ""},
      form2: {},
      url: "/api/video_api/TargetApi",
      api_url: "/api/video_api/TargetListApi",
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
      let result = await this.$deleteJson2(this.url, row.id)
      if (result.data.code == 1) {
        this.$message('删除成功!');
        this.tableData.splice(index, 1)
      } else {
        this.$message('');
      }
    },
    async onSubmit() {
      let result = await this.$postJson2(this.url, 0, this.form)
      if (result.data.code == 1) {
        this.activeName = this.TAB_FIRST
        this.form = {}
        // await this.$router.push({path: 'video/works'})
      } else {
        this.$message('失败');
      }
    },
    onCancel() {
      this.form = {}
      this.activeName = this.TAB_FIRST
    },
    handleEdit(index, row) {
      this.dialogVisible = true
      this.form2 = row
    },
    async onSubmit2() {
      let result = await this.$putJson2(this.url, this.form2.id, this.form2)
      if (result.data.code == 1) {
        this.dialogVisible = false
        this.form2 = {}
      } else {
        this.$message('失败');
      }
    },
    onCancel2() {
      this.dialogVisible = false
      this.form2 = {}
    },
    async init() {
      let result = await this.$get2(this.api_url, 0, {user_id: this.user_id})
      if (result.data.code == 1) {
        this.tableData = result.data.data
        // await this.$router.push({path: 'video/works'})
      } else {
        this.$message('失败');
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