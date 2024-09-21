<template>
<div class="background"></div>
<body>
  <img src="../../assets/img/22.gif" class="pic" ref="pic" alt="pic" style="position: absolute;">
  <header class="header">
      <nav class="navbar">
          <a href="#" @click="home_skip">首页</a>
          <a href="#">图表</a>
          <a href="#" @click="management_skip">管理</a>
          <a href="#" @click="login_skip">退出</a>
      </nav>
      <form action="" class="search-bar">
      </form>
  </header>
  <div class="container2">
    <div class="scrolling">
      <div class="scrolling-list-container">
          <transition name="slide">
            <ul class="scrolling-list" :style="{ transform: `translateY(${offset}px)` }">
              <table>
                <tr v-for="item in barrage" :key="item.id" :class="index % 2 === 0 ? 'even-row' : ''">
                    <td>{{ item.rood_id }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.content }}</td>
                    <!-- 依据内容设置类名 -->
                    <td :class="getClass(item.nature_of_words)">{{ item.nature_of_words }}</td>
                </tr>
              </table>
            </ul>
          </transition>
      </div>
    </div>
    <div class="pie">
      <v-chart class="chart" :option="option" autoresize />
    </div>
    <div class="bar">
      <div id="container3" style="height: 100%"></div>
    </div>
  </div>
  <div class="word_cloud">
    <div id="myEchart" class="myEchart"></div>
  </div>
  <div class="song">
    <h1 style="color: #fff; font-size: 20px;">歌曲播放</h1>
    <audio ref="audio" :src="currentSongUrl"></audio>
    <el-button type="primary"  @click="play();toggleButton()" v-if="showButton">
      <el-icon> <CaretRight /></el-icon>
    </el-button>
    <el-button type="primary" @click="pause();toggleButton()" v-else>
      <el-icon><VideoPause /></el-icon>
    </el-button>
    <input type="range" min="0" max="100" v-model="volume" @input="setVolume">
  </div>
  <div id="clock">
    {{ hour }}:{{ minute }}:{{ second }}
  </div>
  <div class="foot">
    <div id="chart-container"></div>
      <!-- <p><i class='bx bx-copyright'></i>版权所有 Love</p> -->
  </div>
</body>
</template>

