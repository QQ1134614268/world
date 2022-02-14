<template>
  <div class="p_c_HolyGrail-body">
    <div class="p_c_HolyGrail-content">
      <div>
        <div :key="index" v-for="(obj,index) in goodsList">
          <a :href="'#'+obj.type">{{ obj.type }}</a>
        </div>
      </div>
      <div>
        <div :key="index" v-for="(obj,index) in goodsList" style="height: 50rem">
          <a :id="obj.type" style="height: 1.6rem; font-weight: bold">{{ obj.type }}</a>
          <div :key="index2" v-for="(obj2, index2) in obj.data">
            <div class="p_c_box-flex">
              <el-image :src="obj2.img"></el-image>
              <div>
                <div>
                  {{ obj2.name }}
                </div>
                <div>
                  售价: {{ obj2.price }}
                  <el-input-number>el-input-number</el-input-number>
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
        <el-button @click="buy"> 结算</el-button>
        <el-table-column prop="num" label="数量" width="180"></el-table-column>
      </el-table>
      <!--        <el-drawer title="购物车" :visible.sync="drawer" direction='btt'>-->
      <!--         -->
      <!--        </el-drawer>-->
    </div>
  </div>
</template>

<script>
import {GoodsApi} from "@/api/api";

export default {
  name: "market",
  data() {
    return {
      goodsList: [
        {
          type: "主食",
          data: [
            {
              type: "主食",
              name: "大米",
              img: "",
              price: "",
            },
            {
              type: "主食",
              name: "馒头",
              img: "",
              price: "",
            },
          ]
        },
        {
          type: "饮料",
          data: [
            {
              name: "青岛",
              img: "",
              price: "",
            },
            {
              type: "饮料",
              name: "矿泉水",
              img: "",
              price: "",
            },
          ]
        }
      ],
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
</style>