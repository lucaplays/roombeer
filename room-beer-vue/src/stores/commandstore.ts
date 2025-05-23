import { defineStore } from 'pinia';

const ip = process.env.VUE_APP_IP || '127.0.0.1';
const BASE_URL = "http://" + ip + ":8000/"

console.log("Hallo" + ip)

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
        // DRIVE
        async driveForwards() {
            await this.postRequest('post/drive/forwards')
        },
        async driveBackwards() {
            await this.postRequest('post/drive/backwards')
        },
        async driveTurnLeft() {
            await this.postRequest('post/drive/turnleft')
        },
        async driveTurnRight() {
            await this.postRequest('post/drive/turnright')
        },
        // STOP
        async stopForwards() {
            await this.postRequest('post/stop/forwards')
        },
        async stopBackwards() {
            await this.postRequest('post/stop/backwards')
        },
        async stopTurnLeft() {
            await this.postRequest('post/stop/turnleft')
        },
        async stopTurnRight() {
            await this.postRequest('post/stop/turnright')
        },
    },
});
