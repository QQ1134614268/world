<template>
  <div class="container">
    <div class="row1">
      <div class="avtar">
        <img class="avtarImg" src="@/assets/icon/favicon2.jpg">
        <div>
          <div class="avtarName">
            用户昵称
          </div>
          <div class="avtarId">
            1134614268
          </div>
        </div>
      </div>
      <img class="logo" src="@/assets/切图/我的/logo.png">
    </div>
    <div class="row2 p_c_test_border">
      <span class="_77">
        77卡
      </span>
      <span class="_77Text">
        一餐能省4块多，两餐回本
      </span>
      <span class="_77LoginBox">
        <span class="_77Login">
        立即开通
      </span>
      </span>
    </div>
    <div class="row3">
      <div>
        <div class="num">
          34.02
        </div>
        <div class="numName">
          余额
        </div>
      </div>
      <div>
        <div class="num">
          843
        </div>
        <div class="numName">
          积分
        </div>
      </div>
      <div>
        <div class="num">
          3
        </div>
        <div class="numName">
          优惠券
        </div>
      </div>
    </div>
    <div class="row4">
      <div class="discountBox">
        <div class="discount">立享整单88折</div>
        <div class="join">入群一起磕综艺</div>
        <div class="redEnvelope">群内每天红包券，抄底价秒杀</div>
      </div>
    </div>
    <div class="row5">
      <div class="menu">
        <img src="@/assets/切图/我的/订单.png">
        <div>我的订单</div>
      </div>
      <div class="menu">
        <img src="@/assets/切图/我的/拼团.png">
        <div>我的拼团</div>
      </div>
      <div class="menu">
        <img src="@/assets/切图/我的/二维码.png">
        <div>兑换码</div>
      </div>
      <div class="menu">
        <img src="@/assets/切图/我的/发票.png">
        <div>发票管理</div>
      </div>
      <div class="menu">
        <img src="@/assets/切图/我的/惊喜.png">
        <div>暗号惊喜</div>
      </div>
      <div class="menu">
        <img src="@/assets/切图/我的/手机.png">
        <div>修改手机号</div>
      </div>
      <div class="menu">
        <img src="@/assets/切图/我的/设置.png">
        <div>设置</div>
      </div>
      <div class="menu">
        <img src="@/assets/切图/我的/客服.png">
        <div>人工客服</div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "UserSpace",
  data() {
    return {
    }
  }
}
</script>

<style scoped lang="less">
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  .row1 {
    width: 688px;
    height: 300px;
    //display: flex;
    align-items: flex-end;
    justify-content: space-between;
    flex-shrink: 0;

    .avtar {
      display: flex;
      flex: 0 0 auto;
      justify-content: center;
      align-items: center;

      .avtarImg {
        width: 100px;
        height: 100px;
        //background-color: #ffffff;
        border: solid 3px #ffffff;
        border-radius: 50%;
      }

      .avtarName {
        width: 108px;
        height: 27px;
        font-family: SourceHanSansCN-Medium;
        font-size: 28px;
        font-weight: normal;
        font-stretch: normal;
        line-height: 37px;
        letter-spacing: -1px;
        //color: #000000;
      }

      .avtarId {
        width: 152px;
        height: 19px;
        font-family: SourceHanSansCN-Regular;
        font-size: 24px;
        font-weight: normal;
        font-stretch: normal;
        line-height: 37px;
        letter-spacing: 1px;
        color: #b3b2b9;
      }
    }

    .logo {
      width: 103px;
      height: 158px;
    }

  }

  .row2 {
    width: 684px;
    height: 85px;
    background-image: linear-gradient(122deg,
    #252745 0%,
    #494d67 100%),
    linear-gradient(#ffffff,
    #ffffff);
    background-blend-mode: normal,
    normal;
    border-radius: 12px 12px 0px 0px;
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    justify-content: space-around;

    ._77 {
      width: 73px;
      height: 27px;
      font-family: zihun54hao-xianhei;
      font-size: 32px;
      font-weight: normal;
      font-style: italic;
      font-stretch: normal;
      line-height: 27px;
      letter-spacing: -1px;
      color: #ece1e1;
      box-shadow: 0px 2px 5px 0px rgba(103, 63, 22, 0.7);
    }

    ._77Text {
      width: 258px;
      height: 21px;
      font-family: SourceHanSansCN-Normal;
      font-size: 22px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      letter-spacing: 0px;
      color: #ebe5c1;
    }

    ._77LoginBox {
      width: 127px;
      height: 47px;
      background-image: linear-gradient(90deg,
      #fbf1cb 0%,
      #f6d7a7 100%),
      linear-gradient(#9ad600,
      #9ad600);
      background-blend-mode: normal,
      normal;
      border-radius: 24px;
      display: flex;
      flex: 0 0 auto;
      align-items: center;
      justify-content: center;

      ._77Login {
        width: 87px;
        height: 21px;
        font-family: SourceHanSansCN-Medium;
        font-size: 21px;
        font-weight: normal;
        font-stretch: normal;
        line-height: 27px;
        letter-spacing: 0px;
        color: #494d67;
        display: flex;
        flex: 0 0 auto;
        align-items: center;
      }

    }
  }

  .row3 {
    width: 685px;
    height: 150px;
    background-color: #ffffff;
    box-shadow: 0px 3px 16px 0px rgba(0, 0, 0, 0.15);
    border-radius: 12px;

    display: flex;
    flex: 0 0 auto;
    justify-content: space-evenly;
    align-items: center;

    .num {
      width: 84px;
      height: 24px;
      font-family: SourceHanSansCN-Bold;
      font-size: 32px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      letter-spacing: 0px;
      color: #000000;
      text-align: center;
    }

    .numName {
      //width: 50px;
      height: 24px;
      font-family: SourceHanSansCN-Regular;
      font-size: 24px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      letter-spacing: 2px;
      color: #969ab6;
      text-align: center;

    }
  }

  .row4 {
    width: 683px;
    height: 229px;
    //background-image: linear-gradient(245deg,
    //#6f7aad 0%,
    //#5f6994 100%),
    //linear-gradient(#ffffff,
    //#ffffff);
    background-image: url('~@/assets/切图/我的/会员卡.png');
    background-blend-mode: normal,
    normal;
    border-radius: 12px;

    .discountBox {
      margin-left: 250px;
    }

    .discount {
      width: 224px;
      height: 50px;
      font-family: SourceHanSansCN-Bold;
      font-size: 36px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      //letter-spacing: 1px;
      color: #ffffff;
    }

    .join {
      width: 174px;
      height: 23px;
      font-family: SourceHanSansCN-Normal;
      font-size: 24px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      //letter-spacing: 1px;
      color: #ffffff;
    }

    .redEnvelope {
      width: 310px;
      height: 23px;
      font-family: SourceHanSansCN-Bold;
      font-size: 23px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 27px;
      //letter-spacing: 0px;
      color: #9fa2af;
    }
  }

  .row5 {
    width: 683px;
    height: 409px;
    background-color: #ffffff;
    border-radius: 12px;
    display: flex;
    flex: 0 0 auto;
    flex-wrap: wrap;

    .menu {
      width: 25%;
      display: flex;
      flex-direction: column;
      flex: 0 0 auto;
      align-items: center;
      justify-content: center;

      .icon {
        width: 38px;
        height: 48px;
      }

      .iconName {
        width: 102px;
        height: 24px;
        font-family: SourceHanSansCN-Regular;
        font-size: 26px;
        font-weight: normal;
        font-stretch: normal;
        line-height: 27px;
        letter-spacing: 0px;
        color: #000000;
      }
    }
  }

}
</style>