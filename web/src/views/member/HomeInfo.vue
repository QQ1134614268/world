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
  width: 750px;
  height: 582px;
  background-color: #9ad600;
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  justify-content: flex-end;
  align-items: center;
  background-image: url('~@/assets/切图/首页/banner.png');

  .row1Txt {
    width: 685px;
    height: 145px;
    background-color: #ffffff;
    box-shadow: 0 3px 16px 0 rgba(0, 0, 0, 0.15);
    border-radius: 12px;
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    justify-content: space-around;

    .join {
      width: 371px;
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
      width: 204px;
      height: 26px;
      font-family: SourceHanSansCN-Normal;
      font-size:  1.6rem;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      //letter-spacing: 3px;
      color: #000000;

    }

    .logo {
      width: 71px;
      height: 107px;
    }

    .joinGroup {
      width: 157px;
      height: 58px;
      background-color: #9ad600;
      border-radius: 29px;
      display: flex;
      flex: 0 0 auto;
      justify-content: center;
      align-items: center;

      font-family: SourceHanSansCN-Regular;
      font-size: 26px;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      letter-spacing: 0;
      color: #ffffff;
    }
  }
}

.row2 {
  width: 685px;
  height: 180px;
  background-color: #ffffff;
  box-shadow: 0 3px 16px 0 rgba(0, 0, 0, 0.15);
  border-radius: 12px;
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
      width: 42px;
      height: 48px;
    }

    .numName {
      //width: 57px;
      height:  1.6rem;
      font-family: SourceHanSansCN-Medium;
      font-size: 28px;
      font-weight: normal;
      font-stretch: normal;
      line-height:  1.6rem;
      //letter-spacing: 3px;
      color: #000000;
      text-align: center;
    }

    .num {
      width: 65px;
      height: 20px;
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
    width: 334px;
    height: 322px;
    background-color: #ffffff;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    flex: 0 0 auto;
    justify-content: center;

    .order {
      display: flex;
      flex: 0 0 auto;
      align-items: center;

      .orderName {
        //width: 185px;
        height: 36px;
        padding: 0.3rem;
        font-family: SourceHanSansCN-Medium;
        font-size: 38px;
        font-weight: normal;
        font-stretch: normal;
        line-height:  1.6rem;
        letter-spacing: 0;
        color: #000000;
      }

      .moreIcon {
        width: 10px;
        height: 16px;
      }
    }

    .orderImg {
      width: 137px;
      height: 150px;
      align-self: center;
    }
  }
}

.row4 {
  display: flex;
  flex: 0 0 auto;

  .activityTotal {
    width: 260px;
    display: flex;
    flex-direction: column;
    flex: 0 0 auto;

    .activityBox {
      width: 260px;
      height: 134px;
      background-color: #ffffff;
      border-radius: 12px;
      display: flex;
      flex: 0 0 auto;
      flex-direction: column;
      align-items: center;

      .activityImg {
        width: 66px;
        height: 60px;
        background-image: linear-gradient(-27deg,
        #a6e603 0%,
        #d1f302 50%,
        #fcff00 100%);
      }

      .activityText {
        width: 128px;
        height: 31px;
        font-family: SourceHanSansCN-Regular;
        font-size: 32px;
        font-weight: normal;
        font-stretch: normal;
        line-height:  1.6rem;
        letter-spacing: 0;
        color: #000000;
      }

    }

  }

  .secBox {
    width: 407px;
    height: 284px;
    background-color: #ffffff;
    border-radius: 12px;

    display: flex;
    flex-direction: column;
    flex: 0 0 auto;

    .secText {
      display: flex;
      flex: 0 0 auto;

      .time {
        width: 136px;
        height: 33px;
        font-family: SourceHanSansCN-Bold;
        font-size: 34px;
        font-weight: normal;
        font-stretch: normal;
        line-height:  1.6rem;
        letter-spacing: 0;
        color: #000000;
      }

      .note {
        width: 120px;
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
          width: 172px;
          height: 130px;
          background-color: #e7ffdd;
          border-radius: 10px;
        }

        .priceBox {
          display: flex;
          flex: 0 0 auto;

          .secPrice {
            width: 69px;
            height: 23px;
            font-family: SourceHanSansCN-Bold;
            font-size: 30px;
            font-weight: normal;
            font-stretch: normal;
            line-height:  1.6rem;
            letter-spacing: 0;
            color: #ff0000
          }

          .price {
            width: 32px;
            height: 18px;
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