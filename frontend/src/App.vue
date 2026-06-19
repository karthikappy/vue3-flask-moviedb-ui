<script setup>
import { useRoute } from 'vue-router'
import NavBar from './components/NavBar.vue'

const route = useRoute()
</script>

<template>
  <v-app>

  <header>
    <NavBar />
  </header>

    <v-main>
      <RouterView :key="route.fullPath" />
    </v-main>
  </v-app>
</template>

<style scoped>

</style>
