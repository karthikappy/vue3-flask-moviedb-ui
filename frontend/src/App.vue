<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
//import HelloWorld from './components/HelloWorld.vue'

import { useRoute } from 'vue-router'

const searchQuery = ref('')
const route = useRoute()

const doSearch = (event) => {
  if (searchQuery.value.trim()) {
    // Redirect to the search results page
    window.location.href = `#/search/${encodeURIComponent(searchQuery.value)}`
  }
}
</script>

<template>
  <v-app>
      <header>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    TV
                  </a>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#/tv/popular/2024">2024 Releases</a></li>
                    <li><a class="dropdown-item" href="#/tv/popular/2023">2023 Releases</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Now Playing</a></li>
                    <li><a class="dropdown-item" href="#">Popular</a></li>
                    <li><a class="dropdown-item" href="#">Top Rated</a></li>
                    <li><a class="dropdown-item" href="#">Upcoming</a></li>
                  </ul>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Movies
                  </a>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#/movie/popular/2024">2024 Releases</a></li>
                    <li><a class="dropdown-item" href="#/movie/popular/2023">2023 Releases</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Now Playing</a></li>
                    <li><a class="dropdown-item" href="#">Popular</a></li>
                    <li><a class="dropdown-item" href="#">Top Rated</a></li>
                    <li><a class="dropdown-item" href="#">Upcoming</a></li>
                  </ul>
                </li>
              </ul>
              
                <input class="form-control me-2" v-model="searchQuery" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit" v-on:click="doSearch">Search</button>
              
            </div>
          </div>
        </nav>
      </header>
    <v-main>
      <RouterView :key="route.fullPath" />
    </v-main>
  </v-app>
</template>

<style scoped>

</style>
