<template>
  <div class="container">
    <img :src="url" class="img">
  </div>
</template>

<script lang="ts" setup>
import { IP } from '@/constants'

const url = "http://" + IP + ":1234/?action=stream"

</script>

<style scoped>
.container {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  position: fixed;
  width: 100%;
  height: 100%;
}

.img {
  display: block;
  width: 100%;
  height: 100%;
}
</style>
