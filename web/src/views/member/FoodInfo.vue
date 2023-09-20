<template>
  <div class="container">
    <div class="storeName">深圳方大城店</div>
    <div class="row1">
      <div class="row1Box">
        <div class="storeBox">
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
    <div class="banner">
      <img src="@/assets/切图/点餐2/banner.png">
    </div>
    <div class="row3">
      <div class="menuGroup">
        <div>
          经典推荐
        </div>
        <div>
          招牌鸡汤
        </div>
        <div>
          人气推荐
        </div>
        <div>
          早餐组合
        </div>
      </div>
      <div class="foodList">
        <div class="group">经典推荐</div>
        <div class="foodBox">
          <img class="foodImg" src="@/assets/切图/首页/图层23.png">
          <div class="foodDescBox">
            <div class="foodName">鸡汁腊鱼</div>
            <div class="foodDesc">【口味：酱香微辣】新鲜的...</div>
            <div class="priceBox">
              <div class="foodPrice">￥15</div>
              <div class="iconAdd">
                <img class="iconAdd" src="@/assets/切图/点餐2/+.png">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {GoodsApi} from "@/api/api";

export default {
  name: "OrderInfo",
  data() {
    return {
      tableData: [],
      order_code:this.$route.query.order_code
    }
  },
  methods: {
    async init() {
      let data = {
        order_code: this.order_code
      }
      let res = await this.$get2(GoodsApi, 0, data)
      if (res.data.code != 1) {
        this.$message.error('服务器异常');
        return
      }
      this.tableData = res.data.data
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

  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  align-items: center;
  justify-content: center;
}

.storeName {
  width: 210px;
  height: 33px;
  font-family: SourceHanSansCN-Medium;
  font-size: 34px;
  font-weight: normal;
  font-stretch: normal;
  line-height: 27px;
  letter-spacing: 0px;
  color: #000000;
}

.row1 {

  width: 100%;
  padding: 1rem 3rem;
  display: flex;
  flex: 0 0 auto;
  justify-content: space-between;

  .storeBox {
    display: flex;
    flex: 0 0 auto;

    .positionIcon {
      width: 26px;
      height: 36px;
    }

    .storeName2 {
      width: 160px;
      height: 25px;
      font-family: SourceHanSansCN-Medium;
      font-size: 26px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      letter-spacing: 0px;
      color: #000000;
    }

    .moreIcon {
      width: 13px;
      height: 23px;
    }
  }

  .address {
    width: 330px;
    height: 24px;
    font-family: SourceHanSansCN-Regular;
    font-size: 24px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 27px;
    letter-spacing: 0px;
    color: #838383;
  }

  .way {
    display: flex;
    flex: 0 0 auto;
    justify-self: center;
    align-items: center;

    .self {
      width: 85px;
      height: 47px;
      background-color: #333333;
      border-radius: 24px;

      display: flex;
      flex: 0 0 auto;
      justify-content: center;
      align-items: center;

      font-family: SourceHanSansCN-Regular;
      font-size: 24px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      letter-spacing: 0px;
      color: #ffffff;
    }

    .out {
      width: 48px;
      height: 24px;
      font-family: SourceHanSansCN-Regular;
      font-size: 24px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      letter-spacing: 0px;
      color: #838383;
    }
  }

}

.banner {
  width: 100%;
  //height: 201px;
  padding: 1rem 3rem;
  //background-color: #9ed710;
  border-radius: 12px;
}

.row3 {
  width: 100%;
  padding: 0 3rem;
  display: flex;
  flex: 0 0 auto;

  .menuGroup {
    width: 96px;
    //height: 884px;
    font-family: SourceHanSansCN-Bold;
    font-size: 24px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 84px;
    letter-spacing: 0px;
    color: #000000;
  }

  .foodList {
    width: 100%;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    flex: 1;


    .group {
      width: 10rem;
      height: 30px;
      font-family: SourceHanSansCN-Regular;
      font-size: 24px;
      font-weight: normal;
      font-stretch: normal;
      letter-spacing: 0px;
      color: #000000;
    }

    .foodBox {
      display: flex;
      flex: 0 0 auto;
      padding: 1rem 0;

      .foodImg {
        width: 6rem;
        height: 6rem;
        border-radius: 12px;
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
          letter-spacing: 0px;
          color: #000000;
        }

        .foodDesc {
          //height: 1rem;
          padding: 0.1rem 0.5rem;
          font-family: SourceHanSansCN-Regular;
          font-weight: normal;
          font-stretch: normal;
          letter-spacing: 0px;
          color: #bbbbbb;
        }

        .priceBox {
          display: flex;
          flex: 0 0 auto;
          justify-content: space-between;
          align-items: center;

          .foodPrice {
            //width: 59px;
            //height: 23px;
            font-family: SourceHanSansCN-Bold;
            font-size: 1.8rem;
            font-weight: normal;
            font-stretch: normal;
            //line-height: 84px;
            letter-spacing: -1px;
            color: #ff0000;
          }

          .iconAdd {
            width: 32px;
            height: 32px;
            background-color: #9ed710;
            border-radius: 12px;
          }
        }

      }
    }
  }
}

</style>