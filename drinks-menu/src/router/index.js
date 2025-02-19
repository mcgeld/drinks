import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import DrinkDetail from '../components/DrinkDetail.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/drink/:id', component: DrinkDetail }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;