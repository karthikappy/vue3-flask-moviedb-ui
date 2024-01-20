<script setup>
import PosterGrid from '../components/PosterGrid.vue'
</script>

<template>
  <main>
    <PosterGrid target="toprated-tv" title="Top Rated TV"/>
    <PosterGrid target="popular-tv" title="Popular TV"/>
    <PosterGrid target="toprated-movies" title="Top Rated Movies"/>
    <PosterGrid target="popular-movies" title="Popular Movies"/>
    
  </main>
</template>
