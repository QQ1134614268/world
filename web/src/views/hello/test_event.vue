<template>
  <div>

    <!-- 使用  .stop  阻止冒泡 -->
    <div class="inner" @click="div1Handler">
      <input type="button" value="点击" @click="btnHandler"/>
    </div>


    <!--     使用  .provent 阻止默认行为 -->
    <a href="http://baidu.com" @click.prevent="linkClick">百度一下</a>

    <!--使用  .capture  实现捕获触发机制  -->
    <div class="inner" @click.capture="div1Handler">
      <input type="button" value="点击" @click="btnHandler"/>
    </div>

    <!-- 使用  .self  實現只有点击只有点击当前元素时候，才会触发事件处理函数 -->
    <div class="inner" @click.self="div1Handler">
      <input type="button" value="点击" @click="btnHandler"/>
    </div>

    <!-- 使用  .once  只触发一次事件处理函数 -->
    <!-- 即按照下面的例子，第一次低级不跳转，第二次才跳转 -->
    <a href="http://baidu.com" @click.prevent.once="linkClick">百度一下</a>

    <!-- 演示： .stop  和  .self  的区别 -->
    <div class="outer" @click="div2Handler">
      <div class="inner" @click="div1Handler">
        <input type="button" value="点击" @click="btnHandler"/>
      </div>
    </div>

    <!-- .self只会阻止自己身上的冒泡，并不会真正阻止冒泡-->
    <div class="outer" @click="div2Handler">
      <div class="inner" @click.self="div1Handler">
        <input type="button" value="点击" @click="btnHandler"/>
      </div>
    </div>
    <!-- 触发了bt按钮的点击事件触发了outer div的点击事件-->
  </div>
</template>

<script>
export default {
  name: "test_event",
  methods: {
    div1Handler() {
      console.log('触发了inner div的点击事件');
    },
    div2Handler() {
      console.log('触发了outer div的点击事件');
    },
    btnHandler() {
      console.log('触发了bt按钮的点击事件');
    },
    linkClick() {
      console.log('触发了链接');
    }
  }
}
</script>
<style type="text/css" scoped>
.inner {
  height: 150px;
  background-color: gray;
}

.outer {
  padding: 40px;
  background: blue;
}
</style>