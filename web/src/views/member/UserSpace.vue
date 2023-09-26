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
    <div class="row2">
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
  padding: 0 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  .row1 {
    width: 100%;
    padding: 1rem 2rem;
    height: 8rem;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    flex-shrink: 0;

    .avtar {
      display: flex;
      flex: 0 0 auto;
      justify-content: center;
      align-items: center;

      .avtarImg {
        width: 6rem;
        height: 6rem;
        //background-color: #ffffff;
        border: solid 0.2rem #ffffff;
        border-radius: 50%;
      }

      .avtarName {
        width: 20rem;
        height: 3rem;
        font-family: SourceHanSansCN-Medium;
        font-size: 2rem;
        font-weight: normal;
        font-stretch: normal;
        line-height: 2.2rem;
        letter-spacing: 0;
        //color: #000000;
      }

      .avtarId {
        width: 20rem;
        height: 2rem;
        font-family: SourceHanSansCN-Regular;
        font-size: 1rem;
        font-weight: normal;
        font-stretch: normal;
        line-height: 2rem;
        letter-spacing: 0;
        color: #b3b2b9;
      }
    }

    .logo {
      width: 6rem;
      height: 6rem;
      object-fit: contain;
    }
  }

  .row2 {
    width: 100%;
    height: 6rem;
    margin-bottom: 1rem;
    background-image: linear-gradient(122deg, #252745 0%, #494d67 100%), linear-gradient(#ffffff, #ffffff);
    background-blend-mode: normal, normal;
    border-radius: 0.8rem 0.8rem 0 0;
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    justify-content: space-around;

    ._77 {
      width: 5rem;
      height: 1.6rem;
      font-family: zihun54hao-xianhei;
      font-size: 2rem;
      font-weight: normal;
      font-style: italic;
      font-stretch: normal;
      line-height: 2rem;
      letter-spacing: 0;
      color: #ece1e1;
      box-shadow: 0 0.1rem 0.3rem 0 rgba(103, 63, 22, 0.7);
    }

    ._77Text {
      width: 20rem;
      height: 1.6rem;
      font-family: SourceHanSansCN-Normal;
      font-size: 1.6rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      letter-spacing: 0;
      color: #ebe5c1;
    }

    ._77LoginBox {
      width: 8rem;
      height: 3rem;
      background-image: linear-gradient(90deg, #fbf1cb 0%, #f6d7a7 100%), linear-gradient(#9ad600, #9ad600);
      background-blend-mode: normal, normal;
      border-radius: 1.5rem;
      display: flex;
      flex: 0 0 auto;
      align-items: center;
      justify-content: center;

      ._77Login {
        width: 8rem;
        height: 1.4rem;
        font-family: SourceHanSansCN-Medium;
        font-size: 1.4rem;
        font-weight: normal;
        font-stretch: normal;
        line-height: 1.6rem;
        letter-spacing: 0;
        color: #494d67;
        display: flex;
        flex: 0 0 auto;
        align-items: center;
        justify-content: center;
      }

    }
  }

  .row3 {
    width: 100%;
    height: 10rem;
    margin-bottom: 1rem;
    background-color: #ffffff;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);
    border-radius: 0.8rem;

    display: flex;
    flex: 0 0 auto;
    justify-content: space-evenly;
    align-items: center;

    .num {
      width: 6rem;
      height: 1.5rem;
      font-family: SourceHanSansCN-Bold;
      font-size: 2rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      letter-spacing: 0;
      color: #000000;
      text-align: center;
    }

    .numName {
      height: 1.5rem;
      font-family: SourceHanSansCN-Regular;
      font-size: 1.5rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      letter-spacing: 0;
      color: #969ab6;
      text-align: center;

    }
  }

  .row4 {
    width: 100%;
    height: 14rem;
    margin-bottom: 1rem;
    background-image: url('~@/assets/切图/我的/会员卡.png');
    background-blend-mode: normal, normal;
    border-radius: 0.8rem;

    .discountBox {
      margin-left: 40%;
      display: flex;
      flex-direction: column;
      padding: 3rem 0;
    }

    .discount {
      width: 20rem;
      height: 3rem;
      font-family: SourceHanSansCN-Bold;
      font-size: 2rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      color: #ffffff;
    }

    .join {
      width: 20rem;
      height: 1.5rem;
      font-family: SourceHanSansCN-Normal;
      font-size: 1.5rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      color: #ffffff;
    }

    .redEnvelope {
      width: 20rem;
      height: 1.5rem;
      font-family: SourceHanSansCN-Bold;
      font-size: 1.5rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 1.6rem;
      //letter-spacing: 0;
      color: #9fa2af;
    }
  }

  .row5 {
    width: 100%;
    height: 25rem;
    margin-bottom: 1rem;
    background-color: rgba(243, 239, 239, 0.43);
    border-radius: 1rem;
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
        width: 3rem;
        height: 3rem;
      }

      .iconName {
        width: 6rem;
        height: 1.5rem;
        font-family: SourceHanSansCN-Regular;
        font-size: 1.6rem;
        font-weight: normal;
        font-stretch: normal;
        line-height: 1.6rem;
        letter-spacing: 0;
        color: #000000;
      }
    }
  }
}
</style>