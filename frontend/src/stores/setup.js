import { defineStore } from 'pinia'

export const useSetupStore = defineStore('setup', {
    state: () => ({
        count: 0
    }),
    actions: {
        increment() {
            this.count++
        }
    }
})
