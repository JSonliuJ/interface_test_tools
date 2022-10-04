#导入对应的库
#1- 应用对象
from PySide2.QtWidgets import QApplication
#2- 界面ui 文件需要导入代码里去
from PySide2.QtUiTools import QUiLoader
#3- 导入读取ui文件的库
from PySide2.QtCore import QFile

#4- 需要一个应用程序对象
app = QApplication([])#sys.argv
#5- 获取ui 文件
qFile = QFile('login.ui')
#6- 打开这个ui文件
qFile.open(QFile.ReadOnly)
#7- 加载ui对象
ui = QUiLoader().load(qFile)
#8- 关闭qfile文件
qFile.close()

#-----登录操作------
def login():
    #账号获取--ui页面的对应的对象获取
    userName = ui.user_edit.text()
    password = ui.pwd_edit.text()
    ui.textBrowser.append(f"用户{userName},登录成功！")
    #密码获取
    #显示登录结果

def exit():
    ui.textBrowser.clear()

#动作关联
ui.login_button.clicked.connect(login)
ui.clear_button.clicked.connect(exit)

#9- 显示这个ui
ui.show()
#10- 运行应用对象
app.exec_()