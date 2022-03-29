<template>
  <div>
    <div class="main">
      <img alt="" class="logo" src="pic.jpg">
      <div class="content">
        <h4 class="name">a name</h4>
        <p class="info">a info</p>
        <p class="notice">This is notice content.</p>
      </div>
    </div>
  </div>
</template>


<style scoped>

.main {
  display: flex;
}

.logo {
  width: 100px;
  height: 100px;
  margin: 10px;
}

.content {
  flex: 1;
}

.content > * {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.hello {
  display: flex;
  /*水平:justify-content 垂直:align-items */
  /*justify-content: space-between;*/
  /* 主轴展现方式 flex-start flex-end; center space-around; space-between;*/
  /*align-content: flex-start;*/

  align-items: flex-start;
  /* 侧展现方式 stretch flex-start flex-end;baseline center;*/
  height: 20rem;
  /*flex-grow: 1;*/
  /*flex-shrink: 2;*/
  /*flex-basis: 2px;*/
  /*flex 是 flex-grow,flex-shrink,flex-basis的缩写; flex-flow 是 flex-direction flex-wrap缩写*/
  /*flex :2 = flex-grow:2*/
}

</style>
<script>
export default {
  name: 'Home',
  data() {
    return {
      webSite: 'world',
      msg: 'Hello world',

    }
  }
}
</script>
