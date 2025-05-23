<template>
  <div>
    <button @click="cmdStore.driveForwards">Send Command</button>
  </div>
</template>

<script lang="ts" setup>
import { commandstore } from '@/stores/commandstore';

var cmdStore = commandstore()

</script>
