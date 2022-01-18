<template>
  <div>
    <div>店内商品</div>
    <div class="p_c_flexbox">
      <div v-for="(o,index) in tableData " class="col-1 p_c_test_border card">
        <div class="p_c_test_border">
          <img :src="o.images" style="object-fit: cover">
        </div>
        <div>
          <div>
            价格: {{ o.price }} 元
          </div>
          <div>
            {{ o.name }}
          </div>
          <div>
            <el-input-number v-model="o.num" @change="handleChange(o)" :min="1" :max="10" size="small"
                             label="描述文字"></el-input-number>
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
import {GoodsApi} from "@/api/api";

export default {
  name: "market",
  data() {
    return {
      num: 0,
      tableData: [],
      drawer: false,
      order_list: [],
      orderMap: {},
    }
  },
  methods: {
    buy() {
    },
    handleChange(goodObj) {
      this.orderMap[goodObj.id] = goodObj
      this.order_list = []
      for (let i in this.orderMap) {
        this.order_list.push(this.orderMap[i])
      }
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
@media (max-width: 768px) {
  .card {
    width: 100%;
  }
}

@media (min-width: 768px) {
  .card {
    width: 8.3%;
  }
}
</style>