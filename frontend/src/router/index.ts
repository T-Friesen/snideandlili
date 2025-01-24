import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import PostDetails from '../views/PostDetails.vue'
import AdminPanel from '../views/AdminPanel.vue'
import About from '../views/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/post/:id', component: PostDetails },
  { path: '/admin', component: AdminPanel },
  { path: '/about', component: About },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
