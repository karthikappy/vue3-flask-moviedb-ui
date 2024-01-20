<script setup>
import PosterGrid from '../components/PosterGrid.vue'
</script>

<template>
  <main>
    <PosterGrid type="tv" target="toprated-tv" title="Top Rated TV"/>
    <PosterGrid type="tv" target="popular-tv" title="Popular TV"/>
    <PosterGrid type="movie" target="toprated-movies" title="Top Rated Movies"/>
    <PosterGrid type="movie" target="popular-movies" title="Popular Movies"/>
    
  </main>
</template>
