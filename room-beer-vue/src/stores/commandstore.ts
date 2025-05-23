import { defineStore } from 'pinia';
import axios from 'axios';

export const commandstore = defineStore('commandstore', {
    state: () => ({

    }),
    actions: {
        postRequest(message: string) {
            axios.post('http://127.0.0.1:8000/post/', {
                name: message
            })
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    },
});
