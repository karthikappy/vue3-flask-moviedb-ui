<script setup>
import PosterGrid from '../components/PosterGrid.vue'
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const props = defineProps(["type", "view"])

const route = useRoute()
const type = props.type
const view = props.view
const year = route.params.year
</script>

<template>
  <main>
    <PosterGrid :type="type" :target="type + '/'+view+'/' + year" :title="'Popular Hollywood movies in ' +  year"/>
  </main>
</template>
