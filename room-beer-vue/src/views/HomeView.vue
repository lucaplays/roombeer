<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
    <p>Count: {{ myStore.count }}</p>
    <button @click="myStore.increment">Increment</button>
  </div>
</template>

<script lang="ts" setup>
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import { store } from '@/stores/store';

const myStore = store()
</script>
