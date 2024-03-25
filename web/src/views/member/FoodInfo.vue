<template>
  <div class="container">
    <div style="overflow-y: auto">
      <div class="storeName">深圳方大城店</div>
      <div class="row1">
        <div class="storeBox">
          <div class="storeInfoBox">
            <img class="positionIcon" src="@/assets/切图/点餐2/位置.png">
            <div class="storeName2">深圳方大城店</div>
            <img class="moreIcon" src="@/assets/切图/点餐2/箭头.png">
          </div>
          <div class="address">
            深圳市南山区桃源社区高发西...
          </div>
        </div>
        <div class="way">
          <span class="self">自取</span>
          <span class="out">外卖</span>
        </div>
      </div>
      <div class="row2">
        <img src="@/assets/切图/点餐2/banner.png">
      </div>
      <div class="row3">
        <div class="menuGroup">
          <div class="foodType">
            经典推荐
          </div>
          <div class="foodType">
            招牌鸡汤
          </div>
          <div class="foodType">
            人气推荐
          </div>
          <div class="foodType">
            早餐组合
          </div>
        </div>
        <div class="foodList">
          <div class="foodTypeName">经典推荐</div>
          <div class="foodGroupList">
            <div class="foodBox" v-for="(food, index) in foodList">
              <img class="foodImg" :src=food.images>
              <div class="foodDescBox">
                <div class="foodName">{{ food.name }}</div>
                <div class="foodDesc">{{ food.describe }}</div>
                <div class="priceBox">
                  <div class="foodPrice">¥{{ food.price }}</div>
                  <div class="iconAdd">
                    <img class="iconAdd" src="@/assets/切图/点餐2/+.png">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="cart">
      <!--      <el-popover-->
      <!--          placement="right"-->
      <!--          width="400"-->
      <!--          trigger="click">-->
      <!--          <el-table :data="gridData">-->
      <!--            <el-table-column width="150" property="date" label="日期"></el-table-column>-->
      <!--            <el-table-column width="100" property="name" label="姓名"></el-table-column>-->
      <!--            <el-table-column width="300" property="address" label="地址"></el-table-column>-->
      <!--          </el-table>-->
      <!--          <el-button slot="reference">click 激活</el-button>-->
      <!--      </el-popover>-->

      <div class="sum">
        <i class="el-icon-shopping-bag-1 cart-icon"></i>
        ¥{{ totalMoney }}
      </div>
      <div class="settlement">
        选好了
      </div>
    </div>
  </div>
</template>

<script>
import {goodsPage} from "@/api/api";
import {getJson3} from "@/api/http";

export default {
  name: "OrderInfo",
  data() {
    return {
      tableData: [],
      order_code: this.$route.query.order_code,
      foodList: [],
      orderList: [],
    }
  },
  computed: {
    totalMoney() {
      if (this.orderList.length === 0) {
        return 0
      }
      return this.orderList.map(value => value.price * value.num).reduce((a, b) => a + b)
    }
  },
  methods: {
    async init() {
      let data = {
        order_code: this.order_code
      }
      let res = await getJson3(goodsPage, data)
      if (res.data.code !== 1) {
        this.$message.error('服务器异常');
        return
      }
      this.foodList = res.data.data
    }
  },
  created() {
    this.init()
  },
}
</script>

<style scoped lang="less">
.container {
  width: 100%;
  padding: 1rem 3rem;
  height: 100%;
  max-height: 100%;

  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  justify-content: center;
  align-items: center;
}

.storeName {
  width: 100%;
  height: 4rem;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: SourceHanSansCN-Medium;
  font-size: 2rem;
  font-weight: bold;
  font-stretch: normal;
  line-height: 1.6rem;
  letter-spacing: 0;
  color: #000000;
}

