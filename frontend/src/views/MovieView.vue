<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const movieInfo = ref({})
const route = useRoute()
const id = route.params.id

onMounted(() => {
  fetch('api/movie/details/' + id)
    .then((response) => response.json())
    .then((data) => {
      movieInfo.value = data
    })
})
</script>

<template>
  <v-container fluid>
    <v-card v-if="movieInfo">
      <v-img
        class="movie-backdrop"
        :src="'http://image.tmdb.org/t/p/w1280' + movieInfo.backdrop_path"
        cover
      >
        <v-container class="fill-height movie-overlay" fluid>
          <v-row align="center">
            <v-col cols="12" md="4">
              <v-img
                :alt="movieInfo.title"
                :src="'http://image.tmdb.org/t/p/w342' + movieInfo.poster_path"
                class="mx-auto"
                max-width="342"
              />
            </v-col>
            <v-col cols="12" md="8">
              <v-card color="rgba(0, 0, 0, 0.65)">
                <v-card-text>
                  <h1>
                    {{ movieInfo.title }}
                    <span v-if="movieInfo.title !== movieInfo.original_title">
                      ({{ movieInfo.original_title }})
                    </span>
                  </h1>
                  <p class="movie-subtitle">{{ movieInfo.tagline }}</p>
                  <p v-if="movieInfo.genres">
                    {{ movieInfo.genres.map((genre) => genre.name).join(', ') }}
                  </p>
                  <p>Runtime: {{ movieInfo.runtime }} minutes</p>
                  <p>Release Date: {{ movieInfo.release_date }}</p>
                  <p>{{ movieInfo.overview }}</p>
                  <v-row class="mt-2">
                    <v-col cols="12" sm="6" md="4">
                      <v-card>
                        <v-card-title>Budget</v-card-title>
                        <v-card-text>{{ movieInfo.budget }}</v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                  <v-card v-if="movieInfo.belongs_to_collection" class="mt-4">
                    <v-card-title>{{ movieInfo.belongs_to_collection.name }}</v-card-title>
                  </v-card>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-img>
    </v-card>
  </v-container>
</template>

<style scoped>
.movie-backdrop {
  min-height: calc(100vh - 64px);
}

.movie-overlay {
  background: rgba(0, 0, 0, 0.45);
}

.movie-subtitle {
  font-style: italic;
}
</style>
