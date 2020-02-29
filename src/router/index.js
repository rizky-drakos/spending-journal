import Vue from 'vue'
import VueRouter from 'vue-router'
import Journal from '@/components/Journal'
import Dashboard from '@/components/Dashboard'
import ItemTypes from '@/components/ItemTypes'
import LandingPage from '@/components/LandingPage'
import AutheticationStore from '../stores/AuthenticationStore'

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
    path: '/',
    name: "LandingPage",
    component: LandingPage
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  // if the user is not authenticated
  if (to.name !== "LandingPage" && !AutheticationStore.data.isAuthenticated) next({ name: "LandingPage" })
  // if the user has been authenticated
  else next()
})

export default router
