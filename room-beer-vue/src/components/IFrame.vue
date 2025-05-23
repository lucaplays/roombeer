<template>
  <div class="iframe-container">
    <iframe :src="url" title="camera" frameborder="0"></iframe>
  </div>
</template>

<script lang="ts" setup>
import { IP } from '@/constants'

const url = "http://" + IP + ":1234/?action=stream"

</script>

<style scoped>
.iframe-container {
  margin: auto;
  width: 640px;
  height: 480px;
  border: 1px solid #ccc;
  overflow: hidden;
}

iframe {
  width: 100%;
  height: 100%;
  border: none;
  /* Remove default border */
}
</style>
