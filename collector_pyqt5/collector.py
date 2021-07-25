
from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QFormLayout, QLineEdit, QLabel, QRadioButton, \
    QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QListWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QRect, Qt


class TestcaseInfo(object):

    def __init__(self):
        qfile_testcase_info = QFile(r"C:\Users\Administrator\Desktop\untitled.ui")
        qfile_testcase_info.open(QFile.ReadOnly)
        qfile_testcase_info.close()

        self.ui = QUiLoader().load(qfile_testcase_info)
        self.ui.plusButton.clicked.connect(self.add_table)
        self.ui.minusButton.clicked.connect(self.sub_table)
        self.ui.okpushButton.clicked.connect(self.confirm_table)
        self.ui.cancelpushButton.clicked.connect(self.cancel_table)
        # # 新增表格数据的信号和槽
        # self.add_pushButton.clicked.connect(self.add_table)
        # # 删除表格数据的信号和槽
        # self.sub_pushButton.clicked.connect(self.sub_table)
        self.init_table()

    def add_table(self, table_key="", table_value=""):
        """
        新增行数据
        """
        # 获取当前表格共有多少行
        rows = self.ui.tableWidget.rowCount()
        new_row = rows
        print("新增")
        self.ui.tableWidget.insertRow(new_row)
        self.ui.tableWidget.setItem(new_row, 0, QTableWidgetItem(table_key))  # 设置j行0列的内容为Value
        self.ui.tableWidget.setItem(new_row, 1, QTableWidgetItem(table_value))  # 设置j行1列的内容为Value

    def sub_table(self):
        # 删除行数据
        # 获取当前表格共有多少行
        rows = self.ui.tableWidget.rowCount()
        print("删除")
        if rows == 0:
            # self.message("表格")
            pass
        self.ui.tableWidget.removeRow(rows - 1)

    def init_table(self):
        self.add_table("performace_data", "123.45")

    def confirm_table(self):
        print("确认按钮被点击了")
        data_dict = {}
        item1 = self.ui.tableWidget.item(0,0).text()
        print(item1)
        print("------------------------")
        rows = self.ui.tableWidget.rowCount()
        # columns = self.ui.tableWidget.columnCount()
        print("该表共有{}行".format(rows))
        # print("该表共有{}列".format(columns))
        for row in range(rows):
            key_content = self.ui.tableWidget.item(row, 0).text()
            value_content = self.ui.tableWidget.item(row, 1).text()
            if key_content:
                data_dict[key_content] = value_content

        print(data_dict)


    def cancel_table(self):
        print("取消按钮被点击了")



