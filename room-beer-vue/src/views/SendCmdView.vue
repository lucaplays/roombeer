<template>
  <div>
    <button @click="cmdStore.postRequest('tmp')">Send Command</button>
  </div>
</template>

<script lang="ts" setup>
import { commandstore } from '@/stores/commandstore';

var cmdStore = commandstore()

</script>
