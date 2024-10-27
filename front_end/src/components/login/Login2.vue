<template>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <div class="background"></div>

    <body>
        <img src="../../assets/img/22.gif" class="pic" ref="pic" alt="pic" style="position: absolute;">
        <!-- <header class="header">
            <nav class="navbar">
                <a href="#">首页</a>
                <a href="../../assets/html/meitu.html">美图</a>
                <a href="../../assets/html/poetry.html">诗词</a>
            </nav>
            <form action="" class="search-bar"> -->
        <!-- placeholder属性是用来设置表单元素的占位符文本的。-->
        <!-- <input type="text" placeholder="搜索...">
                <button><i class='bx bx-search'></i></button>
            </form>
        </header> -->
        <div class="background"></div>
        <div class="container">
            <div class="item">
                <h2 class="logo"><i class='bx bxl-vimeo'>Love</i></h2>
                <div class="text-item">
                    <h2>弹幕情感分析系统</h2><br>
                    <h3><span>开始使用</span></h3>
                    <p>永远不要沉溺在安逸里得过且过，能给你遮风挡雨的，同样能让你不见天日。只有让自己更加强大，才能真正地撑起一片天。</p>
                    <div class="social-icon">
                        <a href="#"><i class="bx bxl-facebook"></i></a>
                        <a href="#"><i class="bx bxl-twitter"></i></a>
                        <a href="#"><i class="bx bxl-youtube"></i></a>
                        <a href="#"><i class="bx bxl-instagram"></i></a>
                        <a href="#"><i class="bx bxl-linkedin"></i></a>
                    </div>
                </div>
            </div>
            <div class="login-section">
                <div class="form-box login">
                    <form action="">
                        <h2>登录</h2>
                        <div class="input-box">
                            <span class="icon"><i class="bx bxs-envelope"></i></span>
                            <input type="email" v-model="Form.email" required>
                            <label for="">邮箱</label>
                        </div>
                        <div class="input-box">
                            <span class="icon"><i class="bx bxs-lock-alt"></i></span>
                            <input type="password" v-model="Form.password" required>
                            <label for="">密码</label>
                        </div>
                        <div class="remember-password">
                            <label for=""><input type="checkbox">记住密码</label>
                            <a href="#">忘记密码</a>
                        </div>
                        <button class="btn" @click="login" type="submit" :plain="true">登录</button>
                        <div class="create-accout">
                            <p>创建一个新账户?<a href="#" class="register-link">注册</a></p>
                        </div>
                    </form>
                </div>
                <div class="form-box register">
                    <form action="">

                        <h2>注册</h2>

                        <div class="input-box">
                            <span class="icon"><i class="bx bxs-user"></i></span>
                            <input type="text" v-model="register_from.uname" required>
                            <label for="">名称</label>
                        </div>
                        <div class="input-box">
                            <span class="icon"><i class="bx bxs-envelope"></i></span>
                            <input type="email" v-model="register_from.email" required>
                            <label for="">邮箱</label>
                        </div>
                        <div class="input-box">
                            <span class="icon"><i class="bx bxs-lock-alt"></i></span>
                            <input type="password" v-model="register_from.password" required>
                            <label for="">密码</label>
                        </div>
                        <div class="remember-password">
                            <label for=""><br><input type="checkbox">同意协议</label>
                        </div>
                        <button class="btn" @click="register">注册</button>
                        <div class="create-accout">
                            <p>已经有账户了吗?<a href="#" class="login-link">登录</a></p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div class="foot">
            <p><i class='bx bx-copyright'></i>版权所有 Love</p>
        </div>
    </body>
</template>

