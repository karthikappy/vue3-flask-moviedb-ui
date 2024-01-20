<script setup>
import { reactive } from 'vue';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router'

const movieInfo = reactive({})
const route = useRoute()
const id = route.params.id
onMounted(() => {
    fetch('api/movie/details/' + id)
        .then(response => response.json())
        .then(data => {
            movieInfo.data = data;
        })
}) 
</script>
<template>
    <main>
        <div class="card" v-if="movieInfo.data">
            <img :src="'http://image.tmdb.org/t/p/w780' + movieInfo.data.backdrop_path" class="card-img backdrop-img" alt="...">
            <div class="card-img-overlay">
                <div class="row">
                    <div class="col-md-4"><img :src="'http://image.tmdb.org/t/p/w342' + movieInfo.data.poster_path" alt="" width="342"><img src="" alt="">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h1 class="card-title">
                                {{ movieInfo.data.title }}
                                <span v-if="movieInfo.data.title != movieInfo.data.original_title">({{ movieInfo.data.original_title }})</span>
                            </h1>
                            <p class="card-text">{{ movieInfo.data.tagline }}</p>
                            <p class="card-text">{{ movieInfo.data.overview }}</p>
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
</style>