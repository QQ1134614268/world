<template>
  <div>
    //右上角查看规则
    <div>
      <a class="rule" href="javascript:;" @click="showpopup">弹出</a>
    </div>
    <!--        //弹窗模块-->
    <div v-show="popup" @click="closepopup">
      <!--这里是半透明背景层-->
      <div class="over"></div>
      <!--这里是要展示的内容层-->
      <div class="login">
        1.这是规则说明；<br>
        2.打王者不要射手走边路，会被越塔；<br>
        3.请参考第二条；
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      popup: 0,
    };
  },

  methods: {
    //打开活动规则页面
    showpopup() {
      this.popup = 1;
    },
    //关闭活动规则页面
    closepopup() {
      this.popup = 0;
    },
  }
};
</script>

<style scoped>


/*这里面可以自定义字体样式等，都是CSS基础*/
.rule {
  /*position: absolute;*/
  width: 0.82rem;
  height: 0.36rem;
  top: 0.08rem;
  right: 0rem;
  background: #111111;
}

.login {
  position: fixed;
  font-size: 24px;
  height: 35rem;
  width: 15rem;
  background-color: gold;
  border-radius: 0.25rem;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000;
}

.over {
  position: fixed;
  width: 100%;
  height: 100%;
  opacity: 0.7;
  /* 透明度为70 % */
  filter: alpha(opacity=70);
  top: 0;
  left: 0;
  z-index: 999;
  background-color: #111111;
}

</style>
