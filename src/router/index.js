import Vue from 'vue'
import VueRouter from 'vue-router'
import Journal from '@/components/Journal'
import Dashboard from '@/components/Dashboard'
import ItemTypes from '@/components/ItemTypes'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
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
  }
]

const router = new VueRouter({
  routes
})

export default router
