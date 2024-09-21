<template>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <div class="background"></div>
    <body>
        <img src="../../assets/img/22.gif" class="pic" ref="pic" alt="pic" style="position: absolute;">
        <header class="header">
            <nav class="navbar">
                <a href="#">首页</a>
                <a href="#" @click="chart_skip">图表</a>
                <a href="#" @click="management_skip">管理</a>
                <a href="#"  @click="login_skip">退出</a>
            </nav>
            <form action="" class="search-bar">
                <input type="text" placeholder="搜索...">
                <button><i class='bx bx-search'></i></button>
            </form>
        </header>
        <div class="container2">
            <div class="item1">
               <h1>弹幕情感分析</h1>
            </div>
            <div class="item2">
                <input type="text" v-model="room_id" placeholder="请输入房间号...">
                <button class="btn1" @click="startAutoRefreshList();toggleButton();execteProgram()" v-if="showButton">开始分析</button>
                <button class="btn1" @click="stopAutoRefreshList();toggleButton()" v-else>停止分析</button>
            </div>
            <hr class="separator"></hr>
            <div class="item3">
                <div class="item4">
                    <!-- 表格 -->
                    <table>
                        <!-- 表头 -->
                        <thead>
                        <tr>
                            <th>房间号</th>
                            <th>用户姓名</th>
                            <th>弹幕内容</th>
                            <th>弹幕性质</th>
                        </tr>
                        </thead>
                        <!-- 表格内容 -->
                        <tbody>
                        <!-- 使用 v-for 循环遍历数据，并根据奇偶行为行添加不同的类名 -->
                        <tr v-for="item in barrage" :key="item.id" :class="index % 2 === 0 ? 'even-row' : ''">
                            <td>{{ item.rood_id }}</td>
                            <td>{{ item.name }}</td>
                            <td>{{ item.content }}</td>
                            <!-- 依据内容设置类名 -->
                            <td :class="getClass(item.nature_of_words)">{{ item.nature_of_words }}</td>
                        </tr>
                        </tbody>
                    </table>
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
export default{
    name:'home',
    data() {
        return {
            room_id: '',
            barrage: [],
            showButton: true,//控制按钮显示状态的变量
        }
    },
    created(){
        this.start();
    },
  methods: {
    execteProgram(){
        Axios.defaults.xsrfCookieName = 'csrftoken';
        Axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        let room_id = this.room_id;
        let roomData = {
            rood_id: room_id
        };
        var url = "http://127.0.0.1:8000/api/room_add/" + room_id + "/";
        Axios.get(url).then(response => {console.log(response.data);})
    },
    toggleButton(){
        this.showButton = !this.showButton;//切换按钮显示状态
    },
    start(){
        var url = "http://127.0.0.1:8000/api/admin/";
        Axios.get(url).then(response => {this.admin = response.data;})
        console.log("链接成功")
    },
    getClass(nature_of_words) {
        if (nature_of_words === "负面") {
            return 'red';
        } else if (nature_of_words === "正面") {
            return 'sky';
        } else if (nature_of_words === "字数不足"){
            return 'gray'; 
        } else {
            return '';// 正常显示
        }
    },
    chart_skip(){
        this.$router.push('/chart')
    },
    login_skip(){
        this.$router.push('/')
    },
    management_skip(){
        this.$router.push('/management')
    },
    // 刷新列表的方法
    refreshList() {
        var url = "http://localhost:8000/api/barrage/";
        // 发送 Axios 请求获取最新数据
        Axios.get(url).then(response => {
            // 将获取到的最新数据和现有列表数据合并，并进行去重处理
            const newData = response.data.filter(newItem => !this.barrage.some(oldItem => oldItem.id === newItem.id));
            // 将去重后的最新数据和现有列表数据合并
            this.barrage = newData.concat(this.barrage);
        }).catch(error => {
            // 这里可以根据需要显示错误消息
            console.error('请求失败:', error);
        });
        // 此处可根据需要重新获取数据或更新数据源
        // 这里只是简单地将列表中的第一个项移到末尾，模拟列表的变化
        // const firstItem = this.barrage.shift();
        // this.barrage.push(firstItem);
    },

    startAutoRefreshList(){
        // 首先立即执行一次刷新列表的操作
        this.refreshList();
        // 然后每隔一段时间（例如5秒）自动执行一次刷新列表的操作
        this.refreshInterval = setInterval(() => {
            this.refreshList();
        }, 5000); // 设置刷新时间间隔（单位：毫秒）
        // 执行消息
        ElMessage({
            message: '正在分析...',
            type: 'success',
        })

    },

    // 终止自动刷新列表
    stopAutoRefreshList() {
        // 停止自动更新的逻辑
        clearInterval(this.refreshInterval); // 清除定时器
        ElMessage({
            message: '已停止分析.',
            type: 'success',
        })
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


/* 正面负面颜色 */
.red{
    color: red;
    font-weight: bold;
}
.sky{
    font-weight: bold;
    color: rgb(164, 199, 212);
}
.gray{
    font-size: bold;
    color: #888;
}
/* 表格样式 */
table {
  width: 100%; /* 表格宽度占满父容器 */
  border-collapse: collapse; /* 合并边框 */
  border-radius: 20px;
  overflow: hidden; /* 隐藏溢出的边角 */
  table-layout: fixed; /* 固定表格布局 */
}
/* 表格行样式 */
tr {
  border-bottom: 1px solid #ccc; /* 设置行底部边框 */
}
/* 表格单元格样式 */
td {
  padding: 10px; /* 单元格内边距 */
  overflow: hidden; /* 设置溢出内容隐藏 */
  white-space: nowrap; /* 防止文本换行 */
  text-overflow: ellipsis; /* 超出部分用省略号表示 */
  text-align: center;
}
/* 偶数行背景色 */
tr:nth-child(even) {
  background-color: rgb(0, 0, 0,0.6); /* 设置偶数行背景色 */
}

/* 奇数行背景色 */
tr:nth-child(odd) {
    background-color: rgb(0, 0, 0,0.3); /* 设置奇数行背景色 */
}

/* 表头样式 */
th {
  background-color: rgb(12, 22, 40); /* 表头背景色 */
  color: white; /* 表头文字颜色 */
  padding: 10px; /* 表头内边距 */
}

.separator{
    border: none; /* 移除默认边框 */
    height: 2px; /* 设置分隔线高度 */
    background-image: linear-gradient(to right, transparent, rgb(59, 89, 205), transparent); /* 设置分隔线背景为水平渐变，两边透明 */
    background-position: 20%;
    margin: 20px 0; /* 设置上下边距 */
}
.item3{
    overflow-y: auto;
    margin: 20px;
    padding: 20px;
    border-radius: 20px;
    height: 72%;
}
.item2{
    padding-left: 16%;
    height: 50px;
    margin: 20px;
    border-radius: 20px;
    padding-top: 5px
}
.item2 input{
    font-size: 16px;
    color: #fff;
    background: transparent;
    width: 80%;
    height: 35px;
    border: none;
    outline: none;
}
.item2 input::placeholder{
    color: #fff;
    opacity: 0.8;
}
.btn1{
    background-color: rgb(59, 89, 205,0.6);
    font-size: 16px;
    cursor: pointer;
    border: none;
    color: #fff;
    transition: color 0.3s; /* 添加过渡效果 */
    border-radius: 20px;
    width: 100px;
    height: 35px;
    opacity: 0.8;
}
/* 鼠标悬停时按钮的样式 */
.btn1:hover {
    color: rgba(164, 199, 212);
}

/* 按钮点击时的样式 */
.btn1:active {
    transform: translateY(2px); /* 按钮按下时向下移动 2 像素 */
    box-shadow: 0 0 5px rgba(12, 25, 78, 0.5); /* 添加阴影效果 */
}
.item1 h1{
    padding-top: 20px;
    margin: 20px;
    text-align: center;
    font-size: 28px;
}
.container2{
    color: #fff;
    position: absolute;
    left: 50%;
    top: -52%;
    transform: translate(-50%,-50%);
    width: 85%;
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

.search-bar{
    width: 250px;
    height: 45px;
    /* transparent 透明色 */
    background-color: transparent;
    border: 2px solid #fff;
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

/* 常见的伪类选择器包括： 
:hover：鼠标悬停在元素上时应用的样式。
:active：元素被激活时应用的样式，例如当用户点击一个链接时。
:focus：元素获得焦点时应用的样式，例如当用户在表单元素中输入文本时。
:visited：已访问链接的样式。
:nth-child()：选择指定父元素下的第n个子元素。
:first-child：选择指定父元素下的第一个子元素。
:last-child：选择指定父元素下的最后一个子元素。
:not()：选择不符合指定选择器的元素。
:checked：选择被选中的表单元素，例如复选框或单选按钮。*/
/*input::placeholder 占位符文本； */
.search-bar input::placeholder{
    color: #fff;
}

.search-bar button i{
    font-size: 22px;
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
