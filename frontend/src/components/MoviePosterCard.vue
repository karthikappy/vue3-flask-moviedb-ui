<script setup>
defineProps(['item'])
</script>

<template>
  <v-card :to="'/movie/' + item.id" width="150">
    <v-img :alt="item.title" :src="'http://image.tmdb.org/t/p/w154' + item.poster_path" cover />
    <v-card-title class="text-body-2 text-wrap">{{ item.title }}</v-card-title>
    <v-card-actions>
      <v-btn color="primary" size="small" variant="text">Details</v-btn>
    </v-card-actions>
  </v-card>
</template>
