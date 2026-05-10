<template>
  <div>
    <h1>Package List</h1>
    <ul>
      <li v-for="pkg in packages" :key="pkg.id">
        <router-link :to="`/packages/${pkg.id}`">{{ pkg.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
const packages = ref([])

onMounted(async () => {
  const res = await fetch('http://localhost:8000/packages/')
  packages.value = await res.json()
})
</script>
