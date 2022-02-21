<template>
  <div class="p_c_HolyGrail-body">
    <div>
      <router-link :to="{path:GoodsAdd,query: {store_id:store_id }}"> 增加</router-link>
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
            <router-link :to="{path:GoodsEdit,query: {store_id:scope.row }}"  > 编辑</router-link>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import {GoodsAdd, GoodsEdit} from "@/views/member";
import {GoodsApi} from "@/api/api";

export default {
  name: "GoodsList",
  data() {
    return {
      GoodsEdit,
      GoodsAdd,
      tableData: [],
      form: {},
      store_id: 1,
    }
  },
  methods: {
    async init() {
      let data = {
        store_id: this.store_id
      }
      let res = await this.$get2(GoodsApi, 0, data)
      this.tableData = res.data.data
    },
    async handleDelete(id) {
      let res = await this.$deleteJson2(GoodsApi, id, {})
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>