.row1 {
  width: 100%;
  margin-top: 1rem;

  display: flex;
  flex: 0 0 auto;
  justify-content: space-between;
  align-items: center;

  .storeBox {
    .storeInfoBox {
      display: flex;
      flex: 0 0 auto;

      .positionIcon {
        width: 1.625rem;
        height: 1.625rem;
        object-fit: contain;
      }

      .storeName2 {
        width: 10rem;
        height: 1.625rem;
        margin: 0 1rem;
        font-family: SourceHanSansCN-Medium;
        font-size: 1.625rem;
        font-weight: normal;
        font-stretch: normal;
        line-height: 1.625rem;
        letter-spacing: 0;
        color: #000000;
      }

      .moreIcon {
        width: 1.625rem;
        height: 1.625rem;
        object-fit: contain;
      }
    }

    .address {
      width: 31.875rem;
      height: 1.5rem;
      font-family: SourceHanSansCN-Regular;
      font-size: 1.5rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      letter-spacing: 0;
      color: #838383;
    }
  }

  .way {
    display: flex;
    flex: 0 0 auto;
    justify-self: center;
    align-items: center;

    .self {
      width: 5.3125rem;
      height: 3rem;
      background-color: #333333;
      border-radius: 1.5rem;

      display: flex;
      flex: 0 0 auto;
      justify-content: center;
      align-items: center;

      font-family: SourceHanSansCN-Regular;
      font-size: 1.5rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      letter-spacing: 0;
      color: #ffffff;
    }

    .out {
      width: 3rem;
      height:  1.5rem;
      font-family: SourceHanSansCN-Regular;
      font-size:  1.5rem;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      letter-spacing: 0;
      color: #838383;
    }
  }

}

.row2 {
  width: 100%;
  margin-top: 1rem;
  //background-color: #9ed710;
  border-radius: 0.75rem;
}

.row3 {
  width: 100%;
  margin-top: 2rem;
  display: flex;
  flex: 0 0 auto;
  height: 50%;

  .menuGroup {
    width: 8rem;
    font-family: SourceHanSansCN-Bold;
    font-size: 1.6rem;
    font-weight: normal;
    font-stretch: normal;
    line-height: 2.4rem;
    letter-spacing: 0;
    color: #000000;

    .foodType {
      width: 100%;
      margin-top: 1rem;
      font-size: 1.6rem;
      font-weight: bold;
    }
  }

  .foodList {
    width: 100%;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    flex: 1;


    .foodTypeName {
      width: 10rem;
      height: 1.875rem;
      font-family: SourceHanSansCN-Regular;
      font-size: 1.5rem;
      font-weight: normal;
      font-stretch: normal;
      letter-spacing: 0;
      color: #000000;
    }

    .foodGroupList {
      width: 100%;

      .foodBox {
        display: flex;
        flex: 0 0 auto;
        padding: 1rem 0;

        .foodImg {
          width: 8rem;
          height: 8rem;
          border-radius: 0.75rem;
          object-fit: contain;
        }

        .foodDescBox {
          padding: 0.5rem;
          display: flex;
          flex-direction: column;
          flex: 1;
          justify-content: space-around;

          .foodName {
            //height: 2.5rem;
            padding: 0.1rem 0.5rem;
            font-family: SourceHanSansCN-Regular;
            font-size: 1.5rem;
            font-weight: normal;
            font-stretch: normal;
            letter-spacing: 0;
            color: #000000;
          }

          .foodDesc {
          //height: 1rem;
          padding: 0.1rem 0.5rem;
          font-family: SourceHanSansCN-Regular;
          font-weight: normal;
          font-stretch: normal;
          letter-spacing: 0;
          color: #bbbbbb;
        }

        .priceBox {
          display: flex;
          flex: 0 0 auto;
          justify-content: space-between;
          align-items: center;

          .foodPrice {
            font-family: SourceHanSansCN-Bold;
            font-size: 1.8rem;
            font-weight: normal;
            font-stretch: normal;
            color: #ff0000;
          }

          .iconAdd {
            width: 2rem;
            height: 2rem;
            background-color: #9ed710;
            border-radius: 0.75rem;
          }
        }
        }
      }
    }
  }
}

.cart {
  width: 100%;
  height: 2rem;
  display: flex;
  flex: 0 0 auto;
  justify-content: center;
  align-items: center;

  font-size: 2rem;

  .sum {
    width: 8rem;
    flex-grow: 1;
    background-color: #92b7ab;
    border-top-left-radius: 2rem;

    .cart-icon {
      color: blue;
      margin-left: 2rem;
    }
  }

  .settlement {
    width: 8rem;
    margin-right: 2rem;
    background-color: #f33b3b;
    border-top-right-radius: 2rem;
    display: flex;
    justify-content: center;
  }
}
</style>