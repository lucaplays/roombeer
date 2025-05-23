<template>
  <div>
    <button @click="sendCommand">Send Command</button>
  </div>
</template>

<script lang="ts" setup>
import axios from 'axios';

const sendCommand = async () => {
  const command = {
    action: 'some_action',
    data: {
      key: 'value'
    }
  };

  try {
    const response = await axios.post('http://localhost:8000/execute-command/', command);
    console.log(response.data);
  } catch (error) {
    console.error('Error sending command:', error);
  }
};
</script>
