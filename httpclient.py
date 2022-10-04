# -- encoding: utf-8 --
# @time:    	2021/10/4 10:04
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

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
