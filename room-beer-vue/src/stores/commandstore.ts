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
        },
        driveForwards() {
            axios.post('http://127.0.0.1:8000/post/drive/forwards/')
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        driveBackwards() {
            axios.post('http://127.0.0.1:8000/post/drive/backwards/')
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        driveTurnLeft() {
            axios.post('http://127.0.0.1:8000/post/drive/turnleft/')
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        driveTurnRight() {
            axios.post('http://127.0.0.1:8000/post/drive/turnright/')
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
    },
});
