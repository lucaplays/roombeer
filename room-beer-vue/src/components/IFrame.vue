<template>
  <div class="iframe-container">
    <iframe src="http://127.0.0.1:8000/" title="" frameborder="0"></iframe>
  </div>
</template>

<script lang="ts" setup>

</script>

<style scoped>
.iframe-container {
  margin: auto;
  width: 50%;
  height: 500px;
  /* Adjust height as needed */
  border: 1px solid #ccc;
  /* Optional border */
  overflow: hidden;
  /* Hide overflow */
}

iframe {
  width: 100%;
  height: 100%;
  border: none;
  /* Remove default border */
}
</style>
