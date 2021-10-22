<template>
  <div>
    <div class="title">
      {{ obj.value }}
    </div>
    <div class="block">
      <div>
        <button @click="addProve">添加</button>
        <button @click="editProve">编辑</button>
        <router-link :to="{name:'/model/AddProve',params: {id:this.id,value:this.obj.value}}">
          <button>添加</button>
        </router-link>
      </div>
      <div v-for="(item , index) in prove">
        <span>{{ index }}</span> {{ item.value }}
      </div>
    </div>
    <div class="block">
      <div v-for="(item , index) in story">
        <span>{{ index }}</span> {{ item.value }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Book",
  data() {
    return {
      obj: {
        value: "希洛之书",
      },
      prove: [
        {
          value: "论点1",
        },
        {
          value: "论点2",
        },
        {
          value: "论点3",
        }
      ],
      story: [
        {
          value: "故事1",
        },
        {
          value: "故事2",
        },
        {
          value: "故事3",
        }],
      url: "/api/model_api/ProveApi",
      url2: "/api/model_api/StoryApi",
      id: 1,
    }
  },
  methods: {
    async get_data() {
      let res1 = await this.$get2(this.url, this.id, {});

      let res2 = await this.$get2(this.url, 0, {"parent_id": this.id});
      let res3 = await this.$get2(this.url2, 0, {"parent_id": this.id});
      if (res1.data.code == 1) {
        this.obj = res1.data.data
      } else {
        this.$message('失败');
      }

      if (res3.data.code == 1) {
        this.prove = res2.data.data
      } else {
        this.$message('失败');
      }
      if (res3.data.code == 1) {
        this.story = res3.data.data
      } else {
        this.$message('失败');
      }
    },
    async addProve() {
      await this.$router.push({path: '/model/AddProve'})
    },
    editProve() {
      this.$router.push({path: '/model/EditProve'})
    }
  },
  created() {
    this.get_data();
  }
}
</script>

<style scoped>

</style>