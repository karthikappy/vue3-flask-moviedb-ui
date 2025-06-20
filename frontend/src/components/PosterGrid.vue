<script setup>
const props = defineProps(["type", "target", "title"])
import { onMounted } from 'vue';
import { ref } from 'vue'
import TVPosterCard from './TVPosterCard.vue';
import MoviePosterCard from './MoviePosterCard.vue';

const apiData = ref({})

onMounted(() => {
    fetch('api/' + props.target)
        .then(response => response.json())
        .then(data => {
            apiData.value = data;
        })
}) 
</script>
<template>
    <div class="card" v-if="apiData">
        <div class="card-body">
            <h5 class="card-title">{{ title }}</h5>
            <v-row>
                <v-carousel hide-delimiters>
                    <v-carousel-item 
                        v-for="item in apiData.results" :key="item.id"
                        :src="'http://image.tmdb.org/t/p/w1280' + item.backdrop_path"
                        cover
                    >
                        <v-card style="position: absolute;bottom:0px;left:0px;width:100%;background-color:rgba(0, 0, 0, 0.5);">
                            <v-card-title><h3>{{ item.title || item.name }}</h3></v-card-title>
                            <v-card-text><p>{{ item.overview }}</p></v-card-text>
                        </v-card>
                        <div class="text-center">
                            
                            
                        </div>
                    </v-carousel-item>
                </v-carousel>
            </v-row>
            <div class="row">
                <div class="col-md-2" v-for="item in apiData.results" :key="item.id">
                    <TVPosterCard v-if="type=='tv'" :item="item"/>
                    <MoviePosterCard v-if="type=='movie'" :item="item"/>
                </div>
            </div>
        </div>
    </div>
</template>