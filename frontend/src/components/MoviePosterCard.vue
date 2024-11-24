<script setup>
    const props = defineProps(["item"])
</script>
<template>
    <div class="card" style="width: 150px;">
        <img :src="'http://image.tmdb.org/t/p/w154' + item.poster_path" alt="" class="card-img top" width="92">
        <div class="card-body">
            <p class="card-text">{{ item.title }}</p>
            <a class="card-text" :href="'#/movie/' + item.id">Details</a>
        </div>
    </div>
</template>