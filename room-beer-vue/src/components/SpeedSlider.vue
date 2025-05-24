<template>
    <div class="container">
        <input type="range" v-model="sliderValue" min="0.0" max="1.0" step="0.1" />
        <p>{{ sliderValue }}</p>
    </div>
</template>
<script setup>
import { commandstore } from '@/stores/commandstore';
import { ref } from 'vue';

const cmdStore = commandstore();

var sliderValue = ref(sliderValue)

cmdStore.setSpeed(sliderValue)

</script>
<style scoped>
.container {
    position: fixed;
    right: 5%;
    bottom: 30%;
}
</style>