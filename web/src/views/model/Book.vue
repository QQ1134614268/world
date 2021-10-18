<template>
  <div>
    <div class="title">
      {{ obj.title }}
    </div>
    <div class="block">
      <div v-for="(item , index) in obj.prove">
        <span>{{ index }}</span> {{ item }}
      </div>
    </div>
    <div class="block">
      <div v-for="(item , index) in obj.story">
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
        prove: ["论点1", "论点2", "论点3"],
        story: ["故事1", "故事2", "故事3",]
      }

    }
  }
}
</script>

<style scoped>

</style>