<template>
    <div class="sensor-container">
        <div class="inner-container">
            <div class="center">
                <div v-if="loaded">
                    <img src="../assets/leberkas.png" alt="">
                </div>
            </div>
            <div class="sensor h front-left"></div>
            <div class="sensor h front-middle"></div>
            <div class="sensor h front-right"></div>
            <div class="sensor v right"></div>
            <div class="sensor h back"></div>
            <div class="sensor v left"></div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue';
import { commandstore } from '@/stores/commandstore';

const cmdStore = commandstore();

const loaded = ref(true);
const sensorData = ref([ 0, 0, 0, 0, 0, 0 ]);

let sensorInterval;

onMounted(() => {
    sensorInterval = setInterval(updateSensorValues, 500);
})

onUnmounted(() => {
    clearInterval(sensorInterval);
})

async function updateSensorValues() {
    await cmdStore.getSensors().then(({sensorData, isLoaded }) => {
        sensorData.value = sensorData;
        loaded.value = isLoaded
    });
}

</script>

<style scoped>
.sensor-container {
    position: absolute;
    left: 0;
    bottom: 0;
    height: 300px;
    width: 400px;
    background-color: rgba(50, 50, 50, 0.5);
    padding: 10px 15px;
}

.inner-container {
    position: relative;
    width: 100%;
    height: 100%;
}

.center {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background-color: lightslategray;
    border-radius: 7px;
    width: 40%;
    height: 40%;
}

.sensor {
    position: absolute;
    background-color: yellow;
}

.sensor.v {
    width: 2px;
}

.sensor.h {
    height: 2px;
}

.front-left {
    position: absolute;
    left: 0;
    top: 0;
    width: calc(100% / 3);
}

.front-middle {
    position: absolute;
    left: calc(100% / 3);
    top: 0;
    width: calc(100% / 3);
}

.front-right {
    position: absolute;
    left: calc(100% / 3 * 2);
    top: 0;
    width: calc(100% / 3);
}

.back {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
}

.left {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
}

.right {
    position: absolute;
    right: 0;
    top: 0;
    height: 100%;
}
</style>
