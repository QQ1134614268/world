<template>
  <div class="member_container">
    <div class="member_body">
      <router-view/>
    </div>
    <div class="member_footer">
      <div class="menuBox" @click="goTo(MemberRootUrl)">
        <img class="menuImg" src="@/assets/切图/首页/首页.png">
        <div class="menuText">首页</div>
      </div>
      <div class="menuBox" @click="goTo(OrderInfo)">
        <img class="menuImg" src="@/assets/切图/首页/餐饮.png">
        <div class="menuText">点餐</div>
      </div>
      <div class="menuBox" @click="goTo(UserSpace)">
        <img class="menuImg" src="@/assets/切图/首页/我的.png">
        <div class="menuText">我的</div>
      </div>
    </div>
  </div>
</template>
<script>
import {userLogout} from "@/api/user";
import {FoodInfo, HomeContent, MemberAdminHome, MemberRootUrl, Store, UserSpace} from "@/views/member/index";
import {SYS_LOGIN_URL, SYS_REGISTER_URL} from "@/views/sys";

export default {
  name: "Home",
  data() {
    return {
      MemberRootUrl,
      Store,
      MemberAdminHome,
      SYS_LOGIN_URL,
      SYS_REGISTER_URL,
      OrderInfo: FoodInfo,
      UserSpace,
      HomeContent,
      menuList: [
        {name: "首页", path: HomeContent},
        {name: "点餐", path: HomeContent},
        {name: "我的", path: UserSpace},
      ],
      store_id: 1,
      // home_icon: require('/assets/img/image1.jpeg')
    }
  },
  computed: {
    user() {
      return this.$store.state.userInfo
    }
  },
  methods: {
    async logout() {
      await userLogout()
    },
    goTo(url) {
      this.$router.push(url)
    }
  }
}
</script>
<style scoped lang="less">
.member_container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;

  @media only screen and (min-width: 768px) {
    width: 768px;
  }
  @media only screen and (max-width: 768px) {
    width: 100%;
  }
}

.member_body {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  flex-shrink: 1;
  overflow-y: scroll;
}

.member_footer {
  width: 100%;
  height: 8rem;
  background-image: linear-gradient(#ffffff, #ffffff), linear-gradient(#ffffff, #ffffff);
  background-blend-mode: normal, normal;
  box-shadow: 0 -0.1875rem 0.5rem 0 rgba(48, 45, 43, 0.21);

  display: flex;
  flex: 0 0 auto;
  justify-content: space-evenly;
  align-items: center;

  //height: 3rem;
  //background: linear-gradient(to top, #f3f3f3, #cccccc, #f3f3f3);
  .menuBox {
    display: flex;
    flex-direction: column;
    flex: 0 0 auto;
    align-items: center;

    .menuImg {
      width: 3rem;
      height: 3rem;
      //background-image: linear-gradient(-27deg,
      //#9ad600 0%,
      //#cffe58 100%);
      object-fit: scale-down;
    }

    .menuText {
      height: 2.4rem;
      font-family: SourceHanSansCN-Medium;
      font-size: 2rem;
      font-weight: normal;
      font-stretch: normal;
      line-height: 2.4rem;
      letter-spacing: 0;
      color: #9ad600;
    }
  }

}

//.footer131 {
//  /*width: 23rem;*/
//  height: 5rem;
//  background-image: linear-gradient(#ffffff, #ffffff), linear-gradient(#ffffff, #ffffff);
//  background-blend-mode: normal, normal;
//  box-shadow: 0rem 0rem 0rem 0rem rgba(48, 45, 43, 0.21);
//}

//footer div:nth-child(n+2) {
//}


</style>
