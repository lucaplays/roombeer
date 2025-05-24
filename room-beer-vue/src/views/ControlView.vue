<template>
  <videoFrame />
  <div class="radial-buttons">
    <button id="topBtn" @mousedown="(evt)=> handleInput(evt, Direction.FORWARD)" @mouseup="(evt)=> handleInput(evt, Direction.FORWARD)" class="button top">
      {{ "^" }}
    </button>
    <button id="leftBtn" @mousedown="(evt)=> handleInput(evt, Direction.LEFT)" @mouseup="(evt)=> handleInput(evt, Direction.LEFT)" class="button left">
      {{ "<" }}
    </button>
    <button id="downBtn" @mousedown="(evt)=> handleInput(evt, Direction.BACK)" @mouseup="(evt)=> handleInput(evt, Direction.BACK)" class="button bottom">
      {{ "v" }}
    </button>
    <button id="rightBtn" @mousedown="(evt)=> handleInput(evt, Direction.RIGHT)" @mouseup="(evt)=> handleInput(evt, Direction.RIGHT)" class="button right">
      {{ ">" }}
    </button>
  </div>
</template>

<script lang="ts" setup>
import videoFrame from "@/components/IFrame.vue";
import { Direction } from "@/constants";
import { commandstore } from '@/stores/commandstore';
import { onMounted, onUnmounted } from 'vue';

const cmdStore = commandstore();

function handleInput(event: KeyboardEvent | MouseEvent, direction: Direction = Direction.NONE) {

  if(event instanceof KeyboardEvent) {
    switch(event.key) {
      case 'w':
        direction = Direction.FORWARD;
        break;
      case 'd':
        direction = Direction.RIGHT;
        break;
      case 's':
        direction = Direction.BACK;
        break;
      case 'a':
        direction = Direction.LEFT;
        break;
  }
}

  console.log(direction);

  if (direction === Direction.NONE){
    return
  }
  
  const isDown = event.type.includes('down');

  cmdStore.move(direction, isDown);
}

onMounted(() => {
  window.addEventListener('keydown', handleInput);
  window.addEventListener('keyup', handleInput);
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleInput);
  window.removeEventListener('keyup', handleInput);
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
