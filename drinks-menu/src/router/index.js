import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../HomePage.vue';
import DrinkDetail from '../components/DrinkDetail.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/drink/:id', name: 'DrinkDetail', component: DrinkDetail },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
