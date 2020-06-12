<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  body{
    margin: 0;
    padding: 0;
    border: 0;
  }
  .el-textarea__inner {
    background-color: #2F2F2F;
    color: #78cf8a;;
    font-size: 15px;
    line-height: 1.4;
}
#app {
  margin: 0;
  padding: 0;
}
</style>
