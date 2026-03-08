<script setup>
import { ref, onMounted } from 'vue'
import { io } from 'socket.io-client'
import { useSetupStore } from './stores/setup'

const message = ref('')
const socketMessage = ref('')
const store = useSetupStore()

onMounted(async () => {
  // Fetch from FastAPI
  try {
    const apiURL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
    const res = await fetch(`${apiURL}/`)
    const data = await res.json()
    message.value = data.message
  } catch (error) {
    message.value = 'Failed to fetch from backend :('
  }

  // Socket.IO Connection
  const apiURL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
  const socket = io(apiURL)
  
  socket.on('connect', () => {
    console.log('Connected to socket', socket.id)
    socket.emit('message', 'Hello from Vue Client!')
  })
  
  socket.on('response', (data) => {
    socketMessage.value = data.data
  })
})
</script>

<template>
  <div class="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center space-y-8 p-4">
    <div class="text-center space-y-4">
      <h1 class="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-500 pb-2">
        Vue + Vite + Tailwind
      </h1>
      <h2 class="text-3xl text-gray-300 font-semibold">
        FastAPI + Socket.IO + MongoDB
      </h2>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl mt-12">
      <!-- API Card -->
      <div class="p-6 bg-gray-800 rounded-2xl shadow-xl border border-gray-700 hover:border-emerald-500/50 transition duration-300">
        <h3 class="text-xl text-emerald-400 font-bold mb-3 flex items-center">
          <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          API Response:
        </h3>
        <p class="text-gray-200 text-lg">{{ message || 'Loading...' }}</p>
      </div>

      <!-- Socket.IO Card -->
      <div class="p-6 bg-gray-800 rounded-2xl shadow-xl border border-gray-700 hover:border-cyan-500/50 transition duration-300">
        <h3 class="text-xl text-cyan-400 font-bold mb-3 flex items-center">
          <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
          Socket.IO:
        </h3>
        <p class="text-gray-200 text-lg">{{ socketMessage || 'Waiting for message...' }}</p>
      </div>

      <!-- Pinia Store Card -->
      <div class="p-6 bg-gray-800 rounded-2xl shadow-xl border border-gray-700 hover:border-fuchsia-500/50 transition duration-300">
        <h3 class="text-xl text-fuchsia-400 font-bold mb-3 flex items-center">
          <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path></svg>
          Pinia Store:
        </h3>
        <p class="text-gray-200 text-lg mb-4">Click Count: <span class="font-bold text-white">{{ store.count }}</span></p>
        <button 
          @click="store.increment" 
          class="w-full px-4 py-2 bg-fuchsia-600 hover:bg-fuchsia-500 text-white font-bold rounded-lg transition duration-200 transform hover:scale-105 active:scale-95 shadow-lg shadow-fuchsia-500/30"
        >
          Increment
        </button>
      </div>
    </div>
  </div>
</template>
