<template>
  <div class="iframe-container">
    <iframe src="http://10.201.128.155:1234/?action=stream" title="camera" frameborder="0"></iframe>
  </div>
</template>

<script lang="ts" setup>

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
