import { createRouter, createWebHistory } from 'vue-router'
import PackageList from '../views/PackageList.vue'
import PackageDetail from '../views/PackageDetail.vue'

const routes = [
  { path: '/', component: PackageList },
  { path: '/packages/:id', component: PackageDetail, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
