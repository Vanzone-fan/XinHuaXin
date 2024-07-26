import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import ElementUI from "element-ui";

import "element-ui/lib/theme-chalk/index.css";
import "../src/assets/global.css";

import TopNavigation from "./components/TopNavigation.vue";
Vue.component("topNav", TopNavigation);

import AsideNavigation from "./components/AsideNavigation.vue";
Vue.component("asideNav", AsideNavigation);

import Loading from "./components/Loading.vue";
Vue.component("loading",Loading)

Vue.use(ElementUI);
Vue.config.productionTip = false;

new Vue({
    router,
    render: (h) => h(App),
}).$mount("#app");
