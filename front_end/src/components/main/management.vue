<template>
<div class="background"></div>
<body>
    <img src="../../assets/img/22.gif" class="pic" ref="pic" alt="pic" style="position: absolute;">
    <header class="header">
        <nav class="navbar">
            <a href="#" @click="home_skip">首页</a>
            <a href="#" @click="chart_skip">图表</a>
            <a href="#">管理</a>
            <a href="#" @click="login_skip">退出</a>
        </nav>
        <form action="" class="search-bar">
        </form>
    </header>
    <div class="container">
        <div class="main">
            <el-tabs :tab-position="tabPosition" style="height: 87%;">
                <el-tab-pane label="用户管理">
                    <table>
                        <thead>
                            <tr>
                                <th>用户名称</th>
                                <th>用户邮箱</th>
                                <th>用户密码</th>
                                <th>用户管理</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in admin" :key="item.id">
                                <td>{{ item.user_name }}</td>
                                <td>{{ item.user_email }}</td>
                                <td>{{ item.pass_word }}</td>
                                <td>
                                    <el-icon @click="deleteList(item.user_email)"><Delete /></el-icon>
                                </td>
                            </tr>
                        </tbody>
                        <div class="page">
                            <el-pagination
                            layout="prev, pager, next" 
                            :background="true" 
                            :total="1"
                            :page-size="12"
                            :hide-on-single-page="true"
                            />
                        </div>
                    </table>
                </el-tab-pane>
                <el-tab-pane label="弹幕管理">
                    <table>
                        <thead>
                            <tr>
                                <th>房间号</th>
                                <th>用户姓名</th>
                                <th>弹幕内容</th>
                                <th>弹幕性质</th>
                                <th>弹幕管理</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in barrage" :key="item.id" :class="index % 2 === 0 ? 'even-row' : ''">
                                <td>{{ item.rood_id }}</td>
                                <td>{{ item.name }}</td>
                                <td>{{ item.content }}</td>
                                <td>{{ item.nature_of_words }}</td>
                                <td>
                                    <el-icon @click="deleteBarrage(item.id)"><Delete /></el-icon>
                                </td>
                            </tr>
                        </tbody>
                        <div class="page">
                            <el-pagination 
                            layout="prev, pager, next" 
                            :background="true" 
                            :total="sum"
                            :page-size="12"
                            :hide-on-single-page="true"
                            :current-page="currentPage"
                            @current-change="handleCurrentChange"
                            @click="get_barrage(this.currentPage)"
                            />
                        </div>
                    </table>
                    <el-button class="all" type="danger" @click="deleteBarrageAll">删除所有</el-button>
                </el-tab-pane>
            </el-tabs>
        </div>
    </div>
</body>
</template>

<script>
import { Delete } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus'
import Axios from 'axios';

export default {
    name:'management',
    data() {
        return {
            admin: [],
            barrage: [],
            tabPosition: 'left',
            sum: 130,
            currentPage: 1,
        }
    },
    created(){
        this.start();
        this.get_barrage();
    },
    methods: {
        start(){
            var url = "http://127.0.0.1:8000/api/admin/";
            Axios.get(url).then(response => {this.admin = response.data;})
            var url = "http://127.0.0.1:8000/api/pagSum/";
            Axios.get(url).then(response => {this.sum = response.data;})
            console.log("链接成功")
        },
        home_skip(){
            this.$router.push('/home')
        },
        login_skip(){
            this.$router.push('/login2')
        },
        chart_skip(){
            this.$router.push('/chart')
        },
        management_skip(){
            this.$router.push('/management')
        },
        // 删除数据库
        deleteList(email){
            var url = "http://127.0.0.1:8000/api/account_management/"+email;
            Axios.get(url).then(response => {this.admin1 = response.data;})
            // 发送 Axios 请求执行删除操作
            ElMessage({
            message: "删除成功",
            type: 'success',
            })
            setTimeout(this.start,250)
        },
        deleteBarrage(id){
            var url = "http://127.0.0.1:8000/api/barrage_delete/"+id;
            Axios.get(url).then(response => {this.admin1 = response.data;})
            // 发送 Axios 请求执行删除操作
            ElMessage({
            message: "删除成功",
            type: 'success',
            })
            setTimeout(this.get_barrage,250)
        },
        deleteBarrageAll(){
            var url = "http://127.0.0.1:8000/api/barrage_delete_all/";
            Axios.get(url).then(response => {this.admin1 = response.data;})
            // 发送 Axios 请求执行删除操作
            ElMessage({
            message: "删除成功",
            type: 'success',
            })
        },
        handleClick(tab, event) {
            console.log(tab, event);
        },
        get_barrage(){
            var url = "http://127.0.0.1:8000/api/paging/"+this.currentPage;
            Axios.get(url).then(response => {this.barrage = response.data;})
        },
        // 当前页改变，处理函数
        handleCurrentChange(newPage) {
            this.currentPage = newPage
        },
    },
    mounted(){
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
    }
}
</script>




<style scoped>

.all{
    position: fixed;
    top:84%;
    right: 12%;
}

.page{
    position: fixed;
    height: 100%;
    margin: 20px;
    top:82%;
}

table{
    width: 100%;
    border-radius: 20px;
    overflow: hidden;
    border-collapse: collapse;
    table-layout: fixed;
}

tr{
    border-bottom: 1px solid rgb(64, 158, 255,1);
}

td{
    padding: 10px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    text-align: center;
}

th{
    padding: 10px;

}

.main{
    margin: 10px 100px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 20px;
    height: 90%;
}


