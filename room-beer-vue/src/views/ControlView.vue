<template>
  <videoFrame />
  <div class="radial-buttons">
    <button id="topBtn" @mousedown="cmdStore.driveForwards()" @mouseup="cmdStore.stopForwards()" class="button top">
      {{ "^" }}
    </button>
    <button id="leftBtn" @mousedown="cmdStore.driveTurnLeft()" @mouseup="cmdStore.stopTurnLeft()" class="button left">
      {{ "<" }} </button>
        <button id="downBtn" @mousedown="cmdStore.driveBackwards()" @mouseup="cmdStore.stopBackwards()"
          class="button bottom">
          {{ "v" }}
        </button>
        <button id="rightBtn" @mousedown="cmdStore.driveTurnRight()" @mouseup="cmdStore.stopTurnRight()"
          class="button right">
          {{ ">" }}
        </button>
  </div>
</template>

<script lang="ts" setup>
import videoFrame from "@/components/IFrame.vue";
import { commandstore } from '@/stores/commandstore';

var cmdStore = commandstore();
const keysPressed: { [key: string]: boolean } = {};

function handleKeyDown(key: string) {
  switch (key) {
    case "w":
      cmdStore.driveForwards()
      break
    case "s":
      cmdStore.driveBackwards()
      break
    case "a":
      cmdStore.driveTurnLeft()
      break
    case "d":
      cmdStore.driveTurnRight()
      break
  }
}

function handleKeyUp(key: string) {
  switch (key) {
    case "w":
      cmdStore.stopForwards()
      break
    case "s":
      cmdStore.stopBackwards()
      break
    case "a":
      cmdStore.stopTurnLeft()
      break
    case "d":
      cmdStore.stopTurnRight()
      break
  }
}

document.addEventListener('keydown', (event: KeyboardEvent) => {
  const key = event.key.toLowerCase();
  if (['w', 'a', 's', 'd'].includes(key) && !keysPressed[key]) {
    keysPressed[key] = true;
    handleKeyDown(key);
  }
});

document.addEventListener('keyup', (event: KeyboardEvent) => {
  const key = event.key.toLowerCase();
  if (['w', 'a', 's', 'd'].includes(key) && keysPressed[key]) {
    keysPressed[key] = false;
    handleKeyUp(key);
  }
});

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
