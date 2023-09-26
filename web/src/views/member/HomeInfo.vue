<template>
  <div class="container">
    <div class="row1">
      <div class="row1Txt">
        <div>
          <div class="join">
            Join the group to get coupons
          </div>
          <div class="joinName">
            入群即得优惠券
          </div>
        </div>
        <div class="logo">
          <img src="@/assets/切图/首页/图层21.png">
        </div>
        <div class="joinGroup">
          立即入群
        </div>
      </div>
    </div>
    <div class="row2">
      <div class="numBox">
        <img class="numIcon" src="@/assets/切图/首页/余额.png">
        <div class="numName">
          余额
        </div>
        <div class="num">
          34.02
        </div>
      </div>
      <div class="numBox">
        <img class="numIcon" src="@/assets/切图/首页/积分.png">
        <div class="numName">
          积分
        </div>
        <div class="num">
          843
        </div>
      </div>
      <div class="numBox">
        <img class="numIcon" src="@/assets/切图/首页/券.png">
        <div class="numName">
          优惠券
        </div>
        <div class="num">
          3
        </div>
      </div>
    </div>
    <div class="row3">
      <div class="orderBox">
        <div class="order">
          <div class="orderName">立即点餐</div>
          <img class="moreIcon" src="@/assets/切图/首页/形状2.png">
        </div>
        <img class="orderImg" src="@/assets/切图/首页/图层23.png"/>
      </div>
      <div class="orderBox">
        <div class="order">
          <div class="orderName">会员码</div>
          <img class="moreIcon" src="@/assets/切图/首页/形状2.png">
        </div>
        <img class="orderImg" src="@/assets/切图/首页/扫码.png"/>
      </div>
    </div>
    <div class="row4">
      <div class="activityTotal">
        <div class="activityBox">
          <img class="activityImg" src="@/assets/切图/首页/图层23.png">
          <div class="activityText">超值券包</div>
        </div>
        <div class="activityBox">
          <img class="activityImg" src="@/assets/切图/首页/图层23.png">
          <div class="activityText">企业团餐</div>
        </div>
      </div>
      <div class="secBox">
        <div class="secText">
          <div class="time">限时秒杀</div>
          <div class="note">今日已结束</div>
        </div>
        <div class="secTotal">
          <div class="secInfo">
            <img class="secImg" src="@/assets/切图/首页/图层23.png">
            <div class="priceBox">
              <div class="secPrice">￥5.9</div>
              <div class="price">￥9</div>
            </div>
          </div>
          <div class="secInfo">
            <img class="secImg" src="@/assets/切图/首页/图层23.png">
            <div class="priceBox">
              <div class="secPrice">￥5.9</div>
              <div class="price">￥9</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

</script>

<style scoped lang="less">
.container {
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  align-items: center;
}

.row1 {
  width: 100%;
  height: 20rem;
  background-color: #9ad600;
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  justify-content: flex-end;
  align-items: center;
  background-image: url('~@/assets/切图/首页/banner.png');
  //background-size: contain;

  .row1Txt {
    width: 42rem;
    height: 9rem;
    background-color: #ffffff;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);
    border-radius: 0.75rem;
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    justify-content: space-around;

    .join {
      width: 23rem;
      height:  1.5rem;
      font-family: zihun54hao-xianhei;
      font-size:  1.5rem;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      letter-spacing: 0;
      color: #000000;
    }

    .joinName {
      width:  12.75rem;
      height:  1.625rem;
      font-family: SourceHanSansCN-Normal;
      font-size:  1.6rem;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      //letter-spacing: 0.2rem;
      color: #000000;

    }

    .logo {
      width: 4.5rem;
      height: 6.8rem;
    }

    .joinGroup {
      width: 10rem;
      height: 3.625rem;
      background-color: #9ad600;
      border-radius: 2rem;
      display: flex;
      flex: 0 0 auto;
      justify-content: center;
      align-items: center;

      font-family: SourceHanSansCN-Regular;
      font-size:  1.625rem;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      letter-spacing: 0;
      color: #ffffff;
    }
  }
}

