import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UploadFileView from '../views/UploadFileView.vue'
import EditDataView from '../views/EditDataView.vue'
import StatusView from "@/views/StatusView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/upload_data',
      name: 'upload_data',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/AboutView.vue')
      component: UploadFileView
    },
    {
      path: '/edit_data',
      name: 'edit_data',
      component: EditDataView
    },
    {
      path: '/system_status',
      name: 'system_status',
      component: StatusView
    },
    {
      path: '/:catchAll(.*)',
      component: () => import('@/views/Error404.vue')
    }
  ]
})

export default router
