import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/monografias',
    name: 'Monografias',
    component: () => import(/* webpackChunkName: "monografias" */ '../views/Monografias.vue')
  },
  {
    path: '/autores',
    name: 'Autores',
    component: () => import(/* webpackChunkName: "autores" */ '../views/Autores.vue')
  },
  {
    path:'/editar/:id',
    name: 'Editar',
    component: () => import(/* webpackChunkName : "editar" */ '../views/Editar.vue'),
    props: true
  },
  {
    path: '/cadastros',
    name: 'Cadastros',
    component: () => import(/* webpackChunkName: "autores" */ '../views/Cadastros.vue')
  },
  {
    path: '/editarcadastro/:id',
    name: 'EditarCadastro',
    component: () => import(/* webpackChunkName: "autores" */ '../views/EditarCadastro.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
