<template>
  <div class="p_c_HolyGrail-body">
    <div>
        <el-button size="mini" type="danger" @click="handleEdit">增加</el-button>
    </div>
    <div>
      <el-table :data="tableData">
        <el-table-column prop="name" label="商品名"></el-table-column>
        <el-table-column prop="images" label="商品图片">
          <template slot-scope="scope">
            <el-image style="width: 5rem" :src="scope.row.images"/>
          </template>
        </el-table-column>
        <el-table-column prop="describe" label="商品描述"></el-table-column>
        <el-table-column prop="price" label="商品价格"></el-table-column>
        <el-table-column prop="create_time" label="上架时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="form.dialogVisible">
        <goods-add :form=form></goods-add>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import {GoodsApi} from "@/api/api";
import {deleteJson2, get2} from "@/api/http";
import GoodsAdd from "@/views/member/admin/GoodsAdd.vue";
import GoodsEdit from "@/views/member/admin/GoodsEdit.vue";

export default {
  name: "GoodsList",
  components: {
    GoodsAdd,
    GoodsEdit,
  },
  data() {
    return {
      tableData: [],
      form: {},
      store_id: 1,
      dialogVisible: false,
    }
  },
  methods: {
    async init() {
      let data = {
        store_id: this.store_id
      }
      let res = await get2(GoodsApi, 0, data)
      this.tableData = res.data.data
    },
    async handleDelete(index, row) {
      let res = await deleteJson2(GoodsApi, row.id, {})
    },
    async handleEdit(id, row) {
      debugger
      this.form = row
      this.form.dialogVisible = true
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>