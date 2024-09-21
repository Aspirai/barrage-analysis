<template>

</template>

<script>
export default {
  data() {
    return {
      hour: 0,
      minute: 0,
      second: 0
    };
  },
  mounted() {
    this.interval = setInterval(() => {
      const date = new Date();
      this.hour = date.getHours();
      this.minute = date.getMinutes();
      this.second = date.getSeconds();
    }, 1000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
  }
};
</script>

<style>
#clock {
  color: #fff;
  font-size: 36px;
}
</style>