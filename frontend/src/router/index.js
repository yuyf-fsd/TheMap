import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TestAta from '@/components/TestAta'
import LeafletMap from '@/components/LeafletMap'
import Simple from '@/components/Simple'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test',
      name: 'TestAta',
      component: TestAta
    },
    {
      path: '/leafletmap',
      name: 'LeafletMap',
      component: LeafletMap
    },
    {
      path: '/simple',
      name: 'Simple',
      component: Simple
    }
  ]
})
