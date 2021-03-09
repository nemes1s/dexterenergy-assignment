import Vue from 'vue'
import App from './App.vue'
import DateRangePicker from 'vue-mj-daterangepicker'
import 'vue-mj-daterangepicker/dist/vue-mj-daterangepicker.css'

Vue.config.productionTip = false

Vue.use(DateRangePicker)

new Vue({
  render: h => h(App),
}).$mount('#app')
