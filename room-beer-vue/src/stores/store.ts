import { defineStore } from 'pinia';

export const store = defineStore('store', {
    state: () => ({
        count: 0,
    }),
    actions: {
        increment() {
            this.count++;
        },
    },
});
