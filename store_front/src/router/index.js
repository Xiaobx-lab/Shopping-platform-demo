import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import goodsDetail from '@/views/goodsDetails'
import login from '@/views/login'
import register from '@/views/register'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/goods/goodsDetail/:id',
      name: 'goodsDetail',
      component: goodsDetail
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
  ]
})
