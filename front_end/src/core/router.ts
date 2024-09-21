// 创建路由器并暴露出去
import path from 'path'
// 1.引入createrRouter
import {createRouter,createWebHistory} from 'vue-router'
import Login from '@/components/login/Login.vue'
import Login2 from '@/components/login/Login2.vue'
import Person from '@/components/Person.vue'
import home from '@/components/main/home.vue'
import chart from '@/components/main/chart.vue'
import management from '@/components/main/management.vue'
// 2.创建路由器
const router = createRouter({
  history:createWebHistory(),//路由器的工作模式
  routes:[
    {
      path:'/login',
      component:Login
    },
    {
      path:'/person',
      component:Person
    },
    {
      path:'/',
      component:Login2
    },
    {
      path:'/home',
      component:home
    },
    {
      path:'/chart',
      component:chart
    },
    {
      path:'/management',
      component:management
    },
  ]
})

// 暴露出去router
export default router