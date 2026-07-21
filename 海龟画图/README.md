# Python Turtle 海龟画图练习

本项目用于存放 Python `turtle` 海龟画图练习题。

练习内容按照难度由浅入深排列，涵盖：

- 海龟的移动与转向
- 循环绘图
- 颜色与图形填充
- 函数封装
- 坐标定位
- 随机数应用
- 键盘事件监听
- 简单动画与小游戏

---

## 一、项目目录

```text
turtle_exercises/
├── README.md
├── 01_square.py
├── 02_triangle.py
├── 03_pentagon.py
├── 04_filled_circle.py
├── 05_colored_rectangles.py
├── 06_concentric_circles.py
├── 07_rotating_squares.py
├── 08_color_spiral.py
├── 09_polygon_function.py
├── 10_five_pointed_star.py
├── 11_traffic_light.py
├── 12_simple_house.py
├── 13_clock_face.py
├── 14_random_dots.py
├── 15_keyboard_control.py
└── 16_simple_snake.py
```

其中：

- `turtle_exercises`：项目总文件夹；
- `README.md`：项目说明文档；
- `.py` 文件：每一道海龟画图练习题对应的 Python 程序。

---

## 二、文件说明

| 文件名 | 中文题目 | 主要练习内容 |
|---|---|---|
| `01_square.py` | 绘制正方形 | `forward()`、`left()`、`for` 循环 |
| `02_triangle.py` | 绘制等边三角形 | 正多边形外角、循环绘图 |
| `03_pentagon.py` | 绘制正五边形 | 正多边形转角公式 |
| `04_filled_circle.py` | 绘制填充圆形 | 轮廓颜色、填充颜色、画笔粗细 |
| `05_colored_rectangles.py` | 绘制双色矩形 | 函数封装、抬笔和落笔、位置移动 |
| `06_concentric_circles.py` | 绘制同心圆 | 坐标调整、循环绘制多个圆 |
| `07_rotating_squares.py` | 绘制旋转正方形 | 嵌套循环、旋转图案 |
| `08_color_spiral.py` | 绘制彩色螺旋线 | 递增长度、颜色列表、取余运算 |
| `09_polygon_function.py` | 通用正多边形函数 | 函数参数、通用绘图代码 |
| `10_five_pointed_star.py` | 绘制五角星 | 特殊转角、循环、图形填充 |
| `11_traffic_light.py` | 绘制简易红绿灯 | 坐标定位、矩形和圆形组合 |
| `12_simple_house.py` | 绘制简易房子 | 多函数组合、综合图形设计 |
| `13_clock_face.py` | 绘制钟表表盘 | 三角函数、圆周坐标、文字输出 |
| `14_random_dots.py` | 随机彩色圆点画 | `random` 库、随机坐标和颜色 |
| `15_keyboard_control.py` | 键盘控制海龟 | 键盘事件监听、函数绑定 |
| `16_simple_snake.py` | 简易贪吃蛇 | 列表、对象、定时刷新、简单动画 |

---

## 三、文件命名规则

本项目采用以下命名格式：

```text
题号_英文功能名.py
```

例如：

```text
01_square.py
08_color_spiral.py
15_keyboard_control.py
```

### 1. 在文件名前添加题号

题号使用两位数字：

```text
01
02
03
...
16
```

这样操作系统按照文件名排序时，练习题会保持正确顺序。

如果直接写成：

```text
1_square.py
2_triangle.py
10_star.py
```

部分系统可能会按照字符顺序排列成：

```text
10_star.py
1_square.py
2_triangle.py
```

因此建议统一使用两位题号。

### 2. 使用小写英文字母

推荐：

```text
simple_house.py
traffic_light.py
```

不推荐：

```text
SimpleHouse.py
TrafficLight.py
```

全部使用小写字母，可以让项目的命名风格更加统一。

### 3. 单词之间使用下划线

推荐：

```text
five_pointed_star.py
keyboard_control.py
```

不推荐：

```text
fivepointedstar.py
keyboard-control.py
keyboard control.py
```

Python 文件名中不建议包含空格或连字符。

### 4. 不要使用中文文件名

虽然部分 Python 环境支持中文文件名，但为了避免路径、编码和跨平台兼容问题，建议使用英文文件名。

不推荐：

```text
第一题正方形.py
海龟画图.py
```

### 5. 不要与标准库同名

尤其不要把程序命名为：

```text
turtle.py
random.py
math.py
time.py
```

这些名称与 Python 标准库模块同名，可能导致导入错误。

例如，当前目录存在一个名为 `turtle.py` 的文件时：

```python
import turtle
```

Python 可能会导入当前目录中的 `turtle.py`，而不是标准库中的 `turtle` 模块。

---

## 四、运行环境

本项目使用 Python 标准库中的 `turtle` 模块，不需要额外安装第三方库。

建议使用：

- Python 3.10 或更高版本
- IDLE
- PyCharm
- Visual Studio Code

