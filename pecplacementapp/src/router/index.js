import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from "../views/Dashboard.vue"
import JobProfiles from "../views/dashboard-views/JobProfiles";
import StudentProfiles from "../views/dashboard-views/StudentProfiles";
import ShowAllApplicants from "../views/dashboard-views/ShowAllApplicants";
import JobView from "../views/dashboard-views/JobView";
import MyAccount from "../views/dashboard-views/MyAccount";
import MyProfile from "../views/dashboard-views/MyProfile";
import JobEntry from "../views/dashboard-views/JobEntry";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    children: [
      { path: '/', component: MyProfile },
      { path: '/studentprofiles', component: StudentProfiles },
      { path: '/showallapplicants', component: ShowAllApplicants },
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
