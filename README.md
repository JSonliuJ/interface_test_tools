# interface_test_tools
接口测试工具：类似postman
## 01需求分析

- 需求：实现接口测试工具，带GUI页面样式

- 功能描述
  - 实现接口测试
  - 为特别场景解决特定问题，提交测试团队效率

![1664785237214](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664785237214.png)

- 实现方案：

  - gui编程

  - requests函数封装

## 02GUI编程概述

### 2. 1 图形库接口用户接口

- 软件提供给用户一个图形化界面

- 用户只需要使用鼠标点点点
- 可以得到图形化的反馈
- 完成与软件的交互过程



## 03GUI实现方案

### 3.1 GUI模块

- **Tkinter** : python中最简单的图形化模块，总共只有14种组件
- **Pyqt** : python中最复杂也是使用最广泛的图形化
- **Wx** : 是python居中的一个图形化，学习结构清晰
- **Pywin** :是python windows下的模块，摄像头控制(opencv),常用于外挂制作

### 3.2 PyQt

- PyQt是GPLv3协议，大意是你的程序中用了它，你的程序就要开源，如果闭源商用就会违反协议，(除非你搞封装动态加载那一套来强行规避
- 使用自由软件时违反了GPL的授权。如果是个人或不正规的公司倒也无所谓，但如果是有规模的公司，恐怕会有被起诉的风险

### 3.3 PySide2

- PySide是LGPL协议，如果只是作为库用用它，你的程序还是可以闭源商用。
- 所以很多人喜欢PySide。如果不做商业项目，强烈建议使用PyQt,资料多，稳定。需要开发闭源商用软件的就用PySide

## 04 GUI开发环境搭建

### 4.1 安装PySide2

```
pip install PySide2 -i https://pypi.douban.com/simple --trusted-host pypi.douban.com
```

![1664788448002](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664788448002.png)

### 4.2 进入python目录找到PySide2目录双击designer.exe

![1664789334140](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664789334140.png)

### 4.3 pycharm关联Designer

- File->Settings->Tools->External Tools，打开页面
  - Program 填写：PySide2安装路径下的 designer.exe 
    路径
  - Working directory 填写：项目路径 $FileDir$
- 目的：用于快速设计、修改 ui 并生成 .ui 文件

![1664790010820](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664790010820.png)

### 4.4 安装pyqt5

```
pip install -U pyqt5 -i https://pypi.douban.com/simple --trusted-host pypi.douban.com
```

![1664791214095](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664791214095.png)

### 4.5 pycharm关联pyside2-uic

![1664791529507](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664791529507.png)

## 05 接口工具ui界面设计

### 5.1 Qt Designer使用File->Settings->Tools->External Tools，打开页面。

- 目的:用于快速设计、修改ui并生成.ui文件。
- Program 填写: PySide2安装路径下的designer.exe 路径
- Working directory填写:项目路径`$FileDir$`

### 5.2 工具主界面

- **工具箱区域**:  提供GUI界面开发使用的各种基本控件，如单选框、文本框等。可以拖动到新创建的主程序界面。
- **主界面区域**: 用户放置各种从工具箱拖过来的各种控件。模板选项中最常用的就是Widget(通用窗口)和MainWindow(主窗口)。二者区别主要是Widget窗口不包含菜单栏、工具栏等
- **对象查看器区域**：查看主窗口放置的对象列表
- **属性编辑器区域**： 提供对窗口、控件、布局的属性编
  辑功能。比如修改控件的显示文本、对象名、大小等。
- **信号/槽编辑器区域**：编辑控件的信号和槽函数，也可
  以添加自定义的信号和槽函数。

### 5.3 常用基本控件介绍

#### 1. 输入控件

- **Line Edit**：单行文本框，输入单行字符串。控件对象
  常用函数为Text() 返回文本框内容，用于获取输入。
- **setText()** 用于设置文本框显示。
- **Text Edit**：多行文本框，输入多行字符串。控件 对象
  常用函数同Line Edit控件。
- **Combo Box**：下拉框列表。用于输入指定枚举值。

![1664808466861](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664808466861.png)

#### 2. 按钮控件

- **Push Button**：命令按钮，信号就是指鼠标左键按下然后释放时会发送信号，从而
  触发相应操作

- **Radio Button**：单选框按钮
-  **Check Box**：多选框按钮

![1664808400362](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664808400362.png)

#### 3. 显示控件

- **Lable**：文本标签，显示文本，可以用来标记控件。
- **Text Browser**：显示文本控件。用于后台命令执行结
  果显示。

![1664808486228](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664808486228.png)

### 5.4 基本控件常用方法

#### 1.  QPushButton按钮

- 点击事件：button.clicked.connect(函数)
- 改变按钮文本：button.setText(text)
- 按钮禁用：button.setEnabled(False)
- 按钮启用：button.setEnabled(True)

#### 2. QLineEdit单行文本框

- 文本获取：text = lineEdit.text()
- 设置提示文本：lineEdit.setPlaceholderText('请输入')
- 设置编辑框文本：lineEdit.setText('zhangsan'）

#### 3. QTextBrowser 文本浏览器

- 末尾追加文本：textBrowser().append('hello world')
- 末尾添加文本: textBrowser.insertPlainText('hello world')

#### 4. QComboBox组合选择框

- 设置一个选项：boxMethod.addItem('get')
- 设置多个选项：boxMethod.addItems(['GET','POST','PUT','DELETE'])
- 清空选项：boxMethod.clear()
- 获取当前选中选项文本：method = boxMethod.currentText()

#### 5.  QPlainTextEdit 多行文本框

- 文本编辑事件：edit.textChanged.connect(函数)
- 获取编辑框文本：text = edit.toPlainText()
- 设置提示文本：edit.setPlaceholderText('请在这里输入请求体')

- 设置编辑框文本：edit.setPlainText('''hello world''')
- 编辑框末尾追加文本：edit.appendPlainText('hello world')
- 编辑框末尾添加文本：edit.insertPlainText('内容')
- 清除编辑框文本：edit.clear()
- 复制编辑框文本：edit.copy()
- 粘贴编辑框文本：edit.paste()

### 5.4 小工具源码

```
import requests
import json
from requests import exceptions
import threading
# 导入对应的库
# 1.应用对象
from PySide2.QtWidgets import QApplication
# 1.2界面ui 文件需要导入代码里去
from PySide2.QtUiTools import QUiLoader
# 1.3导入读取ui文件的库
from PySide2.QtCore import QFile


class HttpClient():
    def __init__(self, ui_name='接口工具.ui'):
        # 1.4获取ui文件
        self.q_file = QFile(ui_name)
        # 1.5 打开ui文件
        self.q_file.open(QFile.ReadOnly)
        # 1.6 加载ui对象
        self.ui = QUiLoader().load(self.q_file)

        # 1.7 动作关联
        self.ui.send_button.clicked.connect(self.send_request)
        self.ui.clearButton.clicked.connect(self.clear_action)

    def clear_action(self):
        self.ui.textBrowser.clear()

    # 2. 发送请求后端逻辑
    def send_request(self):
        # 2.1 获取请求方法
        global res
        method = self.ui.comboBox.currentText()
        # 2.2 获取url
        url = self.ui.urlEdit.text()
        # 2.3 获取请求头
        header = self.ui.headTextEdit.toPlainText()
        if header.strip() != "":
            try:
                # 2.4将字符串转字典
                header = json.loads(header)
            except:
                self.ui.textBrowser.append('请求头参数格式错误！')
                header = None
        else:
            header = None
        # 2.5 获取请求体
        body = self.ui.bodyTextEdit.toPlainText()
        if body.strip() != "":
            try:
                # 2.6将字符串转字典
                body = json.loads(body)
            except:
                self.ui.textBrowser.append('请求体参数格式错误！')
                body = None
        else:
            body = None
        print(method, url, header, body)
        if header:
            try:
                res = requests.Request(method, url, headers=header, data=body)
            except exceptions as e:
                print(e)
                self.ui.textBrowser.append(e)
        else:
            try:
                res = requests.Request(method, url, data=body)
            except exceptions as e:
                self.ui.textBrowser.append(e)
        # 2.7获取请求数据
        prepare = res.prepare()
        # 2.8创建会话
        s = requests.Session()

        # 2.9 启动线程
        t1 = threading.Thread(target=self.thread_send, args=(s, prepare))
        t1.start()

    # 3.线程发送请求
    def thread_send(self, s, prepare):
        resp = s.send(prepare)
        self.show_respone(resp)

    # 4. 响应数据处理返回
    def show_respone(self, resp):
        resp.encoding = 'utf-8'
        self.ui.textBrowser.append(
            "HTTP/1.1 {} \n{} \n\n{}".format(
                resp.status_code,  # 4.1状态码
                '\n'.join('{}:{}'.format(k, v) for k, v in resp.headers.items()),  # 4.2响应头
                resp.text  # 4.3响应体
            )
        )


# 5.1创建应用程序对象
app = QApplication([])  # sys.argv
httpClient = HttpClient()
# 5.2显示ui
httpClient.ui.show()
# 5.3运行应用对象
app.exec_()
# url:http://WebXml.com.cn/WebServices/WeatherWS.asmx/getRegionCountry method:post,data:{"a": "b"},header:{"Content-Type": "application/x-www-form-urlencoded"}
```

#### 5.5 ui界面

![1664857972611](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664857972611.png)

## 06 windoiws平台打包可执行文件

### 6.1 安装pyinstaller库

```
pip install pyinstaller  -i https://pypi.douban.com/simple --trusted-host pypi.douban.com
```

![1664867710826](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664867710826.png)

### 6.2 找到python工程下输入cmd

```
1. cmd
2. 打包方式1(exe)：pyinstaller py文件名 --noconsole --hidden-import PySide2.QtXml # 方式1
2.打包方式2(exe+依赖)：pyinstaller -F httpclient.py --noconsole --hidden-import PySide2.QtXml
```

![1664865418360](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664865418360.png)

![1664865761627](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664865761627.png)

![1664865786881](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1664865786881.png)