.row2 {
  width: 42rem;
  height: 12rem;
  background-color: #ffffff;
  box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);
  border-radius:  0.75rem;
  display: flex;
  flex: 0 0 auto;
  justify-content: space-around;

  .numBox {
    display: flex;
    flex-direction: column;
    flex: 0 0 auto;
    justify-content: center;
    align-items: center;

    .numIcon {
      width: 2.625rem;
      height: 3rem;
    }

    .numName {
      height:  1.6rem;
      font-family: SourceHanSansCN-Medium;
      font-size: 1.75rem;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      //letter-spacing: 0.2rem;
      color: #000000;
      text-align: center;
    }

    .num {
      width: 4rem;
      height: 1.25rem;
      font-family: SourceHanSansCN-Regular;
      font-size:  1.6rem;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      //letter-spacing: 0;
      color: #838383;
      text-align: center;
    }
  }
}

.row3 {
  display: flex;
  flex: 0 0 auto;

  .orderBox {
    width: 20rem;
    height: 20rem;
    background-color: #ffffff;
    border-radius:  0.75rem;
    display: flex;
    flex-direction: column;
    flex: 0 0 auto;
    justify-content: center;

    .order {
      display: flex;
      flex: 0 0 auto;
      align-items: center;

      .orderName {
        height:2.25rem;
        padding: 0.3rem;
        font-family: SourceHanSansCN-Medium;
        font-size: 2.375rem;
        font-weight: normal;
        font-stretch: normal;
        line-height:  1.6rem;
        letter-spacing: 0;
        color: #000000;
      }

      .moreIcon {
        width: 0.625rem;
        height: 1rem;
      }
    }

    .orderImg {
      width: 8.5rem;
      height: 9.3rem;
      align-self: center;
    }
  }
}

.row4 {
  display: flex;
  flex: 0 0 auto;

  .activityTotal {
    width: 16.25rem;
    display: flex;
    flex-direction: column;
    flex: 0 0 auto;

    .activityBox {
      width: 16.25rem;
      height: 8.5rem;
      background-color: #ffffff;
      border-radius:  0.75rem;
      display: flex;
      flex: 0 0 auto;
      flex-direction: column;
      align-items: center;

      .activityImg {
        width: 4.125rem;
        height: 3.75rem;
        background-image: linear-gradient(-27deg,
        #a6e603 0%,
        #d1f302 50%,
        #fcff00 100%);
      }

      .activityText {
        width: 11.75rem;
        height: 2rem;
        font-family: SourceHanSansCN-Regular;
        font-size: 2rem;
        font-weight: normal;
        font-stretch: normal;
        line-height:  1.6rem;
        letter-spacing: 0;
        color: #000000;
      }

    }

  }

  .secBox {
    width: 25.5rem;
    height: 17.8rem;
    background-color: #ffffff;
    border-radius:  0.75rem;

    display: flex;
    flex-direction: column;
    flex: 0 0 auto;

    .secText {
      display: flex;
      flex: 0 0 auto;

      .time {
        width: 8.5rem;
        height: 2rem;
        font-family: SourceHanSansCN-Bold;
        font-size: 2rem;
        font-weight: normal;
        font-stretch: normal;
        line-height:  1.6rem;
        letter-spacing: 0;
        color: #000000;
      }

      .note {
        width: 7.5rem;
        height:  1.5rem;
        font-family: SourceHanSansCN-Regular;
        font-size:  1.5rem;
        font-weight: normal;
        font-stretch: normal;
        line-height:  1.6rem;
        letter-spacing: 0;
        color: #a3a3a3;
      }
    }

    .secTotal {
      display: flex;
      flex: 0 0 auto;

      .secInfo {
        .secImg {
          width: 1.8rem;
          height: 8.2rem;
          background-color: #e7ffdd;
          border-radius: 0.625rem;
        }

        .priceBox {
          display: flex;
          flex: 0 0 auto;

          .secPrice {
            width: 4.5rem;
            height: 1.4rem;
            font-family: SourceHanSansCN-Bold;
            font-size: 1.875rem;
            font-weight: normal;
            font-stretch: normal;
            line-height:  1.6rem;
            letter-spacing: 0;
            color: #ff0000
          }

          .price {
            width: 2rem;
            height: 1.2rem;
            font-family: SourceHanSansCN-Regular;
            font-size:  1.5rem;
            font-weight: normal;
            font-stretch: normal;
            line-height:  1.6rem;
            letter-spacing: 0;
            color: #a0a0a0;
          }
        }
      }
    }
  }
}
</style>