.container{
    position: absolute;
    left: 50%;
    top: -52%;
    transform: translate(-50%,-50%);
    width: 99%;
    margin-top: 15px;
    background: black;
    background-position: center;
    background-size: over;
    border-radius: 20px;
    background-color: rgb(0, 0, 0,0.5);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.8);
    height: 97%;
    padding-top: 6%;
}
/* 隐藏浏览器默认的滚动条 */
::-webkit-scrollbar {
    display: none; /* Safari 和 Chrome */
    }
    ::-moz-scrollbar {
    display: none; /* Firefox */
    }
    ::-ms-scrollbar {
    display: none; /* Edge */
    }
    
    /* 自定义滚动条的样式 */
    ::-webkit-scrollbar {
    width: 10px; /* 设置滚动条宽度 */
    background-color: #f1f1f1; /* 设置滚动条背景色 */
    }
    
    ::-webkit-scrollbar-thumb {
    background-color: #888; /* 设置滚动条滑块颜色 */
    border-radius: 5px; /* 设置滚动条滑块的圆角 */
    }
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Simsun",sans-serif;
}
body{
    height: 100vh;
    width: 100%;
    background-color: black;
    position: fixed;
}
.background{
    background: url(../../assets/img/background2.jpg) no-repeat;
    background-position: center;
    background-size: over;
    height: 100vh;
    width: 100%;
    /* 用于为元素添加一个视觉效果。它可以用于实现模糊、色彩变换、亮度调整等效果。 */
    filter: blur(15px);
}
.header{
    /* 设置元素定位方式 static正常布局； relative 基于正常位置定位；absolute 基于最近的祖先元素定位；fixed 基于浏览器窗口定位；sticky 滚动到特定位置时固定*/
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    /* 内边距 上右下左 四个值； 上下 左右 两个值；上 左右 下 三个值 */
    padding: 25px 13%;
    background-color: transparent;
    /* 元素显示方式 block 新行开始，占用可用宽度；inline 内联元素，同上行开始，依据内容自动调整宽度；inline-block 内联块，上行开始，可设置宽高内外边距；none 元素隐藏，不占空间； flex 显示为flex容器，可使用flex布局；grid 显示为grid容器，可使用grid布局 */
    display: flex;
    /* 设置flex容器中所有flex项目的水平对齐方式 flex-start 起始对齐；flex-end 结束对齐；center 中心对齐；space-between 平均分布，间距相等；space-around 平均分布，间隔相等，容器两端间隔为其它间隔一半 */
    justify-content: space-between;
    /* 设置flex容器垂直对齐方式 flex-start flex-end center baseline容器基线上对齐 stretch 拉伸以填满容器 */
    align-items: center;
    /* 层叠优先级高覆盖低 */
    z-index: 100;
}

.navbar a{
    position: relative;
    font-size: 16px;
    color: #fff;
    margin-right: 30px;
    /* none 取消下划线；underline 下划线；overline 上划线；line-through 删除线；blink 文本闪烁 */
    text-decoration: none;
}

.search-bar{
    width: 250px;
    height: 45px;
    /* transparent 透明色 */
    background-color: transparent;
    border: none;
    border-radius: 6px;
    display: flex;
    align-items: center;
}

.search-bar input{
    width: 100%;
    background-color: transparent;
    border: none;
    /* 轮廓线样式宽度和颜色 */
    outline: none;
    color: #fff;
    font-size: 16px;
    padding-left: 10px;
}
.search-bar button{
    width: 40px;
    height: 100%;
    background: transparent;
    outline: none;
    border: none;
    color: #fff;
    /* 改变鼠标指针的外观 auto 自动选择；default 默认鼠标；pointer 手性鼠标，表示该元素可以点击；text 可编辑；move 可拖动；not-allowed 不可用 */
    cursor: pointer;
}

/* 伪元素是CSS中的一种特殊选择器，用于在元素的某个位置插入额外的内容或样式。它们不是HTML中真正的元素，而是通过CSS来创建的。
    常见的伪元素包括::before和::after，它们可以在元素的前面或后面插入内容，例如图标、文本等。伪元素可以使用content属性来设置插入的内容，也可以使用其他CSS属性来设置样式。伪元素的使用可以增强页面的可读性和美观度，同时也可以减少HTML代码的冗余。 */
.navbar a::after{
    /* normal/none 伪元素不插入任何值；attr(attribute)插入元素的属性值；url(url)插入指定url；string插入字符串 */
    content: "";
    position: absolute;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: #fff;
    bottom: -5px;
    border-radius: 5px;
    /* rotate(angle) 旋转元素的角度；scale（x,y）缩放元素水平和垂直的平移距离；skew(x,y)倾斜元素水平和垂直倾斜的角度；matrix使用矩阵变换对元素变化 */
    transform: translateY(10px);
    /* 元素透明度 */
    opacity: 0;
    /* transition-property 指定要过渡的属性名称；transition-duration 指定过渡的持续时间；transition-timing-function 指定过渡效果的时间函数；transition-delay指定过渡效果的延迟时间 */
    /* ease 先后慢中间快；ease-out 先快后慢 */
    transition: .5s ease;
}
.navbar a:hover:after{
    transform: translateY(0);
    opacity: 1;
}

.middle{
    position: absolute;
    left: 50%;
    top: -50%;
    height: auto;
    width: 80%;
    border: 2px solid red;
    transform: translate(-50%,-50%);
    border-radius: 20px;
}
.pic{
    position: absolute;
    width: 60px;
    height: 60px;
    z-index: 111;
}
</style>