<script>
// 饼图
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart,BarChart } from 'echarts/charts';
import {
  GridComponent,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from 'echarts/components';
import VChart, { THEME_KEY } from 'vue-echarts';
import { ref } from 'vue';
use([
  GridComponent,
  BarChart,
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

import { getCurrentInstance, onMounted } from 'vue';

import * as echarts from 'echarts';
import 'echarts-wordcloud';

import Axios from 'axios';

export default {
  name:'Chart',
  components: {
    VChart,
  },
  provide: {
    [THEME_KEY]: 'dark',
  },
  setup() {
    // 获取其它组件值
    const dint = getCurrentInstance();
    let counter;
    onMounted(() => {
      setInterval(() => {
        counter = dint.data.counter
      },5000);
    });
    // 饼图
    const option = ref({
      title: {
        text: '情感饼图',
        left: 'center',
      },
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)',
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: ['正面', '中性', '字数不足', '负面'],
      },
      series: [
        {
          name: '分布占比',
          type: 'pie',
          radius: '55%',
          center: ['50%', '60%'],
          data: [
            { value: 2, name: '正面' },
            { value: 2, name: '中性' },
            { value: 2, name: '字数不足' },
            { value: 2, name: '负面' },
          ],
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)',
            },
          },
        },
      ],
    });
    // 定时更新数据
    setInterval(() => {
      option.value.series[0].data[0].value = counter.正面;
      option.value.series[0].data[1].value = counter.中性;
      option.value.series[0].data[2].value = counter.字数不足;
      option.value.series[0].data[3].value = counter.负面;
      // console.log(option.value.series[0].data)
    }, 5000); // 每隔5秒更新一次数据

    return { option };
  },
  data() {
      return {
          barrage: [],

          // 滚动列表变量设置
          offset: 0, // 滚动偏移量
          barrageHeight: 13, // 列表项高度
          scrollSpeed: 50, // 滚动速度，值越小滚动越快

          counter: {'正面':2,'负面':2,'中性':2,'字数不足':2},

          word:[{name: '+1',value: 10},{name: "haha",value: 5},{name: "^-^",value: 6}],

          currentSongUrl: '/music/纸短情长.mp3', // 歌曲的URL
          volume: 50, // 音量，默认为50
          showButton: true,

          hour: 0,
          minute: 0,
          second: 0
      }
  },
  created(){
      this.start();
      this.refreshList();
      this.startAutoRefreshList();
  },
  methods: {
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

    home_skip(){
        this.$router.push('/home')
    },

    login_skip(){
        this.$router.push('/login2')
    },
    
    management_skip(){
        this.$router.push('/management')
    },
    // 删除数据库
    deleteList(){
        var url = "http://localhost:8000/api/delete-list";
        // 发送 Axios 请求执行删除操作
        Axios.delete(url).then(response => {
        if (response.data.success) {
            console.log('数据库列表数据已删除');
            // 这里可以根据需要显示删除成功消息
        } else {
            console.error('删除数据库列表数据失败');
            // 这里可以根据需要显示删除失败消息
        }}).catch(error => {
            console.error('请求失败:', error);
            // 这里可以根据需要显示错误消息
        });
    },

    // 刷新列表的方法
    refreshList() {
        var url = "http://localhost:8000/api/barrage/";
        // 发送 Axios 请求获取最新数据
        Axios.get(url).then(response => {
            // 将获取到的最新数据和现有列表数据合并，并进行去重处理
            const newData = response.data.filter(newItem => !this.barrage.some(oldItem => oldItem.id === newItem.id));
            // 将去重后的最新数据和现有列表数据合并
            // this.barrage = newData.concat(this.barrage);//将数据压入列表头
            this.barrage.push(...newData)//将数据压入列尾
            // console.log('获取成功')
        }).catch(error => {
            // 这里可以根据需要显示错误消息
            console.error('请求失败:', error);
        });
        // 此处可根据需要重新获取数据或更新数据源
        // 这里只是简单地将列表中的第一个项移到末尾，模拟列表的变化
        // const firstItem = this.barrage.shift();
        // this.barrage.push(firstItem);
    },

    // 自动刷新列表
    startAutoRefreshList(){
        // 首先立即执行一次刷新列表的操作
        this.refreshList();
        console.log("正在刷新列表...")
        // 然后每隔一段时间（例如5秒）自动执行一次刷新列表的操作
        this.refreshInterval = setInterval(() => {
            this.refreshList();
        }, 5000); // 设置刷新时间间隔（单位：毫秒）
        // 延时一秒统计正负后自动刷新
        setTimeout(() => {
          setInterval(() => {
            this.updateCounter();
          },5000)
        },3000);
    },

    // 终止自动刷新列表
    stopAutoRefreshList() {
        // 停止自动更新的逻辑
        clearInterval(this.refreshInterval); // 清除定时器
        console.log("停止成功")
    },

    // 自动滚动
    startScrolling() {
      this.timer = setInterval(() => {
        this.offset -= 1; // 每次滚动偏移一个像素
        if (Math.abs(this.offset) >= this.barrage.length * this.barrageHeight) {
          this.offset = 0; // 如果滚动超过列表长度，重新开始滚动
        }
      }, this.scrollSpeed);
    },

    // 统计正负
    updateCounter() {
      this.counter.中性 = 0;
      this.counter.字数不足 = 0;
      this.counter.正面 = 0;
      this.counter.负面 = 0;
      // console.log('正在分析...')
      // 遍历列表并统计出现次数
      this.barrage.forEach(item => {
      // 获取对象的指定字段的值
      let fieldValue = item.nature_of_words;
      // 如果该字段值已经在counter对象中存在，则将其计数加一，否则初始化为1
      if (this.counter[fieldValue]) {
          this.counter[fieldValue] += 1;
      } else {
          this.counter[fieldValue] = 1;
      }
      });
      // console.log(this.counter)
    },

    // 词云
    word_cloud() {
      const echartDom = document.getElementById('myEchart')
      const myChart = echarts.init(echartDom)
      const option  = {
          series: [{
          type: 'wordCloud',
          shape: 'square',
          keepAspect: false,
          // maskImage: maskImage,
          left: 'center',
          top: 'center',
          width: '100%',
          height: '100%',
          right: null,
          bottom: null,
          sizeRange: [12, 60],
          rotationRange: [-90, 90],
          rotationStep: 45,
          gridSize: 18,
          drawOutOfBound: false,
          layoutAnimation: true,
          textStyle: {
              fontFamily: 'sans-serif',
              fontWeight: 'bold',
              color: function () {
                  return 'rgb(' + [
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160)
                  ].join(',') + ')';
              }
          },
          emphasis: {
              // focus: 'self',
              textStyle: {
                  textShadowBlur: 3,
                  textShadowColor: '#333'
              }
          },
          //data属性中的value值却大，权重就却大，展示字体就却大
          data: this.word
      }]

      }
      option && myChart.setOption(option)

      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
          myChart.resize();
      });
    },
    word_cloud_api(){
      var url = "http://127.0.0.1:8000/api/test/"
      Axios.get(url).then(response => {this.word = response.data})
    },
    autoRefresh(){
      setInterval(() => {
        this.word_cloud_api();
        this.word_cloud();
        console.log('success')
      },7000)
    },

    // 音乐
    play() {
      this.$refs.audio.play(); // 播放歌曲
    },
    pause() {
      this.$refs.audio.pause(); // 暂停歌曲
    },
    setVolume() {
      this.$refs.audio.volume = this.volume / 100; // 设置音量
    }
  },
  mounted(){

    this.interval = setInterval(() => {
      const date = new Date();
      this.hour = date.getHours();
      this.minute = date.getMinutes();
      this.second = date.getSeconds();
    }, 1000);

    this.word_cloud();
    this.autoRefresh();
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

    // 滚动列表
    // this.startScrolling();
    
    const data = [1,1,1,1,4];
    const doesSomething = () => {
      // console.log(this.counter.正面) // Ok
      data[0] = this.counter.正面
      data[1] = this.counter.负面
      data[2] = this.counter.中性
      data[3] = this.counter.字数不足
      data[4] = data[0] + data[1] + data[2] + data[3];
    }
    setInterval(() => {
      doesSomething();
    },5000);

    var dom = document.getElementById('container3','chart-container');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    
    var option;

    option = {
      graphic: {
        elements: [
          {
            type: 'group',
            left: '85%',
            top: '85%',
            children: new Array(5).fill(0).map((val, i) => ({
              type: 'rect',
              x: i * 20,
              shape: {
                x: 0,
                y: -20,
                width: 6,
                height: 30
              },
              style: {
                fill: '#5470c6'
              },
              keyframeAnimation: {
                duration: 1000,
                delay: i * 200,
                loop: true,
                keyframes: [
                  {
                    percent: 0.5,
                    scaleY: 0.3,
                    easing: 'cubicIn'
                  },
                  {
                    percent: 1,
                    scaleY: 1,
                    easing: 'cubicOut'
                  }
                ]
              }
            }))
          }
        ]
      },
      xAxis: {
        max: 'dataMax'
      },
      yAxis: {
        type: 'category',
        data: ['正面', '中性', '负面','字数不足','总数'],
        inverse: true,
        animationDuration: 300,
        animationDurationUpdate: 300,
        max: 4 // only the largest 3 bars will be displayed
      },
      series: [
        {
          realtimeSort: true,
          // name: '列表',
          type: 'bar',
          data: data,
          label: {
            show: true,
            position: 'right',
            valueAnimation: true
          }
        }
      ],
      legend: {
        show: true
      },
      animationDuration: 0,
      animationDurationUpdate: 3000,
      animationEasing: 'linear',
      animationEasingUpdate: 'linear'
    };
    function run() {

      myChart.setOption({
        series: [
          {
            type: 'bar',
            data
          }
        ]
      });
    }
    setTimeout(function () {
      run();
    }, 0);
    setInterval(function () {
      run();
    }, 3000);

    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);

  },
  beforeDestroy() {
    clearInterval(this.interval);
  }
}
</script>




