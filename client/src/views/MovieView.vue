<script setup>
import { ref } from 'vue';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router'

const movieInfo = ref({})
const route = useRoute()
const id = route.params.id
onMounted(() => {
    fetch('api/movie/details/' + id)
        .then(response => response.json())
        .then(data => {
            movieInfo.value = data;
        })
}) 
</script>
<template>
    <main>
        <div class="card" v-if="movieInfo">
            <img :src="'http://image.tmdb.org/t/p/w780' + movieInfo.backdrop_path" class="card-img backdrop-img" alt="...">
            <div class="card-img-overlay">
                <div class="row">
                    <div class="col-md-4"><img :src="'http://image.tmdb.org/t/p/w342' + movieInfo.poster_path" alt="" width="342"><img src="" alt="">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h1 class="card-title">
                                {{ movieInfo.title }}
                                <span v-if="movieInfo.title != movieInfo.original_title">({{ movieInfo.original_title }})</span>
                            </h1>
                            <p class="card-subtitle">{{ movieInfo.tagline }}</p>
                            <p class="card-text" v-if="movieInfo.genres">{{ movieInfo.genres.map(obj => obj.name).join(', ') }}</p>
                            <p class="card-text">Runtime: {{ movieInfo.runtime }} minutes</p>
                            <p class="card-text">Release Date: {{ movieInfo.release_date }}</p>
                            <p class="card-text">{{ movieInfo.overview }}</p>
                            <div class="row">
                                <div class="col-md-3">
                                    <div class="card">
                                        <div class="card-body">
                                            <h5 class="card-title">Budget</h5>
                                            <p class="card-text">{{movieInfo.budget}}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
<style scoped>
.backdrop-img {
    opacity: 0.5;
    color: black;
    background-size: cover;
}
.card-subtitle {
    font-style: italic;
}
</style>