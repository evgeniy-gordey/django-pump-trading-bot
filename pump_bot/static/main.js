import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'

import VueProgressBar from 'vue-progressbar'

import Main from './Main.vue'

// Axios csrf settings
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// Progress bar interceptors
axios.interceptors.request.use((config) => { router.app.$Progress.start(); return config }, function (error) { router.app.$Progress.fail(); return Promise.reject(error) })
axios.interceptors.response.use((response) => { router.app.$Progress.finish(); return response }, function (error) { router.app.$Progress.fail(); return Promise.reject(error) })


Vue.use(Meta)
Vue.use(VueProgressBar)

/* eslint-disable no-new */
new Vue({
  el: '#main',
  router,
  store,
  render: h => h(Main)
})
