import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import PosterGridView from '../views/MoviePosterGridView.vue'
const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path:'/movie/popular/:year',
      name: 'Movie Popular by year',
      props: {
        type:"movie",
        view:"popular"
      },
      component: PosterGridView
    },
    {
      path:'/tv/popular/:year',
      name: 'TV Popular by year',
      props: {
        type:"tv",
        view:"popular"
      },
      component: PosterGridView
    },
    {
      path: '/movie/:id',
      name: 'movie',
      component: MovieView
    },
    
  ]
})

export default router
