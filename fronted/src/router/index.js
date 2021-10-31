import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import FAQ from '../views/FAQ.vue'
import Contact from "../views/Contact";
import Table from "../views/Table";
import Statement from "../views/Statement";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/table',
    name: 'Table',
    component: Table
  },
  {
    path: '/statement',
    name: 'Statement',
    component: Statement
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: FAQ
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