检查 Python 是否安装成功：

```bash
python --version
```

某些 Windows 环境需要使用：

```bash
py --version
```

---

## 五、运行程序

### 方法一：使用 IDLE

1. 使用 IDLE 打开对应的 `.py` 文件；
2. 点击菜单栏中的 `Run`；
3. 选择 `Run Module`；
4. 也可以直接按 `F5` 运行。

### 方法二：使用命令行

先进入项目目录：

```bash
cd turtle_exercises
```

然后运行某一道题：

```bash
python 01_square.py
```

在部分 Windows 环境中也可以使用：

```bash
py 01_square.py
```

### 方法三：使用 VS Code

1. 使用 VS Code 打开 `turtle_exercises` 文件夹；
2. 打开需要运行的 `.py` 文件；
3. 点击右上角的运行按钮；
4. 海龟画图窗口会自动打开。

---

## 六、推荐练习顺序

建议按照以下顺序完成：

```text
01 → 02 → 03 → 04 → 05
→ 06 → 07 → 08 → 09 → 10
→ 11 → 12 → 14 → 15 → 13 → 16
```

各阶段的学习目标如下：

### 第一阶段：基础绘图

对应文件：

```text
01_square.py
02_triangle.py
03_pentagon.py
04_filled_circle.py
05_colored_rectangles.py
```

主要掌握：

- 海龟前进和转向
- 循环绘图
- 画笔颜色
- 图形填充
- 抬笔和落笔

### 第二阶段：循环与函数

对应文件：

```text
06_concentric_circles.py
07_rotating_squares.py
08_color_spiral.py
09_polygon_function.py
10_five_pointed_star.py
```

主要掌握：

- 嵌套循环
- 列表与取余运算
- 函数定义
- 函数参数
- 重复图案绘制

### 第三阶段：坐标与综合图形

对应文件：

```text
11_traffic_light.py
12_simple_house.py
13_clock_face.py
14_random_dots.py
```

主要掌握：

- 坐标定位
- 多种图形组合
- 随机数
- 三角函数
- 文字输出

### 第四阶段：事件与动画

对应文件：

```text
15_keyboard_control.py
16_simple_snake.py
```

主要掌握：

- 键盘事件监听
- 函数绑定
- 屏幕刷新
- 定时任务
- 简单游戏逻辑

---

## 七、基础代码结构

每个练习文件可以使用下面的基本结构：

```python
import turtle


def main():
    pen = turtle.Turtle()
    pen.speed(0)

    # 在这里编写绘图代码

    pen.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
```

其中：

- `import turtle`：导入海龟画图库；
- `turtle.Turtle()`：创建一只海龟；
- `speed(0)`：将绘图速度设置为最快；
- `hideturtle()`：绘制完成后隐藏海龟图标；
- `turtle.done()`：让绘图窗口保持打开；
- `main()`：将主要程序封装到函数中；
- `if __name__ == "__main__":`：保证当前文件被直接运行时才执行主程序。

---

## 八、常见问题

### 1. 为什么窗口一闪而过？

通常是因为程序最后没有写：

```python
turtle.done()
```

也可以使用：

```python
turtle.mainloop()
```

二者通常选择一个即可。

### 2. 为什么海龟移动时出现多余线条？

移动到新位置之前先抬笔：

```python
pen.penup()
pen.goto(x, y)
pen.pendown()
```

### 3. 为什么 `import turtle` 报错？

检查当前项目中是否存在以下文件：

```text
turtle.py
turtle.pyc
```

如果存在，请重命名或删除，并删除可能生成的 `__pycache__` 文件夹。

### 4. 为什么图形方向不正确？

需要区分图形的内角和海龟每次转动的外角。

正 `n` 边形的外角为：

```text
360 ÷ n
```

例如正五边形每次应转动：

```text
360 ÷ 5 = 72°
```

### 5. 为什么中文显示乱码？

`turtle.write()` 显示中文时，可以手动指定支持中文的字体：

```python
pen.write(
    "海龟画图",
    align="center",
    font=("Microsoft YaHei", 16, "normal")
)
```

不同操作系统中的字体名称可能不同。

---

## 九、学习要求

完成每一道题时，建议遵守以下要求：

1. 先独立分析需要使用哪些命令；
2. 能使用循环时，不重复编写相同代码；
3. 重复使用的绘图过程尽量封装为函数；
4. 移动位置时注意抬笔和落笔；
5. 为关键代码添加简洁注释；
6. 完成后尝试修改边长、颜色、数量或坐标；
7. 不要只复制答案，要理解海龟每一步的运动过程。

---

## 十、项目目标

完成全部练习后，应能够：

- 熟练使用 `turtle` 的常用绘图命令；
- 使用循环绘制规则图形和重复图案；
- 使用函数封装绘图功能；
- 使用坐标控制图形位置；
- 使用随机数生成随机图案；
- 使用键盘控制海龟；
- 理解简单动画和小游戏的基本实现方式。
