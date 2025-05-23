import { Direction, IP } from '@/constants';
import { defineStore } from 'pinia';

const BASE_URL = "http://" + IP + ":8000/"

export const commandstore = defineStore('commandstore', {
    state: () => ({

    }),
    actions: {
        async postRequest(path: string, body: object) {
            try {
                const result = await fetch(BASE_URL + path, {
                    method: "POST",
                    body: JSON.stringify(body)
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
        async move(direction: Direction, isDown: boolean) {
            await this.postRequest('move', {
                direction,
                isDown
            })
        },
    },
});
