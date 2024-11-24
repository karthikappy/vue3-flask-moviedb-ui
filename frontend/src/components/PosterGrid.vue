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
            <div class="row">
                <div class="col-md-2" v-for="item in apiData.results" :key="item.id">
                    <TVPosterCard v-if="type=='tv'" :item="item"/>
                    <MoviePosterCard v-if="type=='movie'" :item="item"/>
                </div>
            </div>
        </div>
    </div>
</template>