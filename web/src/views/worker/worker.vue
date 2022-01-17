<template>
  <div>
    <div>
      <div>
        <el-button type="primary" plain @click="handleAdd">增加</el-button>
        <el-button type="primary" plain @click="upDialog=true">导入</el-button>
        <el-button type="primary" plain @click="exportExcel">导出</el-button>
      </div>
      <div class="p_c_flexbox">
        <div class="col-3">
          <span class="col-3">姓名:</span>
          <el-autocomplete class="inline-input" v-model="searchName" placeholder="请输入内容"
                           :fetch-suggestions="querySearch"
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
        <div class="col-6">
          <span>入职时间:</span>
          <el-date-picker class="col-6" value-format="yyyy-MM-dd" v-model="dateRange"
                          type="daterange" range-separator="至 " start-placeholder="开始日期" end-placeholder="结束日期">
          </el-date-picker>
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
      <el-pagination hide-on-single-page
                     @size-change="handleSizeChange" @current-change="handleCurrentChange"
                     :current-page="currentPage" :page-size="pageSize" :total="totalNum"
                     layout=" prev, pager, next">
      </el-pagination>

    </div>

    <el-dialog title="上传Excel" :visible.sync="upDialog" width="30%">
      <el-upload multiple :auto-upload="false" :action="worker_excel_url" :headers="headers" ref="upload"
                 :on-success="handleSuccess">

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
          <el-date-picker class="col-6" value-format="yyyy-MM-dd" v-model="form.birthday" type="date">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="入职日期 : ">
          <el-date-picker class="col-6" value-format="yyyy-MM-dd" v-model="form.start_time" type="date">
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
import Axios from "axios";
import {WorkerApi, WorkerExcelApi} from "@/api/api";

export default {
  name: "MyWorker",
  data() {
    return {
      //搜索
      dateRange: [],
      searchName: "",
      searchIDCard: "",
      searchPhone: "",
      headers: {
        token: localStorage.getItem("token")
      },
      //分页
      currentPage: 1,
      pageSize: 6,
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
    async handleSuccess(res, file) {
      if (res.code === 1) {
        this.$message('操作成功')
      }
      if (res.code === 2) {
        this.$message(res.data.data)
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
      this.$refs.upload.submit();
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
        page: this.currentPage,
        pageSize: this.pageSize,
        name: this.searchName,
        idCard: this.searchIDCard,
        phone: this.searchPhone,
        startDate: this.dateRange[0],
        endDate: this.dateRange[1],
      }
      let response = await this.$get2(WorkerApi, 0, data);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.data = response.data.data
    },
    async sortChange(column, prop, order) {
      let data = {
        page: this.currentPage,
        pageSize: this.pageSize,
        name: this.searchName,
        idCard: this.searchIDCard,
        phone: this.searchPhone,
        startDate: this.dateRange[0],
        endDate: this.dateRange[1],
        sortBy: column.prop,
        order: column.order
      }
      let response = await this.$get2(WorkerApi, 0, data);
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.data = response.data.data
    },
    async querySearch(queryString, cb) {
      let data = {name: queryString}
      let res = await this.$get2(WorkerApi, 0, data)
      let suggest = []
      for (let i = 0; i < res.data.data.length; i++) {
        suggest.push({
          value: res.data.data[i].name
        })
      }
      cb(suggest)
    },
    async save() {
      let response;
      if (this.form.id) {
        response = await this.$putJson2(WorkerApi, this.form.id, this.form);
      } else {
        response = await this.$postJson2(WorkerApi, 0, this.form);
      }
      if (response.data.code != 1) {
        this.$message(response.data.data);
        return
      }
      this.$message('success');

      await this.init();
    },

    async exportExcel() {
      let res = await Axios.get(this.worker_excel_url, {
        responseType: 'arraybuffer', // 或者responseType: 'blob'
        xsrfHeaderName: 'Authorization',
        headers: this.headers
      })
      try {
        let data = JSON.parse(res.data)
        if (data.code != 1) {
          this.$message(data.data)
        }
      } catch (err) {
        // const {data, headers} = res;
        // const fileName = headers['content-disposition'].replace(/\w+;filename=(.*)/, '$1');
        const link = document.createElement('a');  // 创建元素
        link.style.display = 'none';
        let blob = new Blob([res.data]);
        link.style.display = 'none';
        link.href = URL.createObjectURL(blob);   // 创建下载的链接
        let fileName = "工人列表.xlsx"
        link.setAttribute('download', fileName);  // 给下载后的文件命名 fileName文件名  type文件格式
        document.body.appendChild(link);
        link.click();  // 点击下载
        document.body.removeChild(link);  //  下载完成移除元素
        window.URL.revokeObjectURL(link.href);  // 释放掉blob对象
      }
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
      let response = await this.$deleteJson2(WorkerApi, row.id);
      await this.init();
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>
