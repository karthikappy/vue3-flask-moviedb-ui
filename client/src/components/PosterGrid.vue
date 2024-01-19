<script setup>
const props = defineProps(["target", "title"])
import { onMounted } from 'vue';
import { reactive } from 'vue'

const apiData = reactive({})

onMounted(() => {
    fetch('http://127.0.0.1:5000/api/' + props.target)
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
                <div class="col-md-2" v-for="item in apiData.data.results">
                    <div class="card" style="width: 150px;">
                        <img :src="'http://image.tmdb.org/t/p/w154' + item.poster_path" alt="" class="card-img top" width="92">
                        <div class="card-body">
                            <p class="card-text">{{ item.name }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>