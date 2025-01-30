<template>
  <div class="app">
    <my-header class="main_header"/>
    <router-view></router-view>
  </div>
</template>


<script>

</script>


<style>

  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  .main_header {
    z-index: 1000;
    top: 0;
    position: sticky;
  }

</style>
