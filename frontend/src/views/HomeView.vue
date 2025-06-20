<script setup>
import PosterGrid from '../components/PosterGrid.vue'
</script>

<template>
  <v-container fluid>

    <PosterGrid type="movie" target="movie/released_last_14days" title="Popular Hollywood movies in the last 2 weeks"/>
  </v-container>
</template>
