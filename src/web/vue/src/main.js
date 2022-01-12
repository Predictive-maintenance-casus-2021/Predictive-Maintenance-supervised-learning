import Vue from "vue";
import App from "./App.vue";
import "./assets/tailwind.css";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:5000/";
Vue.prototype.$http = axios;

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
