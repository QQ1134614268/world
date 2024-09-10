<template>
  <div class="containerBox">
    <div class="searchBox">
      <el-button size="mini" @click="init">查询</el-button>
    </div>
    <div class="actionBox">
      <el-button size="mini" type="danger" @click="handleAdd">增加</el-button>
    </div>
    <div class="tableBox">
      <el-table :data="page.data">
        <el-table-column prop="value" label="value"></el-table-column>
        <el-table-column prop="label" label="label"></el-table-column>
        <el-table-column prop="code" label="code"></el-table-column>
        <el-table-column prop="comment" label="comment"></el-table-column>
        <el-table-column prop="create_time" label="create_time"></el-table-column>
        <el-table-column prop="group_code" label="group_code"></el-table-column>
<!--        <el-table-column prop="sort" label="sort"></el-table-column>-->
        <el-table-column label="操作">
          <template slot-scope="scope">
            <a :href="ENUM_INFO+'?parent_code='+scope.row.id">
              <el-button size="mini" type="danger">详情</el-button>
            </a>
            <el-button size="mini" type="danger" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <el-pagination @size-change="handleSizeChange"
                   @current-change="handleCurrentChange"
                   :current-page="page.page"
                   :page-size="page.page_size"
                   :total="page.total"
                   layout=" prev, pager, next, total">
    </el-pagination>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogForm.dialogVisible">
      <EnumUpdate :form=form :dialogForm=dialogForm></EnumUpdate>
    </el-dialog>
  </div>
</template>

<script>
import {ConfigApi, enum_api_page} from "@/api/api";
import {deleteJson2, getJson3} from "@/api/http";
import EnumUpdate from "@/views/sys/EnumUpdate.vue";
import {ENUM_INFO} from "@/views/sys/index";

export default {
  name: "GoodsList",
  components: {
    EnumUpdate
  },
  data() {
    return {
      ENUM_INFO: ENUM_INFO,
      page: {
        page: 1,
        page_size: 10,
        data: [],
      },
      form: {},
      dialogForm: {
        dialogVisible: false,
      },
      store_id: 1,
    }
  },
  methods: {
    async init() {
      let param = {
        currentPage: this.page.page,
        pageSize: this.page.page_size,
        parent_code: -1,
      }
      let res = await getJson3(enum_api_page, param)
      if (res.data.code === 1) {
        this.page = res.data
      } else {
        this.$message.error('服务器异常');
      }
    },
    async handleDelete(index, row) {
      let res = await deleteJson2(ConfigApi, row.id, {})
      if(res.data.code !== 1){
        this.$message.error('服务器异常');
      }
    },
    async handleEdit(id, row) {
      this.form = row
      this.dialogForm.dialogVisible = true
    },
    async handleAdd() {
      this.dialogForm.dialogVisible = true
    },
    handleCurrentChange(val) {
      this.page.page = val;
      this.init();
    },
    handleSizeChange(val) {
      this.page.page_size = val;
      this.init();
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped lang="less">
.containerBox {
  width: 100%;
  padding: 1rem;

  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  //justify-content: center;
  align-items: center;

  .searchBox {
    width: 100%;
    height: 3rem;

    //margin-top: 1rem;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);

    background-color: #ffffff;
    border-radius: 0.75rem;

    display: flex;
    flex: 0 0 auto;
    align-items: center;
  }

  .actionBox {
    width: 100%;
    height: 3rem;

    //margin-top: 1rem;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);

    background-color: #ffffff;
    border-radius: 0.75rem;

    display: flex;
    flex: 0 0 auto;
    align-items: center;
  }

  .tableBox {
    width: 100%;
    //margin-top: 1rem;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);

    background-color: #ffffff;
    border-radius: 0.75rem;

    display: flex;
    flex: 0 0 auto;
    align-items: center;
  }
}

</style>
