<template>
  <div>
    <el-table :data="tableData" :default-sort="{prop:'duration',order:'descending'}">
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
      <el-table-column label="异常信息" sortable>
        <template slot-scope="scope">
          <div v-if="scope.row.size>10">文件大于10M;</div>
          <div v-if="scope.row.duration>15">时间太长</div>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit( scope.row)">编辑</el-button>
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" label-width="8rem" style="padding: 1rem">
        <el-form-item label="视频" prop="describe" required>
          <WrdVideoUploadV2 @getUrl="getUrl" :fileUrl="form.file" :fileList="fileList"
                            :before-avatar-upload="beforeAvatarUpload">
          </WrdVideoUploadV2>
        </el-form-item>
        <el-form-item label="视频封面" prop="describe" required>
          <WrdImgUpload @getUrl="getUrl2" :fileUrl="form.thumbnail"></WrdImgUpload>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="form.describe"></el-input>
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

import {FileApi, WorksApi} from "@/api/api";
import {videoBeforeUpload} from "@/api/util";
import {VideoUrl} from "@/views/video";
import WrdVideoUploadV2 from "@/components/WrdVideoUploadV2";
import WrdImgUpload from "@/components/WrdImgUpload";

export default {
  name: "ERR_Video",
  components: {WrdVideoUploadV2, WrdImgUpload},
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
    getUrl(fileUrl) {
      this.form.file = fileUrl
    },
    getUrl2(fileUrl) {
      this.form.thumbnail = fileUrl
    },
    async onSubmit() {
      if (!this.form.file) {
        this.$message.warning('请上传视频');
        return
      }
      let result = await this.$ppJson(WorksApi, this.form.id, this.form)
      if (result.data.code == 1) {
        this.dialogVisible = false
      } else {
        this.$message.error('失败');
      }
      this.$message.success('保存成功');
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
        this.$message.success('删除成功!');
        this.tableData.splice(index, 1)
      } else {
        this.$message.error('操作失败');
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