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
        <el-table-column prop="name" label="商品名"></el-table-column>
        <el-table-column prop="image" label="商品图片">
          <template slot-scope="scope">
            <el-image style="width: 5rem" :src="scope.row.image"/>
          </template>
        </el-table-column>
        <el-table-column prop="describe" label="商品描述"></el-table-column>
        <el-table-column prop="price" label="商品价格"></el-table-column>
        <el-table-column prop="type_name" label="分类"></el-table-column>
        <el-table-column prop="create_time" label="上架时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <el-pagination @size-change="init"
                   @current-change="init"
                   :current-page="page.page"
                   :page-size="page.page_size"
                   :total="page.total"
                   layout=" prev, pager, next, total">
    </el-pagination>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogForm.dialogVisible">
      <goods-edit :form=form :dialogForm=dialogForm></goods-edit>
    </el-dialog>
  </div>
</template>

<script>
import {GoodsApi, goodsPage} from "@/api/api";
import {deleteJson2, getJson3} from "@/api/http";
import GoodsEdit from "@/views/member/admin/GoodsEdit.vue";

export default {
  name: "GoodsList",
  components: {
    GoodsEdit,
  },
  data() {
    return {
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
      types: []
    }
  },
  methods: {
    async init() {
      let data = {
        store_id: this.store_id
      }
      let res = await getJson3(goodsPage, data)
      if (res.data.code === 1) {
        this.page = res.data
      } else {
        this.$message.error('服务器异常');
      }
    },
    async handleDelete(index, row) {
      let res = await deleteJson2(GoodsApi, row.id, {})
    },
    async handleEdit(id, row) {
      this.form = row
      this.dialogForm.dialogVisible = true
    },
    async handleAdd() {
      this.dialogForm.dialogVisible = true
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
