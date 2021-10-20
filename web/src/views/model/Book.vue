<template>
  <div>
    <div class="title">
      {{ obj.title }}
    </div>
    <div class="block">
      <div v-for="(item , index) in prove">
        <span>{{ index }}</span> {{ item }}
      </div>
    </div>
    <div class="block">
      <div v-for="(item , index) in story">
        <span>{{ index }}</span> {{ item }}
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
        title: "希洛之书",
      },
      prove: ["论点1", "论点2", "论点3"],
      story: ["故事1", "故事2", "故事3",],
      url: "/api/model_api/ProveApi",
      url2: "/api/model_api/StoryApi",
      _id: 0,
    }
  },
  methods: {
    async get_data() {
      let vo1 = this.$get2(this.url, this._id, {});
      let vo2 = this.$get2(this.url, 0, {"parent_id": this._id});
      let vo3 = this.$get2(this.url2, 0, {"parent_id": this._id});
      this.obj = vo1
      this.prove = vo2
      this.story = vo3
    }
  },
  created() {
    this.get_data();
  }
}
</script>

<style scoped>

</style>