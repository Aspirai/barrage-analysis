<template>
  <div class="login">
    <RouterView></RouterView>
  </div>
</template>

<script lang="ts">
  import Person from './components/Person.vue';
  // 暴露组件
  export default {
    name: 'App',//组件名
    components:{Person} //注册组件
  }
  import { RouterView } from 'vue-router';
</script>

<style scoped>
</style>