<style scoped>

#clock {
  color: #fff;
  font-size: 36px;
  position: fixed;
  top: 22%;
  right: -7%;
  width: 25%;
  height: 35%;
  z-index: 100;
}

/*音乐*/
.song{
  background-color: rgb(0, 0, 0,0.3);
  position: fixed;
  top: 10%;
  left: 26px;
  width: 24.9%;
  height: 37.5%;
  z-index: 100;
}

.song button{
  position: fixed;
  background-color: rgb(59, 89, 205,0.6);
  font-size: 64px;
  cursor: pointer;
  border: none;
  color: #fff;
  transition: color 0.3s; /* 添加过渡效果 */
  border-radius: 50%;
  width: 100px;
  height: 100px;
  opacity: 0.8;
  top:20%;
  left: 11%;
}

.song input{
  position: fixed;
  top:35%;
  left: 10%;
}

.song h1{
  margin: 20px;
  text-align: center;
}

/*词云*/
.word_cloud{
  background-color: rgb(0, 0, 0,0.3);
  position: fixed;
  bottom: 30px;
  right: 20px;
  width: 23%;
  height: 49%;
}
.myEchart{
  height: 100%;
  width: 100%;
}

/*加载样式*/
.chart-container {
  height: 100px;
  overflow: hidden;
}

/*柱状图*/
.bar{
  position: fixed;
  top: 65px; /* 与顶部的间距 */
  left: 28%; /* 与左侧的间距 */
  width: 46.8%; /* div的宽度 */
  height: 39%; /* div的高度 */
  background-color: rgb(0, 0, 0,0.3);
}
.container3{
  height: 100%;
}


/*饼图*/
.chart {
  position: fixed;
  bottom: 20px; /* 与底部的间距 */
  left: 20px; /* 与左侧的间距 */
  width: 25%; /* div的宽度 */
  height: 50%; /* div的高度 */
  background-color: rgb(0, 0, 0,0.3);;
}


/*滚动列表*/
.scrolling{
  position: fixed;
  bottom: 20px; /* 与底部的间距 */
  left: 28%; /* 与左侧的间距 */
  width: 46.8%; /* div的宽度 */
  height: 50%; /* div的高度 */
}

.scrolling-list-container {
  color: #fff;
  overflow: hidden;
  height: 100%; /* 列表容器的高度 */
}

.scrolling-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.slide-enter-active, .slide-leave-active {
  transition: transform 0.5s;
}

.slide-enter, .slide-leave-to {
  transform: translateY(0);
}


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
