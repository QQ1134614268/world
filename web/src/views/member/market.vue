<template>
  <div>
    店内商品
    <div class="p_c_flexbox">
      <div v-for="(o,index) in tableData " style="width: 10rem;">
        <div>
          <img :src="FilePathApi+o.images" style="object-fit: cover">
        </div>
        <div>
          <div>
            价格: {{ o.price }} 元
          </div>
          <div>
            {{ o.name }}
          </div>
          <div>
            <el-button @click="">caozuo</el-button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="order_list.length">
      <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
        购物车
      </el-button>
      <el-button @click="buy"> 结算</el-button>
    </div>
    <el-drawer title="购物车" :visible.sync="drawer" direction='btt'>
      <el-table :data="order_list" style="width: 100%">
        <el-table-column prop="name" label="商品名" width="180"></el-table-column>
        <el-table-column prop="price" label="商品价格"></el-table-column>
        <el-button @click="buy"> 结算</el-button>
        <el-table-column prop="num" label="数量" width="180"></el-table-column>
      </el-table>
    </el-drawer>
  </div>
</template>

<script>
import {FilePathApi, GoodsApi} from "@/api/api";

export default {
  name: "market",
  data() {
    return {
      tableData: [],
      drawer: false,
      order_list: [],
      FilePathApi
    }
  },
  methods: {
    buy() {
    },
    async init() {
      let data = {
        store_id: 1
      }
      let response = await this.$get2(GoodsApi, 0, data);
      this.tableData = response.data.data
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>