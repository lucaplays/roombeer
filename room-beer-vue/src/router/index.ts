import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CntrView from '../views/ControlView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/cntrl',
    name: 'control',
    component: CntrView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
