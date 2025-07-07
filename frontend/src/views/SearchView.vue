<script setup>
import { defineProps, onMounted, ref, computed } from 'vue';
import { useRoute } from 'vue-router';

import TVPosterCard from '@/components/TVPosterCard.vue';
import MoviePosterCard from '@/components/MoviePosterCard.vue';
const route = useRoute()
const query = computed(() => route.params.query)
const searchResults = ref([])

onMounted(() => {
    fetch('api/search/' + query.value)
        .then(response => response.json())
        .then(data => {
            searchResults.value = data;
        })
}) 
</script>
<template>
    <div class="row">
        <div class="col-md-2" v-for="item in searchResults.results" :key="item.id">
            <TVPosterCard v-if="item.media_type=='tv'" :item="item"/>
            <MoviePosterCard v-if="item.media_type=='movie'" :item="item"/>
        </div>
    </div>
</template>