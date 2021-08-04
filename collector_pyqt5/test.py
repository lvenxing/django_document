

# class Solution:
#     def merge(self, intervals):
#         flag = True
#         while flag:
#             flag = False
#             for i in range(len(intervals) -1):
#                 if intervals[i][0] > intervals[i+1][0]:
#                     intervals[i], intervals[i+1] = intervals[i+1], intervals[i]
#                     flag = True
#         print(intervals)
#         res = []
#         flag = True
#         for j in range(len(intervals)):
#             if flag:
#                 start = intervals[j][0]
#             end = intervals[j][1]
#             while j > 0:
#                 if intervals[j][0] <= intervals[j-1][1]:
#                     flag = False
#                     end = intervals[j][1]
#                 else:
#                     res.append([start, end])
#                     print("------")
#
#         print(res)
#
#
#         # for k in intervals:
#         #     if k == []:
#
#         # print(intervals)
#
# Solution().merge([[1,3],[2,6],[8,10],[15,18]])

# import sys
# import requests
# import logging
# import telnetlib
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PyQt5 import QtCore, QtGui, QtWidgets
# from urllib.parse import urlparse
#
# fmt = '%(asctime)s -[line:%(lineno)d] - %(levelname)s: %(message)s'
# logging.basicConfig(level=logging.INFO, format=fmt)
#
#
# class MyThread(QtCore.QThread):
#     signal = QtCore.pyqtSignal(list)  # 括号里填写信号传递的参数
#
#     def __init__(self):
#         super().__init__()
#
#     def set_task(self, tasks):
#         self.tasks = tasks
#
#     def __del__(self):
#         # wait 是阻塞
#         # quit 是退出
#         self.wait()
#
#     def run(self):
#         # 进行任务操作
#         """
#         放置任务函数
#         """
#
#         url, method, headers, params = self.tasks
#
#         try:
#             res = requests.request(method=method, url=url, headers=headers, params=params)
#             self.tasks.append(res)
#             self.signal.emit((self.tasks))  # 发射信号
#         except BaseException as e:
#             self.signal.emit(([]))
#
#
# # def check_url(url):
# #     try:
# #         url_data = urlparse(url)
# #         netloc = url_data.netloc
# #         url,port = netloc.split(":")
# #         telnetlib.Telnet(f'{url}',port=f'{port}',timeout=3)
# #     except BaseException as e:
# #         return 0
# #     else:
# #         return 1
#
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("postman")
#         Form.resize(800, 729)
#
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(240, 10, 51, 41))
#         self.label.setObjectName("label")
#
#         # post,get方法
#         self.method = QtWidgets.QComboBox(Form)
#         self.method.setGeometry(QtCore.QRect(40, 60, 111, 31))
#         self.method.setObjectName("method")
#         self.method.addItem("")
#         self.method.addItem("")
#
#         # url地址
#         self.url_lineEdit = QtWidgets.QLineEdit(Form)
#         self.url_lineEdit.setGeometry(QtCore.QRect(220, 60, 221, 31))
#         self.url_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
#         self.url_lineEdit.setCursorPosition(0)
#         self.url_lineEdit.setObjectName("url_lineEdit")
#
#         # send发送
#         self.send_pushButton = QtWidgets.QPushButton(Form)
#         self.send_pushButton.setGeometry(QtCore.QRect(490, 60, 112, 32))
#         self.send_pushButton.setObjectName("send_pushButton")
#
#         self.label_2 = QtWidgets.QLabel(Form)
#         self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 31))
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(Form)
#         self.label_3.setGeometry(QtCore.QRect(290, 110, 141, 41))
#         self.label_3.setObjectName("label_3")
#
#         # 表格
#         self.tableWidget = QtWidgets.QTableWidget(Form)
#         self.tableWidget.setGeometry(QtCore.QRect(20, 180, 201, 192))
#         self.tableWidget.setColumnCount(2)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setRowCount(0)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setHorizontalHeaderItem(1, item)
#
#         # add 增加
#         self.add_pushButton = QtWidgets.QPushButton(Form)
#         self.add_pushButton.setGeometry(QtCore.QRect(80, 110, 41, 32))
#         self.add_pushButton.setObjectName("add_pushButton")
#
#         # 减少
#         self.sub_pushButton = QtWidgets.QPushButton(Form)
#         self.sub_pushButton.setGeometry(QtCore.QRect(130, 110, 41, 32))
#         self.sub_pushButton.setObjectName("sub_pushButton")
#
#         # 消息回显
#         self.textBrowser = QtWidgets.QTextBrowser(Form)
#         self.textBrowser.setGeometry(QtCore.QRect(25, 411, 581, 241))
#         self.textBrowser.setObjectName("textBrowser")
#
#         # 消息体
#         self.textEdit = QtWidgets.QTextEdit(Form)
#         self.textEdit.setGeometry(QtCore.QRect(253, 177, 341, 191))
#         self.textEdit.setObjectName("textEdit")
#
#         # 清除
#         self.clear_pushButton = QtWidgets.QPushButton(Form)
#         self.clear_pushButton.setGeometry(QtCore.QRect(250, 670, 112, 32))
#         self.clear_pushButton.setObjectName("clear_pushButton")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.label.setText(_translate("Form", "postman"))
#         self.method.setItemText(0, _translate("Form", "GET"))
#         self.method.setItemText(1, _translate("Form", "POST"))
#         self.send_pushButton.setText(_translate("Form", "发送"))
#         self.label_2.setText(_translate("Form", "消息头"))
#         self.label_3.setText(_translate("Form", "消息体"))
#         item = self.tableWidget.horizontalHeaderItem(0)
#         item.setText(_translate("Form", "名称"))
#         item = self.tableWidget.horizontalHeaderItem(1)
#         item.setText(_translate("Form", "值"))
#         self.add_pushButton.setText(_translate("Form", "+"))
#         self.sub_pushButton.setText(_translate("Form", "-"))
#         self.clear_pushButton.setText(_translate("Form", "清除"))
#
#
# class Main(QMainWindow, Ui_Form):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#         # 新增表格数据的信号和槽
#         self.add_pushButton.clicked.connect(self.add_table)
#         # 删除表格数据的信号和槽
#         self.sub_pushButton.clicked.connect(self.sub_table)
#         # 清除文本框里面的信号和槽
#         self.clear_pushButton.clicked.connect(self.clear_data)
#         # 多线程 requests 请求的信号和槽
#         self.send_pushButton.clicked.connect(self.send_data)
#
#     def add_table(self):
#         """
#         新增行数据
#         """
#         # 获取当前表格共有多少行
#         rows = self.tableWidget.rowCount()
#         new_row = rows
#         logging.info("新增")
#         self.tableWidget.insertRow(new_row)
#         self.tableWidget.setItem(new_row, 0, QtWidgets.QTableWidgetItem(""))  # 设置j行0列的内容为Value
#         self.tableWidget.setItem(new_row, 1, QtWidgets.QTableWidgetItem(""))  # 设置j行1列的内容为Value
#
#     def sub_table(self):
#         # 删除行数据
#         # 获取当前表格共有多少行
#         rows = self.tableWidget.rowCount()
#         logging.info("移除")
#         if rows == 0:
#             self.message("表格")
#         self.tableWidget.removeRow(rows - 1)
#
#     def message(self, name):
#         # 提示弹窗
#         QMessageBox.information(self, '信息提示对话框', f'{name}！')
#
#     def send_data(self):
#         # 清除数据
#         self.clear_data()
#         # 遍历表格里面的所有数据
#         rows = self.tableWidget.rowCount()
#         headers = {self.tableWidget.item(x, 0).text(): self.tableWidget.item(x, 1).text() for x in range(rows)}
#         method = self.method.currentText()
#         url = self.url_lineEdit.text()
#         params = self.textEdit.toPlainText()
#         self.thread = MyThread()
#         # 回调线程的返回值
#         self.thread.signal.connect(self.callback)
#         self.thread.tasks = [url, method, headers, params]
#         self.thread.start()
#
#     def parse_dict(self, items):
#         for k, v in items.items():
#             self.textBrowser.append(f"{k} {v}")
#
#     def clear_data(self):
#
#         self.textBrowser.clear()
#
#     def callback(self, args):
#         if args:
#             url, method, headers, params, res = args
#             logging.info(f"args->{args}")
#
#             # res = requests.request(method=method, url=url,headers=headers, params=params)
#             send_info = f"""
#     ----------------发送信息------------------
#     {method} {url}
#                 """
#             self.textBrowser.append(send_info)
#             self.parse_dict(headers)
#
#             res_info = f"""
#     ----------------响应信息------------------
#                 """
#             self.textBrowser.append(res_info)
#             self.parse_dict(res.headers)
#             self.textBrowser.append(f"{res.json()}")
#         else:
#             self.message("请求地址异常")
#
#
# if __name__ == "__main__":
#     # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
#     app = QApplication(sys.argv)
#     # 初始化
#     myWin = Main()
#     # 将窗口控件显示在屏幕上
#     myWin.show()
#     # 程序运行，sys.exit方法确保程序完整退出。
#     sys.exit(app.exec_())

