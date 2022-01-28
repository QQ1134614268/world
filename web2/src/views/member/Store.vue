<template>
  <div class="container p_c_HolyGrail-content">
    <div class="">
      菜单分类
      <ul>

        <li><a href="#miao">去找喵星人</a></li>

        <li><a href="#wang">去找汪星人</a></li>

        <li><a href="#meng">其他萌物</a></li>

      </ul>
    </div>
    <div>
      商品信息
      <div v-for="(obj, index) in goodList ">
        obj
      </div>
      <a name="miao"></a><!--设置锚点方法1-->

      <h3 id="miao">喵星人基地</h3><!--设置锚点方法2-->

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>

      <p>喵喵喵~</p>


      <a name="wang"></a>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <p>汪汪汪~</p>

      <a name="meng"></a>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>

      <p>萌萌萌~</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Store",
  data() {
    return {
      goodList: [
        {
          type: "主食",
          name: "大米",
          img: "",
          price: "",
        },
        {
          type: "主食",
          name: "馒头",
          img: "",
          price: "",
        },
        {
          type: "饮料",
          name: "青岛",
          img: "",
          price: "",
        },
        {
          type: "饮料",
          name: "矿泉水",
          img: "",
          price: "",
        },
      ],
      // goodList2: [
      //   {
      //     type: "主食",
      //     name: "大米",
      //     img: "",
      //     price: "",
      //   },
      //   {
      //     type: "主食",
      //     name: "馒头",
      //     img: "",
      //     price: "",
      //   },
      //   {
      //     type: "饮料",
      //     name: "青岛",
      //     img: "",
      //     price: "",
      //   },
      //   {
      //     type: "饮料",
      //     name: "矿泉水",
      //     img: "",
      //     price: "",
      //   },
      // ]
    }
  },
  methods() {

  }
}
</script>

<style scoped>

</style>