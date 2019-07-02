import Vue from 'vue'
import Router from 'vue-router'
import Weather from './views/Weather.vue'
import Txt from './views/TxtGetter.vue'
import Display from './views/Display.vue'
import Display1 from './components/display-1.vue'
import Display2 from './components/display-2.vue'
import Display3 from './components/display-3.vue'
import Display4 from './components/display-4.vue'
import Display5 from './components/display-5.vue'
import STLParser from './views/STLParser.vue'
import Mail from './views/Mail.vue'
import Log from './views/Log.vue'
import TreeManager from './views/TreeManager.vue'
import TreeRecord from './components/TreeRecord.vue'
import TreeMaintain from './components/TreeMaintain.vue'
import TreeDanger from './components/TreeDanger.vue'


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
      path: '/mail',
      name: 'mail',
      component: Mail
    },
    {
      path: '/log',
      name: 'log',
      component: Log
    },
    {
      path: '/tree',
      name: 'tree',
      component: TreeManager,
      children: [
        {
          path: 'tree-record',
          name: 'tree-record',
          component: TreeRecord
        },
        {
          path: 'tree-danger',
          name: 'tree-danger',
          component: TreeDanger
        },
        {
          path: 'tree-maintain',
          name: 'tree-maintain',
          component: TreeMaintain
        }
      ]
    },
    {
      path: '/txt-getter',
      name: 'txt-getter',
      component: Txt
    },
    {
      path: '/stlparser',
      name: 'stlparser',
      component: STLParser
    },
    {
      path: '/display',
      name: 'display',
      component: Display,
      children: [
        {
          path: 'd1',
          name: 'd1',
          component: Display1
        },
        {
          path: 'd2',
          name: 'd2',
          component: Display2
        },
        {
          path: 'd3',
          name: 'd3',
          component: Display3
        },
        {
          path: 'd4',
          name: 'd4',
          component: Display4
        },
        {
          path: 'd5',
          name: 'd5',
          component: Display5
        },
      ]
    }
  ]
})
