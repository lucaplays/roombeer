<template>
  <videoFrame />
  <div class="radial-buttons">
    <button @click="cmdStore.driveForwards" class="button top">{{ "^" }}</button>
    <button @click="cmdStore.driveTurnLeft" class="button left">{{ "<" }}</button>
        <button @click="cmdStore.driveBackwards" class="button bottom">{{ "v" }}</button>
        <button @click="cmdStore.driveTurnRight" class="button right">{{ ">" }}</button>
  </div>
</template>

<script lang="ts" setup>
import videoFrame from "@/components/IFrame.vue";
import { commandstore } from '@/stores/commandstore';

var cmdStore = commandstore();

</script>

<style scoped>
.radial-buttons {
  position: relative;
  width: 200px;
  /* Adjust size as needed */
  height: 200px;
  /* Adjust size as needed */
  margin: auto;
}

.button {
  position: absolute;
  width: 50px;
  /* Adjust button size as needed */
  height: 50px;
  /* Adjust button size as needed */
  border: none;
  border-radius: 50%;
  background-color: #007bff;
  /* Button color */
  color: white;
  font-size: 20px;
  cursor: pointer;
}

.top {
  top: 0;
  left: 50%;
  transform: translate(-50%, -50%);
}

.left {
  top: 50%;
  left: 0;
  transform: translate(-50%, -50%);
}

.bottom {
  bottom: 0;
  left: 50%;
  transform: translate(-50%, 50%);
}

.right {
  top: 50%;
  right: 0;
  transform: translate(50%, -50%);
}
</style>
