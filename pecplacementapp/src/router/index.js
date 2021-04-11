import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from "../views/Dashboard.vue"
import JobView from "../views/dashboard-views/JobView";
import JobEntry from "../views/dashboard-views/JobEntry";
import MyAccount from "../views/dashboard-views/MyAccount";
import MyProfile from "../views/dashboard-views/MyProfile";
import JobProfiles from "../views/dashboard-views/JobProfiles";
import StudentProfiles from "../views/dashboard-views/StudentProfiles";
import MyApplications from "../views/dashboard-views/ShowMyApplications";
import ShowAllApplicants from "../views/dashboard-views/ShowAllApplicants";

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
      { path: '/jobentry', component: JobEntry },
      { path: '/account', component: MyAccount },
      { path: '/jobprofiles', component: JobProfiles },
      { path: '/myapplications', component: MyApplications},
      { path: '/jobview', props: true, component: JobView },
      { path: '/studentprofiles', component: StudentProfiles },
      { path: '/showallapplicants', component: ShowAllApplicants },
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
