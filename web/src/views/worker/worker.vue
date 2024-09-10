<template>
  <div>
    <div>
      <div>
        <el-button type="primary" size="mini" plain @click="handleAdd">增加</el-button>
        <el-button type="primary" size="mini" plain @click="upDialog=true">导入</el-button>
        <el-button type="primary" size="mini" plain @click="exportExcel">导出</el-button>
      </div>
      <div class="p_c_flexbox">
        <div class="col-3">
          <span class="col-3">姓名:</span>
          <el-autocomplete class="inline-input" v-model="searchName" placeholder="请输入内容"
                           :fetch-suggestions="query"
                           :trigger-on-focus="false">
          </el-autocomplete>
        </div>
        <div class="col-3">
          <span>身份证:</span>
          <el-input class="col-6" v-model="searchIDCard"></el-input>
        </div>
        <div class="col-3">
          <span class="col-3">联系电话:</span>
          <el-input class="col-9" v-model="searchPhone"></el-input>
        </div>
        <div>
          <el-button type="primary" @click="init">搜索</el-button>
        </div>
      </div>

      <el-table :data="data" style="width: 100%" @sort-change="sortChange">
        <el-table-column prop="name" label="姓名" sortable="custom"></el-table-column>
        <el-table-column prop="id_card_number" label="身份证" sortable></el-table-column>
        <el-table-column prop="sex" label="性别" sortable></el-table-column>
        <el-table-column prop="pay" label="薪资" sortable></el-table-column>
        <el-table-column prop="birthday" label="生日"></el-table-column>
        <el-table-column prop="start_time" label="入职时间" sortable></el-table-column>
        <el-table-column prop="phone" label="联系电话"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
          @size-change="handleSizeChange" @current-change="handleCurrentChange"
          :current-page="currentPage" :page-size="pageSize" :total="totalNum"
          layout=" prev, pager, next">
      </el-pagination>

    </div>

    <el-dialog title="上传Excel" :visible.sync="upDialog" width="30%">
      <el-upload multiple :auto-upload="false" :action="worker_excel_url" :headers="headers" ref="upload"
                 :on-success="uploadFileSuccess">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">点击上传</div>
        <div class="el-upload__tip">上传excel文件</div>
      </el-upload>
      <span slot="footer" class="dialog-footer">
          <el-button @click="upDialog = false">取 消</el-button>
          <el-button type="primary" @click="upLoad();upDialog = false">确认</el-button>
      </span>
    </el-dialog>

    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="editDialog" width="30%">
      <el-form v-model="form" label-position="left" label-width="8rem">
        <el-form-item label="姓名 : ">
          <el-input class="col-6" v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="身份证 : ">
          <el-input class="col-6" v-model="form.id_card_number"></el-input>
        </el-form-item>
        <el-form-item label="电话 : ">
          <el-input class="col-6" v-model="form.phone"></el-input>
        </el-form-item>
        <el-form-item label="生日 : ">
          <el-date-picker class="col-6" :value-format=DATE_FMT v-model="form.birthday" type="date">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="入职日期 : ">
          <el-date-picker class="col-6" :value-format=DATE_FMT v-model="form.start_time" type="date">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="薪资 : ">
          <el-input class="col-6" v-model="form.pay"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button @click="editDialog = false">取 消</el-button>
          <el-button type="primary" @click="save();editDialog = false">保存</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import {WorkerApi, WorkerExcelApi} from "@/api/api";
import {exportExcelByHeader, getToken, querySearch} from "@/api/util";
import {DATE_FMT} from "@/api/config";
import {deleteJson2, get2, ppJson} from "@/api/http";

export default {
  name: "MyWorker",
  data() {
    return {
      DATE_FMT,

      //搜索
      searchName: "",
      searchIDCard: "",
      searchPhone: "",
      headers: {
        token: getToken()
      },
      //分页
      currentPage: 1,
      pageSize: 10,
      totalNum: 0,

      //表格
      data: [],
      worker_excel_url: process.env.VUE_APP_BASE_URL + WorkerExcelApi,
      // 表单
      form: {},

      upDialog: false,
      editDialog: false,
    }
  },
  methods: {
    async uploadFileSuccess(res, file) {
      if (res.code === 1) {
        this.$message.success('操作成功')
      }
      if (res.code === 2) {
        this.$message.error(res.data)
      }
      if (res.code === 4) {
        let str = res.data.join(' <br/> ');
        this.$message({
          dangerouslyUseHTMLString: true,
          message: str,
          type: 'warning'
        });
      }
    },
    async upLoad() {
      await this.$refs.upload.submit();
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.init();
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.init();
    },
    async init() {
      let data = {
        currentPage: this.currentPage,
        pageSize: this.pageSize,
        name: this.searchName,
        idCard: this.searchIDCard,
        phone: this.searchPhone,
        startDate: this.dateRange && this.dateRange.length > 0 ? this.dateRange[0] : "",
        endDate: this.dateRange && this.dateRange.length > 1 ? this.dateRange[1] : "",
      }
      let response = await get2(WorkerApi, 0, data);
      if (response.data.code !== 1) {
        this.$message.error(response.data.data);
        return
      }
      this.data = response.data.data
      this.totalNum = response.data.total
    },
    async sortChange(column, prop, order) {
      let data = {
        page: this.currentPage,
        pageSize: this.pageSize,
        name: this.searchName,
        idCard: this.searchIDCard,
        phone: this.searchPhone,
        startDate: this.dateRange && this.dateRange.length > 0 ? this.dateRange[0] : "",
        endDate: this.dateRange && this.dateRange.length > 1 ? this.dateRange[1] : "",
        sortBy: column.prop,
        order: column.order
      }
      let response = await get2(WorkerApi, 0, data);
      if (response.data.code !== 1) {
        this.$message.error(response.data.data);
        return
      }
      this.data = response.data.data
    },
    async query(queryString, cb) {
      let data = {name: queryString}
      await querySearch(data, cb, WorkerApi)
    },
    async save() {
      let response = await ppJson(WorkerApi, this.form.id, this.form);
      if (response.data.code !== 1) {
        this.$message.error(response.data.data);
        return
      }
      this.$message('success');
      await this.init();
    },

    async exportExcel() {
      await exportExcelByHeader(this.worker_excel_url, this.headers)
    },
    handleAdd() {
      this.form = {};
      this.editDialog = true
    },
    handleEdit(index, row) {
      this.form = row;
      this.editDialog = true
    },
    async handleDelete(index, row) {
      let response = await deleteJson2(WorkerApi, row.id);
      if (response.data.code !== 1) {
        this.$message.error(response.data.data);
      }
      await this.init();
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>
