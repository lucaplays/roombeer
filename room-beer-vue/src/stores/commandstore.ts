import { Direction, IP } from '@/constants';
import { defineStore } from 'pinia';

const BASE_URL = "http://" + IP + ":8000/"

interface Distance {
    distFront: number;
    distBack: number;
    distLeft: number;
    distRight: number;
}

export const commandstore = defineStore('commandstore', {
    state: () => ({}),
    actions: {
        async postRequest(path: string, body: object) {
            console.log(body)
            try {
                const result = await fetch(BASE_URL + path, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
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
        async getSensors(): Promise<Array<number>> {
            try {
                const result = await fetch(BASE_URL + "sonicsensors", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json"
                    },
                });

                if (result.ok) {
                    const data = await result.json();
                    return data.res.map((s:any) => s.distance);
                } else {
                    console.log(result.status + " " + result.statusText);
                }
            } catch (error) {
                console.log("Failed: " + error);
            }

            return [];
        },
        async setSpeed(speed: number) {
            await this.postRequest('speed', {
                speed
            })
        },
        async move(direction: Direction, isDown: boolean) {
            await this.postRequest('move', {
                direction,
                isDown
            })
        },
    },
});