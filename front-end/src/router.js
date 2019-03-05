import Vue from 'vue'
import Router from 'vue-router'
import Weather from './views/Weather.vue'
import Txt from './views/TxtGetter.vue'
import Display from './views/Display.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'weather',
      component: Weather
    },
    {
      path: '/txt-getter',
      name: 'txt-getter',
      component: Txt
    },
    {
      path: '/display',
      name: 'display',
      component: Display
    }
  ]
})
