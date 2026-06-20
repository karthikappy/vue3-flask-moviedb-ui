<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import MoviePosterCard from '@/components/MoviePosterCard.vue'
import TVPosterCard from '@/components/TVPosterCard.vue'

const route = useRoute()
const query = computed(() => route.params.query)
const searchResults = ref([])

onMounted(() => {
  fetch('api/search/' + query.value)
    .then((response) => response.json())
    .then((data) => {
      searchResults.value = data
    })
})
</script>

<template>
  <v-container fluid>
    <v-row>
      <v-col v-for="item in searchResults.results" :key="item.id" cols="6" sm="4" md="2">
        <TVPosterCard v-if="item.media_type === 'tv'" :item="item" />
        <MoviePosterCard v-if="item.media_type === 'movie'" :item="item" />
      </v-col>
    </v-row>
  </v-container>
</template>