class EnvironmentInfo(object):
    def __init__(self):
        qfile_testcase_info = QFile(r"C:\Users\Administrator\Desktop\env_page.ui")
        qfile_testcase_info.open(QFile.ReadOnly)
        qfile_testcase_info.close()

        self.ui = QUiLoader().load(qfile_testcase_info)

        self.ui.addButton.clicked.connect(self.add_device)
        self.ui.delButton.clicked.connect(self.sub_device)

        self.ui.tabWidget.currentChanged.connect(self.tab_change)

        self.ui.nextButton.clicked.connect(self.next_click)

        self.reload_config()

        self.env_list = []

    def reload_config(self):
        bmc_ip = "90.90.67.3"
        bmc_user = "Administrator"
        bmc_pwd = "Admin@9000"
        os_ip = "90.90.26.128"
        os_user = "root"
        os_pwd = "huawei"
        self.add_device(bmc_ip, bmc_user, bmc_pwd, os_ip, os_user, os_pwd)


    def add_device(self, bmc_ip="", bmc_user="", bmc_pwd="", os_ip="", os_user="", os_pwd=""):
        """
        新增行数据
        """
        # 获取当前表格共有多少行
        rows = self.ui.tableWidget.rowCount()
        new_row = rows
        print("新增设备")
        self.ui.tableWidget.insertRow(new_row)
        self.ui.tableWidget.setItem(new_row, 0, QTableWidgetItem(bmc_ip))  # 设置j行0列的内容为Value
        self.ui.tableWidget.setItem(new_row, 1, QTableWidgetItem(bmc_user))  # 设置j行1列的内容为Value
        self.ui.tableWidget.setItem(new_row, 2, QTableWidgetItem(bmc_pwd))
        self.ui.tableWidget.setItem(new_row, 3, QTableWidgetItem(os_ip))
        self.ui.tableWidget.setItem(new_row, 4, QTableWidgetItem(os_user))
        self.ui.tableWidget.setItem(new_row, 5, QTableWidgetItem(os_pwd))

    def sub_device(self):
        # 删除行数据
        # 获取当前表格共有多少行
        rows = self.ui.tableWidget.rowCount()
        print("删除设备")
        if rows == 0:
            # self.message("表格")
            pass
        self.ui.tableWidget.removeRow(rows - 1)

    def get_basic_info(self):
        self.env_list = []
        # item1 = self.ui.tableWidget.item(0, 0).text()
        # print(item1)
        print("------------------------")
        rows = self.ui.tableWidget.rowCount()
        # columns = self.ui.tableWidget.columnCount()
        print("该表共有{}行".format(rows))
        # print("该表共有{}列".format(columns))
        for row in range(rows):
            device_dict = {}
            bmc_ip = self.ui.tableWidget.item(row, 0).text()
            bmc_user = self.ui.tableWidget.item(row, 1).text()
            bmc_pwd = self.ui.tableWidget.item(row, 2).text()
            os_ip = self.ui.tableWidget.item(row, 3).text()
            os_user = self.ui.tableWidget.item(row, 4).text()
            os_pwd = self.ui.tableWidget.item(row, 5).text()
            if not self.is_ipv4(bmc_ip):
                print("输入的bmc ip 不合法")
                msg_box = QMessageBox(QMessageBox.Warning, "警告", "输入的bmc ip 不合法")
                msg_box.exec_()
            if not self.is_ipv4(os_ip):
                print("输入的os ip 不合法")
                msg_box = QMessageBox(QMessageBox.Warning, "警告", "输入的bmc ip 不合法")
                msg_box.exec_()

            if bmc_ip and bmc_user and bmc_pwd and os_ip and os_user and os_pwd:
                device_dict["bmc_ip"] = bmc_ip
                device_dict["bmc_user"] = bmc_user
                device_dict["bmc_password"] = bmc_pwd
                device_dict["os_ip"] = os_ip
                device_dict["os_user"] = os_user
                device_dict["os_password"] = os_pwd
                self.env_list.append(device_dict)

        print(self.env_list)

    def tab_change(self):
        if self.ui.tabWidget.currentIndex() == 1:
            self.get_basic_info()
            self.dynamic_display_other_page()

    def next_click(self):
        pass

    def is_ipv4(self, ip):
        return True if [1] * 4 == [x.isdigit() and 0 <= int(x) <= 255 for x in ip.split(".")] else False

    def dynamic_display_other_page(self):
        print("我是动态显示sheet页的函数")
        print("当前获取到的合法环境信息：{}".format(self.env_list))
        os_ip_list = [device["os_ip"] for device in  self.env_list]
        for os_ip in os_ip_list:
            ip_lable = QLabel(os_ip)
            role_edit = QLineEdit()
            display_radio = QRadioButton()
            self.ui.tab_2.horizontalLayoutWidget_2.addWidget(ip_lable)
            self.ui.tab_2.horizontalLayoutWidget_2.addWidget(role_edit)
            self.ui.tab_2.horizontalLayoutWidget_2.addWidget(display_radio)

        # import time
        # time.sleep(3)
        # self.ui.tabWidget.
        # layout = QFormLayout()
        # layout.addRow('姓名', QLabel())
        # layout.addRow('地址', QLineEdit())
        # # self.setTabText(0, '联系方式')
        # self.ui.tab_2.setLayout(layout)
        # for os_ip in os_ip_list:
        #     self.ui.tab_2.addTab(self.ui.tab_2, "dsada {}".format(os_ip))

        # layout = QVBoxLayout()
        # layout.setSpacing(20)
        # hLayout1 = QHBoxLayout()
        # # hLayout1.BottomToTop()
        # label1 = QLabel("OS IP")
        # hLayout1.addWidget(label1)
        #
        # label1 = QLabel("服务器角色")
        # hLayout1.addWidget(label1)
        #
        # label1 = QLabel("是否前台展示")
        # hLayout1.addWidget(label1)
        #
        # layout.addLayout(hLayout1)
        #
        # self.ui.tab_2.setLayout(layout)


        # self.layout = QVBoxLayout()
        # self.layout.setSpacing(20)
        # # 第一行按钮布局管理
        # hLayout1 = QHBoxLayout()
        # button = QPushButton("Button1")
        # button.setMinimumSize(60, 30)
        # button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # hLayout1.addWidget(button)
        # button = QPushButton("Button2")
        # button.setMinimumSize(60, 30)
        # button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # hLayout1.addWidget(button)
        # 第二行按钮布局管理
        # hLayout2 = QHBoxLayout()
        # button = QPushButton("Button1")
        # button.setMinimumSize(60, 30)
        # button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # hLayout2.addWidget(button)
        # button = QPushButton("Button2")
        # button.setMinimumSize(60, 30)
        # button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # hLayout2.addWidget(button)
        # 整体垂直布局管理
        # self.layout.addLayout(hLayout1)
        # self.layout.addLayout(hLayout2)

        # self.ui.tab_2.setLayout(self.layout)


        # self.box_layout1 = QVBoxLayout()
        # self.box_layout1.setContentsMargins(0, 0, 0, 0)
        # self.box_layout1.setSpacing(0)
        # self.list_widget = QListWidget()
        # self.list_widget.setFixedSize(200, 500)
        # self.list_widget.sizeHintForColumn(0)
        # self.someWidget3 = QLineEdit()
        # self.someWidget3.setFixedWidth(200)
        # self.box_layout1.addWidget(self.list_widget, Qt.AlignLeft)
        # self.box_layout1.addWidget(self.someWidget3, Qt.AlignLeft)

        # Right side
        # self.box_layout2 = QVBoxLayout()
        # self.box_layout2.setContentsMargins(0, 0, 0, 0)
        # self.box_layout2.setGeometry(QRect(0, 0, 800, 680))
        # self.tabs_widget = TabsWidget(self)
        # self.box_layout2.addWidget(self.tabs_widget)

        # self.box_layout1.addLayout()


app = QApplication([])
testcase_info = EnvironmentInfo()
testcase_info.ui.show()
app.exec_()