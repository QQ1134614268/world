<template>
  <div class="p_c_HolyGrail-body" style="height: 100%; ">
    <div class="p_c_box-flex" style="overflow-y: scroll">
      <nav class="p_c_box-flex_col">
        <a :href="'#'+obj.label" key="index" v-for="(obj,index) in tableData">{{ obj.label }}</a>
      </nav>
      <div>
        <div :key="index" v-for="(obj,index) in tableData" style="height: 50rem">
          <a :id="obj.label" style="height: 1.6rem; font-weight: bold">{{ obj.label }}</a>
          <div :key="index2" v-for="(obj2, index2) in obj.data">
            <div class="p_c_box-flex">
              <el-image :src="obj2.img"></el-image>
              <div>
                <div>
                  {{ obj2.name }}
                </div>
                <div>
                  售价: {{ obj2.price }}
                  <el-input-number v-model="obj2.num" @change="handleChange(obj2)" :min="1" :max="10" size="small"
                                   label="描述文字"></el-input-number>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
      <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
        购物车
      </el-button>
      <el-table :data="order_list" style="width: 100%" v-show="drawer">
        <el-table-column prop="name" label="商品名" width="180"></el-table-column>
        <el-table-column prop="price" label="商品价格"></el-table-column>
        <el-button @click="buy">结算</el-button>
        <el-table-column prop="num" label="数量" width="180"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import {GoodsApi} from "@/api/api";
import {toTree} from "@/api/util";

export default {
  name: "Store",
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
      this.tableData = toTree(this.tableData)
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
</style>