# import sys
# import os
# import logging
# from PyQt5 import QtGui, QtWidgets, QtCore
#
# log = logging.getLogger("Foo")
# logging.basicConfig(
#     level=logging.INFO, format='%(levelname)s: %(filename)s - %(message)s')
# log.setLevel(logging.DEBUG)
#
#
# class ConsolePanelHandler(logging.Handler):
#
#     def __init__(self, parent):
#         logging.Handler.__init__(self)
#         self.parent = parent
#
#     def emit(self, record):
#         self.parent.write(self.format(record))
#
#
# class Foo(QtWidgets.QWidget):
#
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#
#         self.textEdit = QtWidgets.QTextEdit(self)
#         self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
#         self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
#
#         vbox = QtWidgets.QVBoxLayout()
#         self.setLayout(vbox)
#         vbox.addWidget(self.textEdit)
#
#     def write(self, s):
#         self.textEdit.setFontWeight(QtGui.QFont.Normal)
#         self.textEdit.append(s)
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     console_panel = Foo()
#     handler = ConsolePanelHandler(console_panel)
#     log.addHandler(handler)
#
#     log.info("Getting logger {0} - {1}".format(id(log), log.handlers))
#     # [log.debug("This is normal text " + str(i)) for i in range(5)]
#     import time
#     for i in range(100):
#         log.debug("This is normal text " + str(i))
#         # time.sleep(0.5)
#     console_panel.show()
#
#     sys.exit(app.exec_())


# 手写的

from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QFormLayout, QLineEdit, QLabel, QRadioButton, \
    QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QListWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QRect, Qt

from PyQt5.QtWidgets import  QMainWindow
from PyQt5 import QtCore, QtGui
import sys, time


from PyQt5 import QtWidgets
from MyUi import Ui_Form

from moni_collect import write_log

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class TestcaseInfo(QMainWindow, Ui_Form):

    def __init__(self):
        super(TestcaseInfo, self).__init__()
        # qfile_testcase_info = QFile(r"C:\Users\Administrator\Desktop\start.ui")
        # qfile_testcase_info.open(QFile.ReadOnly)
        # qfile_testcase_info.close()

        # self.ui = QUiLoader().load(qfile_testcase_info)
        self.setupUi(self)

        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

        self.pushButton.clicked.connect(self.add_table)

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()
        QtWidgets.QApplication.processEvents()

    def add_table(self):
        write_log()
        QtWidgets.QApplication.processEvents()

        for i in range(10):
            print(i)
            time.sleep(0.5)
            QtWidgets.QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testcase_info = TestcaseInfo()
    testcase_info.show()
    sys.exit(app.exec_())