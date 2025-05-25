<template>
    <div class="sensor-container">
        <div class="inner-container">
            <div class="center">
                <div v-if="loaded">
                    <img class="img" src="../assets/leberkas.png" alt="">
                </div>
            </div>
            <div :style="{top: getPosition(sensorData[4]) +'%',
             left: getDistanceToEdge(sensorData[4])  + '%'}" 
             class="sensor h front-left"></div>
            <div :style="{top: getPosition(sensorData[0]) +'%'}"
              class="sensor h front-middle"></div>
            <div :style="{top: getPosition(sensorData[5]) +'%',
             right: getDistanceToEdge(sensorData[5]) + '%'}" 
              class="sensor h front-right"></div>
            <div :style="{right: getPosition(sensorData[3]) +'%',
             top: getDistanceToEdge(sensorData[3]) + '%',
             bottom: getDistanceToEdge(sensorData[3]) + '%'}" 
              class="sensor v right"></div>
            <div :style="{bottom: getPosition(sensorData[2]) +'%',
             left: getDistanceToEdge(sensorData[3]) + '%',
             right: getDistanceToEdge(sensorData[3]) + '%'}" 
              class="sensor h back"></div>
            <div :style="{left: getPosition(sensorData[1]) +'%',
             top: getDistanceToEdge(sensorData[3]) + '%',
             bottom: getDistanceToEdge(sensorData[3]) + '%'}" 
              class="sensor v left"></div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue';
import { commandstore } from '@/stores/commandstore';

const cmdStore = commandstore();

const loaded = ref(false);
const sensorData = ref<number[]>([ 0, 0, 0, 0, 0, 0 ]);

let sensorInterval:number;

function getPosition(value: number){
    return (1 - (value / 3200)) * 30;
}

function getDistanceToEdge(value:number){
    return (1 - value / 3200) * 30
}

onMounted(() => {
    sensorInterval = setInterval(updateSensorValues, 100);
})

onUnmounted(() => {
    clearInterval(sensorInterval);
})

async function updateSensorValues() {
    await cmdStore.getSensors().then((sData:Array<number> = []) => {
        const isLoaded = sData.pop()
        loaded.value = isLoaded == undefined ? false : isLoaded < 100;
        sensorData.value = sData;
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
    display: flex;
    justify-items: center;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background-color: lightslategray;
    border-radius: 7px;
    width: 40%;
    height: 40%;
}

.img {
    display: block;
    width: 100%;
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
    right: 70%;
    top: 0;
}

.front-middle {
    position: absolute;
    left: 30%;
    right: 30%;
    top: 0;
}

.front-right {
    position: absolute;
    left: 70%;
    right: 0;
    top: 0;
}

.back {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
}

.left {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
}

.right {
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
}
</style>
