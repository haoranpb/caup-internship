import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { Container, Main, Button, Col, Row, Header, Cascader, Select, Tabs, Input, Option, TabPane } from 'element-ui';

Vue.config.productionTip = false;
Vue.use(Button);
Vue.use(Container);
Vue.use(Main);
Vue.use(Col);
Vue.use(Row);
Vue.use(Header);
Vue.use(Cascader);
Vue.use(Select);
Vue.use(Tabs);
Vue.use(Input);
Vue.use(Option);
Vue.use(TabPane);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
