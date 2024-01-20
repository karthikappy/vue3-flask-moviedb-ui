<script setup>
const props = defineProps(["type", "target", "title"])
import { onMounted } from 'vue';
import { reactive } from 'vue'
import TVPosterCard from './TVPosterCard.vue';
import MoviePosterCard from './MoviePosterCard.vue';

const apiData = reactive({})

onMounted(() => {
    fetch('api/' + props.target)
        .then(response => response.json())
        .then(data => {
            apiData.data = data;
        })
}) 
</script>
<template>
    <div class="card" v-if="apiData.data">
        <div class="card-body">
            <h5 class="card-title">{{ title }}</h5>
            <div class="row">
                <div class="col-md-2" v-for="item in apiData.data.results" :key="item.id">
                    <TVPosterCard v-if="type=='tv'" :item="item"/>
                    <MoviePosterCard v-if="type=='movie'" :item="item"/>
                </div>
            </div>
        </div>
    </div>
</template>