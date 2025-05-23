import { defineStore } from 'pinia';

const BASE_URL = "http://127.0.0.1:8000/"

export const commandstore = defineStore('commandstore', {
    state: () => ({

    }),
    actions: {
        async postRequest(path: string) {
            try {
                let result = await fetch(BASE_URL + path, {
                    method: "POST"
                })
                if (result.ok) {
                    //ok
                } else {
                    console.log(result.status + " " + result.statusText)
                }
            } catch (error) {
                console.log("Failed: " + error)
            }
        },
        async driveForwards() {
            await this.postRequest('http://127.0.0.1:8000/post/drive/forwards/')
        },
        async driveBackwards() {
            await this.postRequest('http://127.0.0.1:8000/post/drive/backwards/')
        },
        async driveTurnLeft() {
            await this.postRequest('http://127.0.0.1:8000/post/drive/turnleft/')
        },
        async driveTurnRight() {
            await this.postRequest('http://127.0.0.1:8000/post/drive/turnright/')
        },
    },
});
