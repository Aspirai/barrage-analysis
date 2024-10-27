# 项目简介

这是一个实时获取B站直播弹幕，并动态进行可视化分析的项目；

项目运行如下图展示：
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/1.png)
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/2.png)
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/3.png)
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/4.png)
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/5.png)
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/6.png)
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/7.png)
![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/8.png)

# 快速使用

## 前端启动

1. 进入front_end文件夹下运行`npm install`

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/9.png)

2. 若出现上面提示,运行`npm audit fix --force`修复

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/10.png)

3. 运行`npm run dev`启动前端项目

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/11.png)

4. 浏览器进入`http://localhost:5173/`

   ![image](https://github.com/Aspirai/BarrageAnalysis/blob/master/img/1.png)

## 后端启动

### 数据库配置

1. 安装数据库`MySQL`,[链接](https://blog.csdn.net/m0_71422677/article/details/136007088)

2. 安装数据库管理`Navicat Premium 16`,[链接](https://www.cnblogs.com/kkdaj/p/16260681.htm)

3. 打开Navicat ,新建链接,后续不用可以删除

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/12.png)

4. 新建数据库`test`

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/13.png)

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/14.png)

5. 引入表结构(在上面)

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/15.png)

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/16.png)

   ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/17.png)

   ## 启动!

   1. 进入`back_end`,运行`python manage.py runserver`

      ![image](https://github.com/Aspirai/barrage-analysis/blob/master/img/18.png)

   启动完成

# 文档说明

项目使用Vue3 + Django + MySQL 搭建
