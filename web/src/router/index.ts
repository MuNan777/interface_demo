import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import _ from 'lodash'
import { IImportModule } from '../types'

// 载入路由
const routes = _.values(import.meta.glob('../view/*/route.ts', { eager: true })).map(item => {
  const module = item as IImportModule<RouteRecordRaw>
  return module.default
})

const router = createRouter({
  // use hash
  history: createWebHashHistory(),
  routes, // `routes: routes` 的缩写
})

export default router