import Vue from 'vue'
import VueRouter from 'vue-router'
import Journal from '@/components/Journal'
import Dashboard from '@/components/Dashboard'
import ItemTypes from '@/components/ItemTypes'
import LandingPage from '@/components/LandingPage'
// import AutheticationStore from '../stores/AuthenticationStore' 

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
  if (to.name !== "LandingPage" && localStorage.getItem("user") == null) {
    console.log("From A " + to.name)
    next({ name: "LandingPage" })
  }
  else if (to.name == "LandingPage" && localStorage.getItem("user") !== null) {
    console.log("From B " + to.name )
    next({ name: "Journal" })
  } else {
    console.log("From C " + to.name)
    next()
  }
})

export default router
