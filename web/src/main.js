import Vue from 'vue'
import vuetify from './plugins/vuetify';
import router from './plugins/router'

import ApiService from "./services/api.service"
import TokenService from "./services/token.service"
import App from './App.vue'
import Landing from './layouts/Landing.vue'
import Main from './layouts/Main.vue'

Vue.config.productionTip = false

ApiService.init("http://192.168.1.6:5000")
// In case the user refreshes the page, headers
// needs to be re-initialized.
if(TokenService.get_token()) {
  ApiService.set_access_token()
}

Vue.component('main-layout', Main)
Vue.component('landing-layout', Landing)

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
