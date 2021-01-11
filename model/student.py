import sys
sys.path.append('./')
import time
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QGroupBox,
                             QToolButton, QSplitter, QVBoxLayout, QHBoxLayout,
                             QLabel, QTableWidget, QTableWidgetItem,
                             QAbstractItemView, QLineEdit, QFileDialog,
                             QToolTip, QComboBox, QMessageBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from model import database
# import database


class StudentPage(QWidget):
    def __init__(self, stu_mes):
        super().__init__()
        self.focus = 0
        self.stu_mes = stu_mes
        self.initUI()

    def initUI(self):
        # 标题栏
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1620, 75)
        self.setTitleBar()

        # 分割
        self.body = QSplitter()
        self.setLeftMunu()
        self.content = None
        self.setContent()

        self.bodyLayout = QGridLayout()
        self.bodyLayout.addWidget(self.titleBar, 0, 0, 1, 7)
        self.bodyLayout.addWidget(self.body, 1, 0, 7, 7)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.bodyLayout)
        self.setFixedSize(1920, 960)
        self.setMyStyle()

    # 设置标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('图书管理系统')
        self.title.setFixedHeight(45)

        self.account = QToolButton()
        self.account.setIcon(QIcon('icon/person.png'))
        self.account.setText(self.stu_mes['SID'])
        self.account.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.account.setFixedHeight(30)
        self.account.setEnabled(False)

        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFixedHeight(45)

        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(100)
        titleLayout.addWidget(self.title)
        titleLayout.addWidget(self.account)
        titleLayout.addWidget(self.out)
        self.titleBar.setLayout(titleLayout)

    # 左侧菜单栏
    def setLeftMunu(self):
        # 查询按钮
        self.bookSearch = QToolButton()
        self.bookSearch.setText('图书查询')
        self.bookSearch.setFixedSize(250, 75)
        self.bookSearch.setIcon(QIcon('icon/book.png'))
        self.bookSearch.setIconSize(QSize(45, 45))
        self.bookSearch.clicked.connect(
            lambda: self.switch(0, self.bookSearch))
        self.bookSearch.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 借阅按钮
        self.borrow = QToolButton()
        self.borrow.setText('借阅信息')
        self.borrow.setFixedSize(250, 75)
        self.borrow.setIcon(QIcon('icon/borrowing.png'))
        self.borrow.setIconSize(QSize(45, 45))
        self.borrow.clicked.connect(lambda: self.switch(1, self.borrow))
        self.borrow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 借阅历史
        self.history = QToolButton()
        self.history.setText('借阅历史')
        self.history.setFixedSize(250, 75)
        self.history.setIcon(QIcon('icon/history.png'))
        self.history.setIconSize(QSize(45, 45))
        self.history.clicked.connect(lambda: self.switch(2, self.history))
        self.history.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 个人信息
        self.detail = QToolButton()
        self.detail.setText('个人信息')
        self.detail.setFixedSize(250, 75)
        self.detail.setIcon(QIcon('icon/detail.png'))
        self.detail.setIconSize(QSize(45, 45))
        self.detail.clicked.connect(lambda: self.switch(3, self.detail))
        self.detail.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.btnList = [
            self.bookSearch, self.borrow, self.history, self.detail
        ]

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.bookSearch)
        self.layout.addWidget(self.borrow)
        self.layout.addWidget(self.history)
        self.layout.addWidget(self.detail)
        self.layout.addStretch()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.menu = QGroupBox()
        self.menu.setFixedSize(250, 750)
        self.menu.setLayout(self.layout)
        self.menu.setContentsMargins(0, 0, 0, 0)
        self.body.addWidget(self.menu)

    def switch(self, index, btn):
        self.focus = index
        for i in self.btnList:
            i.setStyleSheet('''
            *{
                background: white;
            }
            QToolButton:hover{
                background-color: rgba(230, 230, 230, 0.3);
            }
            ''')

        btn.setStyleSheet('''
        QToolButton{
            background-color: rgba(230, 230, 230, 0.7);
        }
        ''')
        self.setContent()

    # 设置右侧信息页
    def setContent(self):
        if self.content is not None:
            self.content.deleteLater()
        if self.focus == 0:
            self.content = Books(self.stu_mes)
        elif self.focus == 1:
            self.content = BorrowingBooks(self.stu_mes)
        elif self.focus == 2:
            self.content = History(self.stu_mes)
        else:
            self.content = detail(self.stu_mes)
        self.body.addWidget(self.content)

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget{
            background-color: rgba(44,44,44,1);
            border:1px solid black;
            border-radius: 10px;
        }
        ''')
        self.menu.setStyleSheet('''
        QWidget{
            border: 0px;
            border-right: 1px solid rgba(227, 227, 227, 1);
        }
        QToolButton{
            color: rgba(51, 90, 129, 1);
            font-family: 微软雅黑;
            font-size: 35px;
            border-right: 1px solid rgba(227, 227, 227, 1);
        }
        QToolButton:hover{
            background-color: rgba(230, 230, 230, 0.3);
        }
        ''')
        self.title.setStyleSheet('''
        *{
            color: white;
            font-family: 微软雅黑;
            font-size: 35px;
            border: 0px;
        }
        ''')
        self.account.setStyleSheet('''
        *{
            color: white;
            font-weight: 微软雅黑;
            font-size: 35px;
            border: 0px;
        }
        ''')
        self.out.setStyleSheet('''
        QToolButton{
            color: white;
            border:0px;
            font-size: 18px;
        }
        QToolButton:hover{
            color: rgba(11, 145, 255, 1);
        }
        ''')


class Books(QGroupBox):
    def __init__(self, stu_mes):
        super().__init__()
        self.stu_mes = stu_mes
        self.book_list = []
        self.body = QVBoxLayout()
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()

        self.setLayout(self.body)
        #self.setFixedSize(1100, 600)
        self.setMyStyle()

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('书籍信息')
        self.title.setFixedHeight(40)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1340, 75)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # 设置搜索框
    def setSearchBar(self):
        self.selectBox = QComboBox()
        self.selectBox.addItems(['书号', '分类', '出版社', '作者', '书名'])
        self.selectBox.setFixedHeight(45)
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索书籍')
        self.searchInput = QLineEdit()
        self.searchInput.setText('')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(600, 60)
        self.searchButton = QToolButton()
        self.searchButton.setFixedSize(150, 60)
        self.searchButton.setText('搜索')
        self.searchButton.clicked.connect(self.searchFunction)
        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.selectBox)
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addStretch()
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    def searchFunction(self):
        convert = {
            '书号': 'BID',
            '分类': 'CLASSIFICATION',
            '出版社': 'PRESS',
            '作者': 'AUTHOR',
            '书名': 'BNAME',
            '': 'BNAME'
        }
        self.book_list = database.search_book(
            self.searchInput.text(), convert[self.selectBox.currentText()],
            self.stu_mes['SID'])
        if self.book_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.setTable()

    # 设置表格
    def setTable(self):
        self.table = QTableWidget(1, 9)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(6, 120)

        self.table.setItem(0, 0, QTableWidgetItem('书号'))
        self.table.setItem(0, 1, QTableWidgetItem('书名'))
        self.table.setItem(0, 2, QTableWidgetItem('作者'))
        self.table.setItem(0, 3, QTableWidgetItem('出版日期'))
        self.table.setItem(0, 4, QTableWidgetItem('出版社'))
        self.table.setItem(0, 5, QTableWidgetItem('分类'))
        self.table.setItem(0, 6, QTableWidgetItem('位置'))
        self.table.setItem(0, 7, QTableWidgetItem('总数/剩余'))
        self.table.setItem(0, 8, QTableWidgetItem('操作'))

        for i in range(9):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        # 显示借阅详情
        for i in self.book_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemBID = QTableWidgetItem(val[0])
        itemBID.setTextAlignment(Qt.AlignCenter)

        itemNAME = QTableWidgetItem('《' + val[1] + '》')
        itemNAME.setTextAlignment(Qt.AlignCenter)

        itemAUTHOR = QTableWidgetItem(val[2])
        itemAUTHOR.setTextAlignment(Qt.AlignCenter)

        itemDATE = QTableWidgetItem(val[3])
        itemDATE.setTextAlignment(Qt.AlignCenter)

        itemPRESS = QTableWidgetItem(val[4])
        itemPRESS.setTextAlignment(Qt.AlignCenter)

        itemPOSITION = QTableWidgetItem(val[5])
        itemPOSITION.setTextAlignment(Qt.AlignCenter)

        itemSUM = QTableWidgetItem(str(val[6]) + '/' + str(val[7]))
        itemSUM.setTextAlignment(Qt.AlignCenter)

        itemCLASSIFICATION = QTableWidgetItem(val[8])
        itemCLASSIFICATION.setTextAlignment(Qt.AlignCenter)

        itemOPERATE = QToolButton(self.table)
        itemOPERATE.setFixedSize(70, 25)
        if val[-1] == '借书':
            itemOPERATE.setText('借书')
            itemOPERATE.clicked.connect(lambda: self.borrowBook(val[0]))
            itemOPERATE.setStyleSheet('''
            *{
                color: white;
                font-family: 微软雅黑;
                background: rgba(38, 175, 217, 1);
                border: 0;
                border-radius: 10px;
                font-size:18px;
            }
            ''')
        else:
            itemOPERATE.setText('不可借')
            itemOPERATE.setEnabled(False)
            itemOPERATE.setToolTip(val[-1])
            QToolTip.setFont(QFont('微软雅黑', 15))
            itemOPERATE.setStyleSheet('''
            QToolButton{
                color: white;
                font-family: 微软雅黑;
                background: rgba(200, 200, 200, 1);
                border: 0;
                border-radius: 10px;
                font-size:18px;
            }
            QToolTip{
                color: black;
                border: 1px solid rgba(200, 200, 200, 1);
            }
            ''')

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemOPERATE)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemBID)
        self.table.setItem(1, 1, itemNAME)
        self.table.setItem(1, 2, itemAUTHOR)
        self.table.setItem(1, 3, itemDATE)
        self.table.setItem(1, 4, itemPRESS)
        self.table.setItem(1, 5, itemCLASSIFICATION)
        self.table.setItem(1, 6, itemPOSITION)
        self.table.setItem(1, 7, itemSUM)
        self.table.setCellWidget(1, 8, itemWidget)

    def borrowBook(self, BID: str):
        ans = database.borrow_book(BID, self.stu_mes['SID'])
        # 刷新表格
        if ans:
            self.searchFunction()

    def setMyStyle(self):
        self.setStyleSheet('''
        *{
            background-color: white;
            border:0px;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget {
            border:0;
            background-color: rgba(216, 216, 216, 1);
            border-radius: 20px;
            color: rgba(113, 118, 121, 1);
        }
        QLabel{
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')
        self.searchTitle.setStyleSheet('''
            QLabel{
                font-size:20px;
                color: black;
                font-family: 微软雅黑;
            }
        ''')
        self.searchInput.setStyleSheet('''
            QLineEdit{
                border: 1px solid rgba(201, 201, 201, 1);
                border-radius: 5px;
                color: rgba(120, 120, 120, 1);
                font-size: 25px
            }
        ''')
        self.searchButton.setStyleSheet('''
            QToolButton{
                border-radius: 10px;
                background-color:rgba(52, 118, 176, 1);
                color: white;
                font-size: 25px;
                font-family: 微软雅黑;
            }
        ''')
        self.selectBox.setStyleSheet('''
        *{
            border: 0px;
            font-size: 15px;
        }
        QComboBox{
            border: 1px solid rgba(201, 201, 201, 1);
        }
        ''')


# 正在借阅的书
class BorrowingBooks(QGroupBox):
    def __init__(self, stu_mes):
        super().__init__()
        self.stu_mes = stu_mes
        self.body = QVBoxLayout()
        self.setTitleBar()
        self.setTable()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('借阅信息')
        self.title.setFixedHeight(40)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1340, 75)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    def setTable(self, val: dict = None):
        self.table = QTableWidget(1, 6)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 125)
        self.table.setColumnWidth(1, 225)
        self.table.setColumnWidth(2, 255)
        self.table.setColumnWidth(3, 255)
        self.table.setColumnWidth(4, 125)
        self.table.setColumnWidth(5, 125)

        self.table.setItem(0, 0, QTableWidgetItem('书号'))
        self.table.setItem(0, 1, QTableWidgetItem('书名'))
        self.table.setItem(0, 2, QTableWidgetItem('借书日期'))
        self.table.setItem(0, 3, QTableWidgetItem('还书日期'))
        self.table.setItem(0, 4, QTableWidgetItem('罚金'))
        self.table.setItem(0, 5, QTableWidgetItem('操作'))

        for i in range(6):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))
        self.body.addWidget(self.table)

        # 显示借阅详情
        self.book_list = database.get_borrowing_books(self.stu_mes['SID'])
        for i in self.book_list:
            self.insertRow(i)
        self.table.setStyleSheet('''
        *{
            font-size:18px;
            color: black;
            background-color: white;
            font-family: 微软雅黑;
        }
        ''')

    # 插入行
    def insertRow(self, val: list):
        itemBID = QTableWidgetItem(val[1])
        itemBID.setTextAlignment(Qt.AlignCenter)
        itemNAME = QTableWidgetItem('《' + val[2] + '》')
        itemNAME.setTextAlignment(Qt.AlignCenter)
        itemBEGIN = QTableWidgetItem(val[3])
        itemBEGIN.setTextAlignment(Qt.AlignCenter)
        itemBACK = QTableWidgetItem(val[4])
        itemBACK.setTextAlignment(Qt.AlignCenter)
        itemPUNISHED = QLabel()
        itemPUNISHED.setText('0')
        itemPUNISHED.setAlignment(Qt.AlignCenter)
        isPunished = database.days_between(val[4],
                                           time.strftime("%Y-%m-%d-%H:%M"))
        if isPunished <= 0:
            itemPUNISHED.setStyleSheet('''
                *{
                    color: green;
                    font-size:20px;
                    font-family: 微软雅黑;
                }
            ''')
        else:
            itemPUNISHED.setText(str(isPunished))
            itemPUNISHED.setStyleSheet('''
                *{
                    color: red;
                    font-size:20px;
                    font-family: 微软雅黑;
                }
            ''')
        itemOPERATE = QToolButton(self.table)
        itemOPERATE.setFixedSize(80, 30)
        if isPunished <= 0:
            itemOPERATE.setText('还书')
            itemOPERATE.clicked.connect(lambda: self.retrurnBook(val[1]))
            itemOPERATE.setStyleSheet('''
            *{
                color: white;
                font-family: 微软雅黑;
                background: rgba(38, 175, 217, 1);
                border: 0;
                border-radius: 10px;
                font-size:18px;
            }
            ''')
        else:
            itemOPERATE.setText('交罚金')
            itemOPERATE.clicked.connect(lambda: self.pay(val[1], isPunished))
            itemOPERATE.setStyleSheet('''
            *{
                color: white;
                font-family: 微软雅黑;
                background: rgba(222, 52, 65, 1);
                border: 0;
                border-radius: 10px;
                font-size:18px;
            }
            ''')

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemOPERATE)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemBID)
        self.table.setItem(1, 1, itemNAME)
        self.table.setItem(1, 2, itemBEGIN)
        self.table.setItem(1, 3, itemBACK)
        self.table.setCellWidget(1, 4, itemPUNISHED)
        self.table.setCellWidget(1, 5, itemWidget)

    def retrurnBook(self, BID: str):
        ans = database.return_book(BID, self.stu_mes['SID'])
        # 刷新表格
        if ans:
            self.book_list = database.get_borrowing_books(self.stu_mes['SID'])
            self.table.deleteLater()
            self.setTable()

    def pay(self, BID: str, PUNISH):
        ans = database.pay(BID, self.stu_mes['SID'], PUNISH)
        # 刷新表格
        if ans:
            self.book_list = database.get_borrowing_books(self.stu_mes['SID'])
            self.table.deleteLater()
            self.setTable()

    def initUI(self):
        self.setFixedSize(1440, 600)
        self.setStyleSheet('''
        *{
            background-color: white;
            border:0px;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget {
            border:0;
            background-color: rgba(216, 216, 216, 1);
            border-radius: 20px;
            color: rgba(113, 118, 121, 1);
        }
        QLabel{
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')


class History(QGroupBox):
    def __init__(self, stu_mes):
        super().__init__()
        self.stu_mes = stu_mes
        self.body = QVBoxLayout()
        self.setTitleBar()
        self.setTable()
        self.setOut()
        self.body.addStretch()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('借阅记录')
        self.title.setFixedHeight(40)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1340, 75)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # 创建表格
    def setTable(self, val: dict = None):
        self.table = QTableWidget(1, 5)
        self.table.setFixedHeight(600)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 375)
        self.table.setColumnWidth(2, 255)
        self.table.setColumnWidth(3, 255)
        self.table.setColumnWidth(4, 150)

        self.table.setItem(0, 0, QTableWidgetItem('书号'))
        self.table.setItem(0, 1, QTableWidgetItem('书名'))
        self.table.setItem(0, 2, QTableWidgetItem('借书日期'))
        self.table.setItem(0, 3, QTableWidgetItem('还书日期'))
        self.table.setItem(0, 4, QTableWidgetItem('罚金'))

        for i in range(5):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        self.list = database.get_log(self.stu_mes['SID'])
        for i in self.list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemBID = QTableWidgetItem(val[1])
        itemBID.setTextAlignment(Qt.AlignCenter)
        itemNAME = QTableWidgetItem('《' + val[2] + '》')
        itemNAME.setTextAlignment(Qt.AlignCenter)
        itemBEGIN = QTableWidgetItem(val[3])
        itemBEGIN.setTextAlignment(Qt.AlignCenter)
        itemBACK = QTableWidgetItem(val[4])
        itemBACK.setTextAlignment(Qt.AlignCenter)
        itemPUNISHED = QLabel()
        itemPUNISHED.setText(str(val[5]))
        itemPUNISHED.setAlignment(Qt.AlignCenter)
        if val[5] == 0:
            itemPUNISHED.setStyleSheet('''
                *{
                    color: green;
                    font-size: 20px;
                }
            ''')
        else:
            itemPUNISHED.setStyleSheet('''
                *{
                    color: red;
                    font-size: 20px;
                }
            ''')

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemBID)
        self.table.setItem(1, 1, itemNAME)
        self.table.setItem(1, 2, itemBEGIN)
        self.table.setItem(1, 3, itemBACK)
        self.table.setCellWidget(1, 4, itemPUNISHED)

    # 导出文件
    def setOut(self):
        self.outButton = QToolButton()
        self.outButton.setText('导出')
        self.outButton.clicked.connect(self.outFunction)
        self.outButton.setFixedSize(100, 50)
        outLayout = QHBoxLayout()
        outLayout.addStretch()
        outLayout.addWidget(self.outButton)
        outWidget = QWidget()
        outWidget.setLayout(outLayout)

        self.body.addWidget(outWidget)

    def outFunction(self):
        import csv
        dirName = QFileDialog.getExistingDirectory(self, '选择文件夹')

        title = ['SID', 'BID', 'BNAME', 'BORROW_DATE', 'BACK_DATE', 'PUNISHED']
        with open(os.path.join(dirName, self.stu_mes['SID'] + '.csv'),
                  'w',
                  newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(title)
            for row in self.list:
                writer.writerow(row)

    def initUI(self):
        self.setFixedSize(1440, 700)
        self.setStyleSheet('''
        *{
            background-color: white;
            border:0px;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget {
            border:0;
            background-color: rgba(216, 216, 216, 1);
            border-radius: 20px;
            color: rgba(113, 118, 121, 1);
        }
        QLabel{
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')
        self.table.setStyleSheet('''
            font-size:18px;
            color: black;
            background-color: white;
            font-family: 微软雅黑;
        ''')
        self.outButton.setStyleSheet('''
        QToolButton{
            border-radius: 10px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')


class detail(QWidget):
    def __init__(self, stu_mes):
        super().__init__()
        self.stu_mes = database.get_student_info(stu_mes['SID'])

        # 学号输入框
        account = QLabel()
        account.setText('学号')
        self.accountInput = QLineEdit()
        self.accountInput.setFixedSize(600, 60)
        self.accountInput.setText(self.stu_mes['SID'])
        self.accountInput.setTextMargins(5, 5, 5, 5)
        self.accountInput.setEnabled(False)
        accountLayout = QHBoxLayout()
        accountLayout.addStretch()
        accountLayout.addWidget(account)
        accountLayout.addWidget(self.accountInput)
        self.accountInput.mousePressEvent = lambda x: self.inputClick(
            self.accountInput)

        # 姓名输入框
        name = QLabel()
        name.setText('姓名')
        self.nameInput = QLineEdit()
        self.nameInput.setFixedSize(600, 60)
        self.nameInput.setText(self.stu_mes['SNAME'])
        self.nameInput.setTextMargins(5, 5, 5, 5)
        self.nameInput.setEnabled(False)
        nameLayout = QHBoxLayout()
        nameLayout.addStretch()
        nameLayout.addWidget(name)
        nameLayout.addWidget(self.nameInput)
        self.nameInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                   nameInput)

        # 密码
        password = QLabel()
        password.setText('密码')
        self.passwordInput = QLineEdit()
        self.passwordInput.setFixedSize(600, 60)
        self.passwordInput.setText('请输入密码')
        self.passwordInput.initText = '请输入密码'
        self.passwordInput.setTextMargins(5, 5, 5, 5)
        self.passwordInput.setEnabled(False)
        passwordLayout = QHBoxLayout()
        passwordLayout.addStretch()
        passwordLayout.addWidget(password)
        passwordLayout.addWidget(self.passwordInput)
        self.passwordInput.mousePressEvent = lambda x: self.inputClick(
            self.passwordInput)

        # 重复密码
        repPassword = QLabel()
        repPassword.setText('请重复输入密码')
        self.repPasswordInput = QLineEdit()
        self.repPasswordInput.setFixedSize(600, 60)
        self.repPasswordInput.setText('请重复输入密码')
        self.repPasswordInput.initText = '请重复输入密码'
        self.repPasswordInput.setTextMargins(5, 5, 5, 5)
        self.repPasswordInput.setEnabled(False)
        repPasswordLayout = QHBoxLayout()
        repPasswordLayout.addStretch()
        repPasswordLayout.addWidget(repPassword)
        repPasswordLayout.addWidget(self.repPasswordInput)
        self.repPasswordInput.mousePressEvent = lambda x: self.inputClick(
            self.repPasswordInput)

        # 院系
        dept = QLabel()
        dept.setText('院系')
        self.deptInput = QLineEdit()
        self.deptInput.setFixedSize(600, 60)
        self.deptInput.setText(self.stu_mes['DEPARTMENT'])
        self.deptInput.setTextMargins(5, 5, 5, 5)
        self.deptInput.setEnabled(False)
        groupLayout = QHBoxLayout()
        groupLayout.addStretch()
        groupLayout.addWidget(dept)
        groupLayout.addWidget(self.deptInput)
        self.deptInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                   deptInput)

        # 专业
        major = QLabel()
        major.setText('专业')
        self.majorInput = QLineEdit()
        self.majorInput.setFixedSize(600, 60)
        self.majorInput.setText(self.stu_mes['MAJOR'])
        self.majorInput.setTextMargins(5, 5, 5, 5)
        self.majorInput.setEnabled(False)
        majorLayout = QHBoxLayout()
        majorLayout.addStretch()
        majorLayout.addWidget(major)
        majorLayout.addWidget(self.majorInput)
        self.majorInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                    majorInput)

        # 保存
        self.save = QToolButton()
        self.save.setText('保存')
        self.save.setFixedSize(150, 60)
        self.save.setEnabled(False)
        self.save.clicked.connect(self.saveFunction)

        # 修改
        self.modify = QToolButton()
        self.modify.setText('修改')
        self.modify.setFixedSize(150, 60)
        self.modify.clicked.connect(self.modifyFunction)

        btnLayout = QHBoxLayout()
        btnLayout.addSpacing(130)
        btnLayout.addWidget(self.modify)
        btnLayout.addWidget(self.save)
        btnLayout.addStretch()

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.addLayout(accountLayout)
        self.bodyLayout.addLayout(nameLayout)
        self.bodyLayout.addLayout(passwordLayout)
        self.bodyLayout.addLayout(repPasswordLayout)
        self.bodyLayout.addLayout(groupLayout)
        self.bodyLayout.addLayout(majorLayout)
        self.bodyLayout.addLayout(btnLayout)
        self.bodyLayout.addStretch()
        self.setLayout(self.bodyLayout)
        self.initUI()

    def inputClick(self, e):

        if e is self.passwordInput or e is self.repPasswordInput:
            e.setEchoMode(QLineEdit.Password)  # 黑点覆盖

    def errorBox(self, mes: str):
        msgBox = QMessageBox(QMessageBox.Warning, "警告!", mes,
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.exec_()

    def saveFunction(self):
        if len(self.nameInput.text()) > 4:
            self.errorBox('姓名长度超过4')
            return
        for c in self.nameInput.text():
            if not ('\u4e00' <= c <= '\u9fa5'):
                self.errorBox('姓名应全为汉字')
                return
        if self.passwordInput.text() != self.repPasswordInput.text():
            self.errorBox('两次输入密码不一致')
            return
        for c in self.deptInput.text():
            if not ('\u4e00' <= c <= '\u9fa5'):
                self.errorBox('院系应全为汉字')
                return
        for c in self.majorInput.text():
            if not ('\u4e00' <= c <= '\u9fa5'):
                self.errorBox('专业应全为汉字')
                return
        if self.passwordInput.text() != '******':
            self.stu_mes['PASSWORD'] = database.encrypt(
                self.passwordInput.text())
        self.stu_mes['SNAME'] = self.nameInput.text()
        self.stu_mes['DEPARTMENT'] = self.deptInput.text()
        self.stu_mes['MAJOR'] = self.majorInput.text()
        if not database.update_student(self.stu_mes):
            print('更新失败')
            return
        self.save.setEnabled(False)
        self.nameInput.setEnabled(False)
        self.passwordInput.setEnabled(False)
        self.repPasswordInput.setEnabled(False)
        self.deptInput.setEnabled(False)
        self.majorInput.setEnabled(False)
        self.setMyStyle()

    def modifyFunction(self):
        self.save.setEnabled(True)
        self.nameInput.setEnabled(True)
        self.passwordInput.setEnabled(True)
        self.repPasswordInput.setEnabled(True)
        self.deptInput.setEnabled(True)
        self.majorInput.setEnabled(True)
        self.setStyleSheet('''
            QWidget{
                background-color: white;
            }
            QLabel{
                font-size: 20px;
                font-family: 微软雅黑;
            }
            QLineEdit{
                border: 1px solid rgba(229, 229, 229, 1);
                border-radius: 10px;
                color: black;
                font-size: 25px
            }
            QToolButton{
                border-radius: 10px;
                background-color:rgba(52, 118, 176, 1);
                color: white;
                font-size: 25px;
                font-family: 微软雅黑;
            }
        ''')
        self.save.setStyleSheet('''
        *{
            background-color:rgba(52, 118, 176, 1);
        }
        ''')

    def initUI(self):
        self.setFixedSize(800, 900)
        self.setMyStyle()

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        QLabel{
            font-size: 20px;
            font-family: 微软雅黑;
        }
        QLineEdit{
            border: 1px solid rgba(229, 229, 229, 1);
            border-radius: 10px;
            color: grey;
            font-size: 25px;
        }
        QToolButton{
            border-radius: 10px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')
        self.save.setStyleSheet('''
        *{
            background-color: gray;
        }
        ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_message = {
        'SID': '201809000122',
        'SNAME': '123456',
        'DEPARTMENT': '计算机系',
        'MAJOR': '计科实',
    }
    ex = StudentPage(user_message)
    ex.show()
    sys.exit(app.exec_())