<script>
    import { ElMessage } from 'element-plus'
    import Axios from 'axios';
    export default {
        name: 'Login2',
        data() {
            return {
                Form: {
                    email: "",
                    password: "",
                },
                register_from: {
                    uname: "",
                    email: "",
                    password: ""
                },
                admin: {},
            }
        },
        created() {
            // let email = document.getElementById('email').value
            // console.log(email)
            this.start();
        },
        methods: {
            start() {
                var url = "http://127.0.0.1:8000/api/admin/";
                Axios.get(url).then(response => { this.admin = response.data; })
                console.log("链接成功")
                console.log(this.admin)
            },
            login() {
                event.preventDefault();
                let num = this.admin.length
                for (let i = 0; i < num; i++) {
                    console.log(this.admin[i].user_email)
                    if (this.Form.email.length == 0 && this.Form.password.length == 0) {
                        ElMessage.error('请填写邮箱或者密码')
                        break;
                    } else if (this.Form.email == this.admin[i].user_email && this.Form.password == this.admin[i].pass_word) {
                        this.$router.push('/home')
                        console.log("success")
                        ElMessage({
                            message: '登录成功！',
                            type: 'success',
                        })
                        break;
                    } else if (i == num - 1) {
                        ElMessage({
                            message: '邮箱或者密码不正确',
                            type: 'warning',
                        })
                    }
                }
            },
            register() {
                var url = "http://127.0.0.1:8000/api/admin/";
                Axios.post(url, { 'user_name': this.register_from.uname, 'pass_word': this.register_from.password, 'user_email': this.register_from.email })
                ElMessage({
                    message: '注册成功！',
                    type: 'success',
                })
            }
        },
        mounted() {
            const pic = this.$refs.pic;
            document.addEventListener('mousemove', (e) => {
                // 计算图片应该移动到的位置
                //   console.log("原",e.clientX,e.clientY)
                const x = e.clientX + 10;
                const y = e.clientY - 820;
                //   console.log(x,y)

                // 更新图片的位置
                pic.style.left = x + 'px';
                pic.style.top = y + 'px';
            });
            const loginsec = document.querySelector('.login-section')
            const loginlink = document.querySelector('.login-link')
            const registerlink = document.querySelector('.register-link')
            registerlink.addEventListener('click', () => {
                loginsec.classList.add('active')
            })
            loginlink.addEventListener('click', () => {
                loginsec.classList.remove('active')
            })
        }
    }
