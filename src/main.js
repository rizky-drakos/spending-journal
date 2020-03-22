import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'

import ApiService from "./services/api.service"
import TokenService from "./services/token.service"


Vue.config.productionTip = false

ApiService.init("http://192.168.1.101:5000")
// In case the user refreshes the page, headers
// needs to be re-initialized.
if(TokenService.get_token()) {
  ApiService.set_access_token()
}

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
