import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from './components/HomeComponent.vue';
import LoginForm from './components/LoginForm.vue';
import RegisterForm from './components/RegisterForm.vue';
import AboutComponent from './components/AboutComponent.vue';
import WeatherComponent from './components/WeatherComponent.vue';
import ContactComponent from './components/ContactComponent.vue';
import DepartamentsComponent from './components/DepartamentsComponent.vue';
import HousesComponent from './components/HousesComponent.vue';
import OfficesComponent from './components/OfficesComponent.vue';
import AdministrationComponent from './components/AdministrationComponent.vue';


const routes = [
  { path: '/', component: HomeComponent },
  { path: '/iniciarsesion', component: LoginForm },
  { path: '/registro', component: RegisterForm },
  { path: '/nosotros', component: AboutComponent },
  { path: '/clima', component: WeatherComponent },
  { path: '/contacto', component: ContactComponent },
  { path: '/departamentos', component: DepartamentsComponent },
  { path: '/casas', component: HousesComponent },
  { path: '/oficinas', component: OfficesComponent },
  { path: '/administracion', component: AdministrationComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
