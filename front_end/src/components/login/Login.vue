<template>
  <div class="login">
    <div class="login-middle">
      <div class="common-layout">
        <div class="login-middle-header">
            <div class="login-middle-header-header">
              <a>弹幕分析</a>
              <p>直播平台弹幕情感分析</p>
              <!-- <li v-for="item in admin">{{ item.user_email }}</li> -->
            </div>
            <div class="login-middle-main">
              <div class="login-middle-main-top">
                <el-input v-model="Form.uname" class="login-middle-main-top-input" placeholder="账号" size="large" :suffix-icon="User"/>
                <el-input v-model="Form.password" type="password" class="login-middle-main-top-input" placeholder="密码" show-password size="large"/>
                <el-button size="large" type="primary" class="login-middle-main-top-button" v-loading="loading" @click="login">登录</el-button>
              </div>
            </div>
            <div class="login-footer">
              <el-link :underline="false" class="login-footer-right">注册</el-link>
              <el-link :underline="false" class="login-footer-left">忘记密码</el-link>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { User,View } from '@element-plus/icons-vue'

import Axios from 'axios';
export default{
  name:'Login',
  data() {
    return {
      Form: {
        uname: "",
        password: "",
      },
      admin:{}
    }
  },
  created(){
    this.login();
  },
  methods: {
    login(){
      var url = "http://127.0.0.1:8000/api/admin/";
      Axios.get(url).then(response => {this.admin = response.data;})
      console.log(this.admin)
      console.log("执行成功")
      let num = this.admin.length
      for(let i=0;i<num;i++){
        console.log(this.admin[i].user_email)
        if (this.Form.uname == this.admin[i].user_email && this.Form.password == this.admin[i].pass_word) {
          this.$router.push('/person')
          console.log("success")
        }else{
          console.log("error")
        }
      }
    },
  }
}

</script>

<style scoped>
.login{
  height: 100vh;
  width: 100vw;
}
.login-middle{
  background-color: rgb(255, 255, 255);
  width: 58vh;
  height: 44vh;
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  box-shadow: 0 0 10px;
  border-radius: 10px;
}
.login-middle-header{
  padding: 20px;
}
.login-middle-header-header{
  font-size: 30px;
}
.login-middle-header-header a{
  display: table;
  margin: 0 auto;
  line-height: 45px;
}
.login-middle-header-header p{
  display: table;
  margin: 0 auto;
  font-size: 14px;
  line-height: 24px;
  color: rgb(108, 117, 125);
}
.login-middle-main-top-input{
  line-height: 24px;
  width: 50vw;
  padding: 12px 12px;
}
.login-middle-main-top-button{
  width: 386px;
  margin: 10px 12px;
}
.login-footer{
  margin: 12px 12px;
  width: 386px;
  color: rgb(108, 117, 125);
}
.login-footer-right{
  left: 354px;
}
.login-footer-left{
  left: -24px;
}
</style>