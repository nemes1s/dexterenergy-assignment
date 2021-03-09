import Vue from 'vue'
import App from './App.vue'
import DateRangePicker from 'vue-mj-daterangepicker'
import 'vue-mj-daterangepicker/dist/vue-mj-daterangepicker.css'
import router from './router'

Vue.config.productionTip = false

Vue.use(DateRangePicker)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
