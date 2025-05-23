<template>

  <div class="radial-buttons">
    <button id="topBtn" :class="{ active: inputPressed[0] }" @mousedown="(evt) => handleInput(evt, Direction.FORWARD)"
      @mouseup="(evt) => handleInput(evt, Direction.FORWARD)" class="button top">
      {{ "^" }}
    </button>
    <button id="rightBtn" :class="{ active: inputPressed[1] }" @mousedown="(evt) => handleInput(evt, Direction.RIGHT)"
      @mouseup="(evt) => handleInput(evt, Direction.RIGHT)" class="button right">
      {{ ">" }}
    </button>
    <button id="downBtn" :class="{ active: inputPressed[2] }" @mousedown="(evt) => handleInput(evt, Direction.BACK)"
      @mouseup="(evt) => handleInput(evt, Direction.BACK)" class="button bottom">
      {{ "v" }}
    </button>
    <button id="leftBtn" :class="{ active: inputPressed[3] }" @mousedown="(evt) => handleInput(evt, Direction.LEFT)"
      @mouseup="(evt) => handleInput(evt, Direction.LEFT)" class="button left">
      {{ "<" }} </button>
  </div>

  <videoFrame />
</template>

<script lang="ts" setup>
import videoFrame from "@/components/IFrame.vue";
import { Direction } from "@/constants";
import { commandstore } from '@/stores/commandstore';
import { ref, onMounted, onUnmounted } from 'vue';

const inputPressed = ref<boolean[]>([false, false, false, false])
const cmdStore = commandstore();

function handleInput(event: KeyboardEvent | MouseEvent, direction: Direction = Direction.NONE) {
  const isDown = event.type.includes('down');

  if (event instanceof KeyboardEvent) {
    switch (event.key) {
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


  if (direction === Direction.NONE) {
    return
  }

  if (isDown && inputPressed.value[direction - 1]) {
    return;
  }

  console.log(direction, isDown);

  inputPressed.value[direction - 1] = isDown;

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
  z-index: 2;
  position: fixed;
  width: 150px;
  height: 150px;
  bottom: 5%;
  right: 5%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button {
  position: absolute;
  width: 50px;
  height: 50px;
  border: none;
  border-radius: 50%;
  background-color: #007bff87;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

.button:hover {
  background-color: #2d91fc87;
}

.button:active {
  background-color: #09325e87;
}

.button:not(:active) {
  background-color: #007bff87;
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
