// 引入createApp用于创建应用
import { createApp } from "vue";
// 引入App根组件
import App from "./App.vue";
// 引入路由器
import router from "./core/router";
// 引入数据交互axios
import axios from "axios";


// createApp(App).mount('#app')
// 创建一个应用
const app = createApp(App)
// 使用路由器
app.use(router)
// 使用axios
app.use(axios)
// 引入Element
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
app.use(ElementPlus);

import * as ElementPlusIconsVue from '@element-plus/icons-vue'

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

// 挂载整个应用到App容器中 index.html 中的 id 为 app 的 div 标签上
app.mount('#app')


// ../上一级    ./同级      @/根目录下

// 创建 Vue 实例对象
// new Vue({
//     render: h => h(App),  // render 函数将帮助解析模板，传入的参数 h 为一个函数，该函数可用来解析 App 这个组件
//     router
// }).$mount('#app') // 将 App.vue 组件挂载到 index.html 中的 id 为 app 的 div 标签上
