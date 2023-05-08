import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UploadValuesView from '../views/UploadValuesView.vue'
import EditValuesView from '@/views/EditValuesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/upload_values',
      name: 'upload_values',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/AboutView.vue')
      component: UploadValuesView
    },
    {
      path: '/edit_values',
      name: 'edit_values',
      component: EditValuesView
    }
  ]
})

export default router
