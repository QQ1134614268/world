<template>
  <div class="p_c_HolyGrail-body">
    <div>
      <router-link to="/admin/GoodsAdd"> 增加</router-link>
    </div>
    <div>
      <el-table :data="data">
        <el-table-column prop="name" label="商品名"></el-table-column>
        <el-table-column prop="describe" label="商品描述"></el-table-column>
        <el-table-column prop="price" label="商品价格"></el-table-column>
        <el-table-column prop="create_time" label="上架时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <router-link to="/admin/GoodsEdit"> 编辑</router-link>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "GoodsList",
  data() {
    return {
      data: [{
        type: "主食",
        name: "大米",
        img: "",
        price: "",
      },],
      form: {},

    }
  },
  methods: {
    handleEdit() {
    },
    handleDelete() {
    },
    exportExcel() {
    }
  }
}
</script>

<style scoped>

</style>