<script setup>
defineProps(['item'])
</script>

<template>
  <v-card width="150">
    <v-img :alt="item.name" :src="'http://image.tmdb.org/t/p/w154' + item.poster_path" cover />
    <v-card-title class="text-body-2 text-wrap">{{ item.name }}</v-card-title>
  </v-card>
</template>
