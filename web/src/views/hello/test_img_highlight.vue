<template>
  <div>
    <img @click="highlight( $event)" src="@/assets/icon/favicon2.jpg">
    <img @click="highlight( $event)" src="@/assets/icon/favicon2.jpg">
    <img @click="highlight( $event)" src="@/assets/icon/favicon2.jpg" class="filter:brightness(1.4)">
    <!--      <li v-for="(item, index) in sortedList"-->
    <!--              class="clearfix hoverStyle"-->
    <!--              @click="handleClickTypeItem($event, index)" >-->
    <!--              <span-->
    <!--                v-show="!item.edit"-->
    <!--                class="floatLeft"-->
    <!--                :class="{ active: selectIndex == index }" >-->
    <!--                {{ item.groupName }}-->
    <!--             </span>-->
    <!--     li/> -->
  </div>
</template>
<script>

export default {
  name: 'Home',
  data() {
    return {}
  },
  methods: {
    highlight(event) {
      let el = event.currentTarget;
      el.style.opacity = 1
      el.style.filter = 'brightness(1.4)'

      //      // 给大盒子添加hover事件
      // $("div").hover(function(){
      // //  给每个img添加hover事件
      //            $("img").hover(function(){
      //            // 给当前img添加动动画改变透明度
      //                $(this).stop(true).animate({opacity:1},100)
      //                $(this).siblings().stop(true).animate({opacity:.5})
      //            })
      //        })
      //        // 当鼠标移开大盒子时添加动画改变透明度
      //        $("div").mouseout(function(){
      //            $("img").animate({opacity:1},100)
      //        })
    }
  }
}
</script>
