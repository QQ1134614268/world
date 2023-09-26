<template>
  <BoxCol class="store">
    <!--    <scroll-view :scroll-y="true" @scroll="productScroll" @scrolltolower="new_productToLower"-->
    <!--                 :scroll-into-view="clickId">-->
    <!--      <view v-for="(item_,index) in current_products" class="right_box" :key="index" :id="'po'+index">-->
    <!--      </view>-->
    <!--    </scroll-view>-->
    <BoxRow class="store_body">
      <BoxCol class="navTotal">
        <!--        侧边导航栏-->
        <a :href="'#'+obj.label" :key="index" v-for="(obj,index) in tableData">
          <div class="nav">{{ obj.label }}</div>
        </a>
      </BoxCol>
      <BoxCol class="store_menu">
        <!--        主体-->
        <BoxCol :key="index" v-for="(obj,index) in tableData">
          <a :id="obj.label">
            <div class="type_class">{{ obj.label }}</div>
          </a>
          <BoxRow :key="index2" v-for="(obj2, index2) in obj.data" class="info">
            <el-image class="img" :src="obj2.images"></el-image>
            <BoxCol class="infoTxt p_c_flex_1 ">
              <div class="goodName ">
                {{ obj2.name }}
              </div>
              <BoxRow class="price  ">
                <div>售价: {{ obj2.price }}</div>

              </BoxRow>
            </BoxCol>
            <el-input-number v-if="obj2.num" v-model="obj2.num" size="small" @change="change"></el-input-number>
            <i v-else class="el-icon-circle-plus add_icon" @click="add(obj2)"></i>
          </BoxRow>
        </BoxCol>
      </BoxCol>
    </BoxRow>
    <BoxCol class="store_chart">
      <BoxRow class="btn">
        <el-button @click="drawer = true" type="primary" style="margin-left: 1rem;">
          购物车
        </el-button>
        <el-button @click="drawer = false" type="primary" style="margin-left: 1rem;" v-if="drawer">
          关闭
        </el-button>
      </BoxRow>
      <BoxCol v-show="drawer">
        <el-table :data="order_list" class="table">
          <el-table-column prop="name" label="商品名" width="180"></el-table-column>
          <el-table-column prop="price" label="商品价格"></el-table-column>
          <el-table-column prop="num" label="数量" width="180">
            <template slot-scope="scope">
              <el-input-number v-model="scope.row.num" size="small" @change="change"></el-input-number>
            </template>
          </el-table-column>
        </el-table>
        <div class="btn2">
          <el-button @click="buy" type="primary">下单</el-button>
        </div>
      </BoxCol>
    </BoxCol>
  </BoxCol>
</template>

<script>
import {GoodsApi} from "@/api/api";
import {toTree} from "@/api/util";
import {postOrder} from "@/api/member_api";

export default {
  name: "Store",
  data() {
    return {
      num: 0,
      tableData: [],
      tableData2: [],
      drawer: false,
      order_list: [],
      orderMap: {},
      store_id: 1
    }
  },
  methods: {
    add(obj) {
      obj.num = (obj.num || 0) + 1
      this.order_list = this.tableData2.filter((obj) => obj.num > 0)
    },
    change() {
      this.order_list = this.tableData2.filter((obj) => obj.num > 0)
    },
    async buy() {
      let res = await postOrder(this.order_list)
      if (res.data.code == 1) {
        this.$message.success("下单成功")
        this.order_list = this.order_list.map((obj) => obj.num = 0)
      } else {
        this.$message.error("下单失败")
      }

    },
    async init() {
      let data = {
        store_id: this.store_id
      }
      let response = await this.$get2(GoodsApi, 0, data);
      this.tableData2 = response.data.data
      this.tableData = toTree(this.tableData2)
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

.store {
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  flex-grow: 1;
}

.store_body {
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  flex-grow: 1;
  height: 10rem;
}

.store_menu {
  width: 100%;
  display: flex;
  flex: 0 0 auto;
  flex-grow: 1;
  overflow-y: auto;
}

.store_chart {

}

.navTotal {
  width: 4rem;
  margin: 1rem 1rem 0rem 1rem;
  background: #e3e1e1;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
}

.nav {
  margin: 1rem 0rem;
  background: #cccccc;
}

.type_class {
  color: #cccccc;
  font-weight: lighter;
  line-height: 2rem;
  margin-top: 1rem;
}

.img {
  width: 5rem;
  height: 5rem;
  margin-right: 0.5rem;
}

.info {
  margin-bottom: 0.5rem;
}

.infoTxt {
  justify-content: space-between;
}

.goodName {
}

.price {
  justify-content: space-between;
  align-content: center;
  width: 100%;
}

.add_icon {
  margin-right: 2rem;
}

.btn {
  justify-content: flex-end;
}

.btn2 {
  align-self: flex-end;
}

.table {
  width: 100%;
  height: 6rem;
}
</style>