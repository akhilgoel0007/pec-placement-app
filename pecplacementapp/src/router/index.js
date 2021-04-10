import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from "../views/Dashboard.vue"
import JobProfiles from "../views/dashboard-views/JobProfiles";
import JobView from "../views/dashboard-views/JobView";
import MyAccount from "../views/dashboard-views/MyAccount";
import MyProfile from "../views/dashboard-views/MyProfile";
import JobEntry from "../views/dashboard-views/JobEntry";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    // path: '/dashboard',
    name: 'Home',
    component: Home
  },

  {
    path: '/dashboard',
    // path: '/',
    name: 'Dashboard',
    component: Dashboard,
    children: [
      { path: '/', component: MyProfile },
      { path: '/jobview', props: true, component: JobView },
      { path: '/jobentry', component: JobEntry },
      { path: '/account', component: MyAccount },
      { path: '/jobprofiles', component: JobProfiles },
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
