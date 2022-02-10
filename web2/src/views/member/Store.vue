<template>
  <div>
    <div>
      <router-link to="/videoAdmin/GoodsList"> 菜单列表</router-link>
    </div>
    <BoxFlex>
      <div>
        <div :key="index" v-for="(obj,index) in goodsList">
          <li><a :href="'#'+obj.type">{{ obj.type }}</a></li>
        </div>
      </div>
      <div>
        <div :key="index" v-for="(obj,index) in goodsList" style="height: 50rem">
          <a :id="obj.type" style="height: 1.6rem; font-weight: bold" >{{ obj.type }}</a>
          <div :key="index2" v-for="(obj2, index2) in obj.data">
            <div>
              <el-image :src="obj2.img"></el-image>
              <div>
                {{ obj2.name }}
              </div>
              <div>
                售价: {{ obj2.price }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </BoxFlex>
  </div>
</template>

<script>
export default {
  name: "Store",
  data() {
    return {
      goodsList: [
        {
          type: "主食",
          data: [
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
          ]
        },
        {
          type: "饮料",
          data: [
            {
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
          ]
        }
      ],
    }
  },
  methods: {
  }
}
</script>

<style scoped>
p {
  height: 20rem;
}
</style>