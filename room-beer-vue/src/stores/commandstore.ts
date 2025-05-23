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
                    // Handle success
                } else {
                    console.log(result.status + " " + result.statusText)
                }
            } catch (error) {
                console.log("Failed: " + error)
            }
        },
        async driveForwards() {
            await this.postRequest('post/drive/forwards') // Only the path
        },
        async driveBackwards() {
            await this.postRequest('post/drive/backwards') // Only the path
        },
        async driveTurnLeft() {
            await this.postRequest('post/drive/turnleft') // Only the path
        },
        async driveTurnRight() {
            await this.postRequest('post/drive/turnright') // Only the path
        },
    },
});
