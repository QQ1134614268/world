<template>
  <div>
    <el-table :data="tableData" :default-sort ="{prop:'duration',order:'descending'}">
      <el-table-column prop="duration" label="异常信息" sortable>
        <template slot-scope="scope">
          <div v-if="scope.row.size>10">文件大于10M;</div>
          <div v-if="scope.row.duration>15">时间太长</div>
        </template>
      </el-table-column>
      <el-table-column prop="describe" label="主题"></el-table-column>
      <el-table-column prop="thumbnail" label="封面">
        <template slot-scope="scope">
          <img href="scope.row.thumbnail">
          <router-link :to="{path:VideoUrl,query: {video_id: scope.row.id}}">
            <img :src="scope.row.thumbnail">
          </router-link>
        </template>
      </el-table-column>
      <el-table-column prop="size" label="大小"></el-table-column>
      <el-table-column prop="duration" label="时长"></el-table-column>
      <el-table-column prop="duration" label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit( scope.row)">编辑</el-button>
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      {{fileList}}
      <el-form ref="form" :model="form" label-width="8rem" style="padding: 1rem">
        <el-form-item label="视频" prop="describe" required  >
          <WrdVideoUpload  @getFileList="getFileList"  :fileList="fileList" :before-avatar-upload="beforeAvatarUpload">
          </WrdVideoUpload>
        </el-form-item>
        <el-form-item label="视频封面" prop="describe" required>
          <el-upload style="width: 10%;height: 10%" :show-file-list="false" :action="FileApi"
                     :on-success="uploadFileSuccess2">
            <img v-if="form.thumbnail" :src="form.thumbnail">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="form.describe"></el-input>
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

import {FileApi, WorksApi} from "@/api/api";
import {videoBeforeUpload} from "@/api/util";
import {VideoUrl} from "@/views/video";
import WrdVideoUpload from "@/components/WrdVideoUpload";

export default {
  name: "market",
  components: {WrdVideoUpload},
  data() {
    return {
      VideoUrl,
      tableData: [],
      form: {},
      dialogVisible: false,
      fileList: [],
      FileApi,

    }
  },
  methods: {
    async init() {
      let url = "/api/video_blueprint_api/err_video"
      let res = await this.$get2(url, 0)
      this.tableData = res.data.data
    },
    getFileList(fileList){
      this.fileList=fileList
    },
    uploadFileSuccess2(res, file, fileList) {
      this.form.thumbnail = res.data
    },
    async onSubmit() {
      if (!this.fileList) {
        this.$message('请上传视频');
        return
      }
      this.form.file = this.fileList[0].name
      let result = await this.$ppJson(WorksApi, this.form.id, this.form)
      if (result.data.code == 1) {
        this.dialogVisible = false
      } else {
        this.$message('失败');
      }
    },
    async onCancel() {
      this.form = {}
      this.dialogVisible = false
    },
    handleEdit(row) {
      this.dialogVisible = true
      this.form = row
    },
    async del(index, id) {
      let result = await this.$deleteJson2(WorksApi, id)
      if (result.data.code == 1) {
        this.$message('删除成功!');
        this.tableData.splice(index, 1)
      } else {
        this.$message('');
      }
    },
    beforeAvatarUpload(file) {
      return videoBeforeUpload(file)
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>