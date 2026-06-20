<script setup>
import { onMounted, ref } from 'vue'

import MoviePosterCard from './MoviePosterCard.vue'
import TVPosterCard from './TVPosterCard.vue'

const props = defineProps(['type', 'target', 'title'])
const apiData = ref({})

onMounted(() => {
  fetch('api/' + props.target)
    .then((response) => response.json())
    .then((data) => {
      apiData.value = data
    })
})
</script>

<template>
  <v-card v-if="apiData">
    <v-card-title>{{ title }}</v-card-title>
    <v-card-text>
      <v-carousel hide-delimiters>
        <v-carousel-item
          v-for="item in apiData.results"
          :key="item.id"
          :src="'http://image.tmdb.org/t/p/w1280' + item.backdrop_path"
          cover
        >
          <v-card
            style="position: absolute; bottom: 0; left: 0; width: 100%; background-color: rgba(0, 0, 0, 0.5)"
          >
            <v-card-title><h3>{{ item.title || item.name }}</h3></v-card-title>
            <v-card-text><p>{{ item.overview }}</p></v-card-text>
          </v-card>
        </v-carousel-item>
      </v-carousel>
      <v-row class="mt-2">
        <v-col v-for="item in apiData.results" :key="item.id" cols="6" sm="4" md="2">
          <TVPosterCard v-if="type === 'tv'" :item="item" />
          <MoviePosterCard v-if="type === 'movie'" :item="item" />
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
