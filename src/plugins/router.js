import Vue from 'vue'
import VueRouter from 'vue-router'
import Journal from '@/views/Journal'
import Dashboard from '@/views/Dashboard'
import ItemTypes from '@/views/ItemTypes'
import LandingPage from '@/views/LandingPage'


Vue.use(VueRouter)

const routes = [
  {
    path: '/journal',
    name: 'Journal',
    meta: { layout: 'main' },
    component: Journal
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    meta: { layout: 'main' },
    component: Dashboard
  },
  {
    path: '/item-types',
    name: 'ItemTypes',
    meta: { layout: 'main' },
    component: ItemTypes
  },
  {
    path: '/',
    name: "LandingPage",
    meta: { layout: 'landing' },
    component: LandingPage
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  if (to.name !== "LandingPage" && localStorage.getItem("access_token") == null) {
    // console.log("From A " + to.name)
    next({ name: "LandingPage" })
  }
  else if (to.name == "LandingPage" && localStorage.getItem("access_token") !== null) {
    // console.log("From B " + to.name )
    next({ name: "Journal" })
  } else {
    // console.log("From C " + to.name)
    next()
  }
})

export default router