</script>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Simsun", sans-serif;
    }

    body {
        height: 100vh;
        width: 100%;
        background-color: black;
        position: fixed;
    }

    .background {
        background: url(../../assets/img/background2.jpg) no-repeat;
        background-position: center;
        background-size: cover;
        height: 100vh;
        width: 100%;
        /* 用于为元素添加一个视觉效果。它可以用于实现模糊、色彩变换、亮度调整等效果。 */
        filter: blur(12px);
    }

    .container {
        position: absolute;
        left: 50%;
        top: -50%;
        transform: translate(-50%, -50%);
        width: 75%;
        height: 550px;
        margin-top: 20px;
        background: url(../../assets/img/background2.jpg) no-repeat;
        background-position: center;
        background-size: cover;
        border-radius: 20px;
        overflow: hidden;
    }

    .item {
        position: absolute;
        top: 0;
        left: 0;
        width: 58%;
        height: 100%;
        color: #fff;
        background-color: transparent;
        padding: 80px;
        display: flex;
        justify-content: space-between;
        flex-direction: column;
    }

    .item .logo {
        color: #fff;
        font-size: 30px;
    }

    .text-item h2 {
        font-size: 36px;
        line-height: 1.2;
        margin: -12px auto;
    }

    .text-item p {
        font-size: 16px;
        margin: 20px 0;
        line-height: 1.5;
    }

    .social-icon a i {
        color: #fff;
        font-size: 24px;
        margin-left: 10px;
        cursor: pointer;
        transition: .5s ease;
    }

    .social-icon a:hover i {
        transform: scale(1.2);
    }

    .container .login-section {
        position: absolute;
        top: 0;
        right: 0;
        /* calc计算元素的宽度为父元素宽度减去58% */
        width: calc(100% - 58%);
        height: 100%;
        color: #fff;
        /* 是CSS中的一个属性，用于为元素的背景添加一个视觉效果。它可以用于实现模糊、色彩变换、亮度调整等效果。以下是backdrop-filter的常见取值：
    blur(radius)：为元素的背景添加高斯模糊效果，其中radius表示模糊半径。
    brightness(value)：调整元素的背景亮度，其中value表示亮度值，可以是百分比或小数。
    contrast(value)：调整元素的背景对比度，其中value表示对比度值，可以是百分比或小数。
    grayscale(value)：将元素的背景转换为灰度图像，其中value表示灰度值，可以是百分比或小数。
    hue-rotate(angle)：调整元素的背景色相，其中angle表示色相角度，可以是正数或负数。
    invert(value)：将元素的背景颜色反转，其中value表示反转值，可以是百分比或小数。
    opacity(value)：调整元素的背景透明度，其中value表示透明度值，可以是百分比或小数。
    saturate(value)：调整元素的背景饱和度，其中value表示饱和度值，可以是百分比或小数。
    sepia(value)：将元素的背景转换为棕褐色图像，其中value表示棕褐色值，可以是百分比或小数。 */
        backdrop-filter: blur(10px);
    }

    .login-section .form-box {
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
    }

    .login-section .form-box.register {
        transform: translateX(530px);
        transition: transform .6s ease;
        transition-delay: 0s;
    }

    .login-section.active .form-box.register {
        transform: translateX(0px);
        transition-delay: .7s;
    }

    .login-section .form-box.login {
        transform: translateX(0px);
        transition: transform .6s ease;
        transition-delay: 0.7s;
    }

    .login-section.active .form-box.login {
        transform: translateX(530px);
        transition-delay: 0s;
    }

    .login-section .form-box h2 {
        text-align: center;
        font-size: 25px;
    }

    .form-box .input-box {
        width: 340px;
        height: 50px;
        border-bottom: 2px solid #fff;
        margin: 30px 0;
        position: relative;
    }

    .input-box input {
        width: 100%;
        height: 100%;
        background: transparent;
        border: none;
        outline: none;
        font-size: 16px;
        padding-right: 28px;
        color: #fff;
    }

    .input-box label {
        position: absolute;
        top: 31%;
        left: 0;
        transform: translateT(-50%);
        font-size: 16px;
        font-weight: 600px;
        pointer-events: none;
        transition: .5s ease;
    }

    .input-box .icon {
        position: absolute;
        top: 13px;
        right: 0;
        font-size: 19px;
    }

    /* 当用户聚焦在<input>元素上时，与其相邻的<label>元素的颜色将变为红色。 */
    .input-box input:focus~label,
    /* 当用户在<input>元素中填写了有效值时，与其相邻的<label>元素的颜色将变为绿色。 */
    .input-box input:valid~label {
        top: -15px;
        color: aquamarine;
    }

    .remember-password {
        font-size: 14px;
        font-weight: 500;
        margin: -15px 0 15px;
        display: flex;
        justify-content: space-between;
    }

    .remember-password label input {
        accent-color: #fff;
        margin-right: 3px;
    }

    .remember-password a {
        color: #fff;
        text-decoration: none;
    }

    .remember-password a:hover {
        text-decoration: underline;
    }

    .btn {
        background: #fff;
        width: 100%;
        height: 45px;
        outline: none;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        background: #0362d8;
        font-size: 16px;
        color: #fff;
        box-shadow: rgba(0, 0, 0, 0.4);

    }

    .create-accout {
        font-size: 14.5px;
        text-align: center;
        margin: 25px;

    }

    .create-accout p a {
        color: #fff;
        font-weight: 600px;
        text-decoration: none;
    }

    .create-accout p a:hover {
        text-decoration: underline;
    }

    .foot p {
        color: #fff;
        position: absolute;
        bottom: 0;
        font-size: 15px;
        left: 47%;
    }

    .pic {
        position: absolute;
        width: 60px;
        height: 60px;
        z-index: 111;
    }
</style>