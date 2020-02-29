import Vue from 'vue'
import VueRouter from 'vue-router'
import Journal from '@/components/Journal'
import Dashboard from '@/components/Dashboard'
import ItemTypes from '@/components/ItemTypes'
import Login from '@/components/Login'
import Home from '@/components/Home'

Vue.use(VueRouter)

const routes = [
  {
    path: '/journal',
    name: 'Journal',
    component: Journal
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/item-types',
    name: 'ItemTypes',
    component: ItemTypes
  },
  {
    path: '/login',
    name: "Login",
    component: Login
  },
  {
    path: '/',
    name: "Home",
    component: Home
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
