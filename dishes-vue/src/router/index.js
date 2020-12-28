import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/registration',
    name: 'Reg',
    component: () => import('../views/Reg.vue')
  },
  {
    path: '/dishes',
    name: 'Dishes',
    component: () => import('../views/Dishes.vue')
  },
  {
    path: '/dish/:id',
    name: 'Dish',
    props: true,
    component: () => import('../views/Dish.vue')
  },
  {
    path: '/user',
    name: 'User',
    component: () => import('../views/User.vue')
  },
  {
    path: '/questions',
    name: 'Questions',
    component: () => import('../views/Questions.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
