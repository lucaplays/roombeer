<template>
    <div class="container">
        <div class="column" v-for="(label, index) in labels" :key="index">
            <div class="circle" :style="circleStyle(distances[index])"></div>
            <h3>{{ label }}</h3>
            <p>{{ distances[index].toFixed(1) }}</p>
        </div>
        <button @click="updateDistanceValues">update</button>
    </div>
</template>

<script setup>
import { commandstore } from '@/stores/commandstore';

var cmdStore = commandstore();
// Labels for the columns
const labels = ['Front', 'Back', 'Left', 'Right'];
// Distances for each column (0 to 1)
var distances = [1.0, 0.0, 0.0, 0.0]; // Example distances

async function updateDistanceValues() {
    await cmdStore.getDistances().then((data) => {
        distances.value = data;
    });
}

// Function to calculate the circle style based on distance
const circleStyle = (distance) => {
    return {
        width: '10px',
        height: '10px',
        borderRadius: '50%',
        backgroundColor: 'red',
        position: 'absolute',
        bottom: `${distance * 100}%`, // Position based on distance
        left: '50%',
        transform: 'translateX(-50%)', // Center the circle horizontally
    };
};
</script>

<style scoped>
.container {
    position: fixed;
    bottom: 0;
    display: flex;
    justify-content: space-around;
    align-items: flex-end;
    height: 200px;
    border-left: 1px solid #ffffff;
    border-right: 1px solid #ffffff;
    border-bottom: 1px solid #ffffff;
    background-color: rgba(0, 0, 0, 0.822);
}

.column {

    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    text-align: center;
    height: 90%;
    width: 100px;
    border-left: 1px solid #ffffff;
    border-right: 1px solid #ffffff;
}

.column:not(:last-child)::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 1px;
    height: 100%;
}

h3 {
    margin: 0;
    border-top: 1px solid #ffffff;
    border-bottom: 1px solid #ccc;
}

p {
    margin: 0;
}

.circle {
    transition: bottom 0.3s;
}
</style>
