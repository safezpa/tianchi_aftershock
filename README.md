# 初赛（6月13日-7月27日）
## 余震捕捉AI大赛

### 准备工作

这个项目需要安装**Python 2.7**和以下的Python函数库：

- [NumPy](http://www.numpy.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

你还需要安装一个软件，以运行和编辑[ipynb](http://jupyter.org/)文件。



### 编码

代码在`tianchi_aftershock.ipynb`文件中给出。

### 运行

下载源码

```git clone https://github.com/safezpa/tianchi_aftershock.git

在终端或命令行窗口中，选定`tianchi_aftershock/`的目录下（包含此README文件），运行下方的命令：

```jupyter notebook tianchi_aftershock.ipynb```

这样就能够启动jupyter notebook软件，并在你的浏览器中打开文件。

### Data

因为本次大赛数据量较大，所以会采用通过OSS客户端下载的方式进行大赛数据的获取，大赛数据下载方式介绍请点击技术圈链接：https://tianchi.aliyun.com/competition/new_articleDetail.html?from=part&raceId=231606&postsId=1552

|    文件名称     | 文件格式 |
| :------------: | :-----------------: | 
| SAC数据头文件说明.pdf |  pdf    | 
| readsac.py        |    py         | 
| station_latlon.txt        |    txt         |
| 样本数据（非比赛数据）.zip     |    zip         |

**竞赛数据**

本次竞赛的数据源包括汶川地震前（before文件夹）后（after文件夹）的十六座地震台站的地震波监测信号，包括东西（BHE）、南北（BHN）、上下（BHZ）三个方向的地震波。下图中的红圆圈表示余震位置，蓝色三角形表示本次比赛中使用的地震台站。
https://img.alicdn.com/tfs/TB1Gb0JRpXXXXbfXpXXXXXXXXXX-973-752.png
![](https://img.alicdn.com/tfs/TB1Gb0JRpXXXXbfXpXXXXXXXXXX-973-752.png)

纵（P）波会被记录在上下方向（BHZ）里，而横波会记录在东西（BHE）、南北（BHN）里。数据以SAC文件格式储存。例如：
SC.YYU.2008133160001.D.00.BHZ.sac
表示四川省YYU地震台站2008年某日测量得到的上下方向的地震波记录。
推荐选手使用python语言来读取SAC文件中的数据，需要安装obspy库：https://github.com/obspy/obspy/wiki
python+obspy读取SAC数据的函数指南：
https://docs.obspy.org/master/packages/obspy.io.sac.html
下图中是读取出的三轴震动数据。P波速度快，在Z轴（第三张图）先显示出来。S波速度慢后到，在三轴都能检出。
![](https://img.alicdn.com/tfs/TB1SV.3RXXXXXXgapXXXXXXXXXX-511-286.png)

我们同时提供地震台站的经纬度坐标，放在station_latlon.csv文件中。
在初赛、复赛、决赛第一阶段、决赛第二阶段，选手所需要监测的时间段不断增加。本次大赛决赛阶段的总原始数据量将达到约400GB。

**选手提交结果表**

在初赛、复赛的不同阶段，大赛会告知选手需要检出的余震数量（n）。选手提交的评测文件会包括n行3列，字段之间以逗号为分隔符，如下例：
Tianchi_aftershocks_detection_submission.csv

|    列名     | 类型 | 含义 | 示例 |
| :------------: | :-----------------: | :---------------: | :-------------: | 
| station_ID |  string    |    地震台站ID      |    YYU     |
| p_begin_index        |    float         |     P波到达该地震站的起始点     |   134543575       |
| s_begin_index        |    float         |     S波到达该地震站的起始点     |   134545981       |



**评估指标**

选手检测出的结果(n条)，将会和地震局人工检出的记录（m条, m < n）作对比。每一个地震局的真实余震记录，将会被匹配到选手检测出的最临近的结果。
真实余震记录的P波和S波到达该地震站的起始点：Pij和Sij
选手检测到余震的P波和S波到达该地震站的起始点：pij和sij
其中，i是地震台的ID，从1号到16号地震台；j是余震编号，从1到m。
选手排名按照RMSE从小到大排列：
![](https://img.alicdn.com/tfs/TB1RUd6RpXXXXX5aXXXXXXXXXXX-463-122.png)
同时，复赛／决赛过程中，地震局专家将对选手算法的误报警率进行抽查检验。如果算法的误报警率过高，那么即使RMSE很低，也会被降低名次。

**注意事项**
本次比赛不允许使用外部数据，但可以使用开源的已有算法。