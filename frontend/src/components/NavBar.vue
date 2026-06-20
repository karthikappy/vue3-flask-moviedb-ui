<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const drawerOpen = ref(false)
const searchQuery = ref('')
const router = useRouter()

const menuItems = [
  {
    title: 'TV',
    items: [
      { title: '2025 Releases', to: '/tv/popular/2025' },
      { title: '2024 Releases', to: '/tv/popular/2024' },
      { title: 'Now Playing' },
      { title: 'Popular' },
      { title: 'Top Rated' },
      { title: 'Upcoming' },
    ],
  },
  {
    title: 'Movies',
    items: [
      { title: '2025 Releases', to: '/movie/popular/2025' },
      { title: '2024 Releases', to: '/movie/popular/2024' },
      { title: 'Now Playing' },
      { title: 'Popular' },
      { title: 'Top Rated' },
      { title: 'Upcoming' },
    ],
  },
]

const doSearch = () => {
  if (searchQuery.value.trim()) {
    router.push(`/search/${encodeURIComponent(searchQuery.value.trim())}`)
    drawerOpen.value = false
  }
}
</script>

<template>
  <v-app-bar color="surface">
    <v-app-bar-nav-icon
      class="d-md-none"
      aria-label="Open navigation"
      @click="drawerOpen = !drawerOpen"
    />
    <v-app-bar-title>
      <RouterLink to="/">Movie DB</RouterLink>
    </v-app-bar-title>

    <div class="d-none d-md-flex align-center ga-2">
      <v-btn to="/" variant="text">Home</v-btn>
      <v-menu v-for="menu in menuItems" :key="menu.title">
        <template #activator="{ props }">
          <v-btn v-bind="props" append-icon="mdi-menu-down" variant="text">{{ menu.title }}</v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="item in menu.items"
            :key="item.title"
            :href="item.to ? undefined : '#'"
            :to="item.to"
            :title="item.title"
          />
        </v-list>
      </v-menu>
    </div>

    <v-form class="d-none d-md-flex align-center ml-4 mr-4" @submit.prevent="doSearch">
      <v-text-field
        v-model="searchQuery"
        aria-label="Search"
        density="compact"
        hide-details
        placeholder="Search"
        prepend-inner-icon="mdi-magnify"
        width="220"
      />
      <v-btn class="ml-2" color="primary" type="submit" variant="outlined">Search</v-btn>
    </v-form>
  </v-app-bar>

  <v-navigation-drawer v-model="drawerOpen" temporary>
    <v-list nav>
      <v-list-item prepend-icon="mdi-home" title="Home" to="/" @click="drawerOpen = false" />
      <v-list-group v-for="menu in menuItems" :key="menu.title" :value="menu.title">
        <template #activator="{ props }">
          <v-list-item v-bind="props" :title="menu.title" />
        </template>
        <v-list-item
          v-for="item in menu.items"
          :key="item.title"
          :href="item.to ? undefined : '#'"
          :to="item.to"
          :title="item.title"
          @click="drawerOpen = false"
        />
      </v-list-group>
    </v-list>
    <v-form class="pa-4" @submit.prevent="doSearch">
      <v-text-field
        v-model="searchQuery"
        density="compact"
        label="Search"
        prepend-inner-icon="mdi-magnify"
      />
      <v-btn block color="primary" type="submit" variant="outlined">Search</v-btn>
    </v-form>
  </v-navigation-drawer>
</template>
