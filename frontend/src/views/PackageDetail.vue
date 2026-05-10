<template>
  <div>
    <h1>Package Detail</h1>
    <p>Title: {{ pkg.title }}</p>
    <p>Description: {{ pkg.description }}</p>
    <p>Price: {{ pkg.price }}</p>
    <p>Region: {{ pkg.region }}</p>
    <p>Duration: {{ pkg.duration_days }} days</p>
    <p>Theme: {{ pkg.theme }}</p>
    <h3>Schedule</h3>
    <ul>
      <li v-for="s in pkg.schedule" :key="s.day">
        Day {{ s.day }}: {{ s.activities.join(', ') }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const pkg = ref({})

onMounted(async () => {
  const res = await fetch(`http://localhost:8000/packages/${route.params.id}`)
  pkg.value = await res.json()
})
</script>
