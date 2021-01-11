import sys
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QLabel, QLineEdit,
                             QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from model import database
# import database


class StudentInfo(QGroupBox):
    '''
    编辑学生信息的界面
    传入{
        'SID': str,
        'SNAME': str,
        'DEPARTMENT': str,
        'MAJOR': str,
    }
    返回{
        'SID': str,
        'SNAME': str,
        'PASSWORD': str,
        'DEPARTMENT': str,
        'MAJOR': str,
    }
    '''
    after_close = pyqtSignal(dict)

    def __init__(self, stu_info: dict):
        super().__init__()
        self.stu_info = stu_info

        self.title = QLabel()
        self.title.setText('学生信息')

        self.subTitle = QLabel()
        self.subTitle.setText('编辑学生信息')

        # 学号输入框
        self.SIDInput = QLineEdit()
        self.SIDInput.setFixedSize(600, 60)
        self.SIDInput.setText(self.stu_info['SID'])
        self.SIDInput.initText = '请输入学号'
        self.SIDInput.setEnabled(False)

        # 姓名输入框
        self.nameInput = QLineEdit()
        self.nameInput.setFixedSize(600, 60)
        self.nameInput.setText(self.stu_info['SNAME'])
        self.nameInput.initText = '请输入姓名'
        self.nameInput.setTextMargins(5, 5, 5, 5)
        self.nameInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                   nameInput)

        # 密码
        self.passwordInput = QLineEdit()
        self.passwordInput.setFixedSize(600, 60)
        self.passwordInput.setText('请输入密码')
        self.passwordInput.initText = '请输入密码'
        self.passwordInput.setTextMargins(5, 5, 5, 5)
        self.passwordInput.mousePressEvent = lambda x: self.inputClick(
            self.passwordInput)

        # 重复密码
        self.repPasswordInput = QLineEdit()
        self.repPasswordInput.setFixedSize(600, 60)
        self.repPasswordInput.setText('请重复输入密码')
        self.repPasswordInput.initText = '请重复输入密码'
        self.repPasswordInput.setTextMargins(5, 5, 5, 5)
        self.repPasswordInput.mousePressEvent = lambda x: self.inputClick(
            self.repPasswordInput)

        # 学院
        self.deptInput = QLineEdit()
        self.deptInput.setFixedSize(600, 60)
        self.deptInput.setText(self.stu_info['DEPARTMENT'])
        self.deptInput.initText = '请输入所在院系'
        self.deptInput.setTextMargins(5, 5, 5, 5)
        self.deptInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                   deptInput)

        # 功法
        self.majorInput = QLineEdit()
        self.majorInput.setFixedSize(600, 60)
        self.majorInput.setText(self.stu_info['MAJOR'])
        self.majorInput.initText = '请输入专业名称'
        self.majorInput.setTextMargins(5, 5, 5, 5)
        self.majorInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                    majorInput)

        # 提交
        self.submit = QToolButton()
        self.submit.setText('提交')
        self.submit.setFixedSize(600, 60)
        self.submit.clicked.connect(self.submitFunction)

        # 退出
        self.back = QToolButton()
        self.back.setText('退出')
        self.back.setFixedSize(600, 60)
        self.back.clicked.connect(self.close)

        self.btnList = [
            self.SIDInput,
            self.nameInput,
            self.passwordInput,
            self.repPasswordInput,
            self.deptInput,
            self.majorInput,
        ]

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.addWidget(self.title)
        self.bodyLayout.addWidget(self.subTitle)
        for i in self.btnList:
            self.bodyLayout.addWidget(i)
        self.bodyLayout.addWidget(self.submit)
        self.bodyLayout.addWidget(self.back)

        self.setLayout(self.bodyLayout)
        self.initUI()

    def inputClick(self, e):
        for i in range(2, 9):
            item = self.bodyLayout.itemAt(i).widget()
            if item.text() == '':
                item.setText(item.initText)
                if item is self.passwordInput or item is self.repPasswordInput:
                    item.setEchoMode(QLineEdit.Normal)

        if e.text() == e.initText:
            e.setText('')
        if e is self.passwordInput or e is self.repPasswordInput:
            e.setEchoMode(QLineEdit.Password)

    def submitFunction(self):
        if self.passwordInput.text() != self.passwordInput.initText:
            if self.passwordInput.text() != self.repPasswordInput.text():
                msgBox = QMessageBox(QMessageBox.Warning, "错误!", '两次输入密码不一致!',
                                     QMessageBox.NoButton, self)
                msgBox.addButton("确认", QMessageBox.AcceptRole)
                msgBox.exec_()
                return
            self.stu_info['PASSWORD'] = database.encrypt(
                self.passwordInput.text())
        self.stu_info['SNAME'] = self.nameInput.text()
        self.stu_info['DEPARTMENT'] = self.deptInput.text()
        self.stu_info['MAJOR'] = self.majorInput.text()
        self.close()
        self.after_close.emit(self.stu_info)

    def initUI(self):
        self.setFixedSize(800, 750)
        self.setWindowTitle('编辑学生信息')
        self.setWindowIcon(QIcon('icon/person.png'))
        self.setMyStyle()

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        QLineEdit{
            border:0px;
            border-bottom: 1px solid rgba(229, 229, 229, 1);
            color: grey;
            font-size: 25px
        }
        QToolButton{
            border: 0px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        QGroupBox{
            border: 1px solid rgba(229, 229, 229, 1);
            border-radius: 5px;
        }
        ''')
        self.title.setStyleSheet('''
        *{
            color: rgba(113, 118, 121, 1);
            font-size: 45px;
            font-family: 微软雅黑;
        }
        ''')
        self.subTitle.setStyleSheet('''
        *{
            color: rgba(184, 184, 184, 1);
            font-size: 35px;
        }
        ''')


if __name__ == '__main__':
    stu_msg = {
        'SID': '001',
        'PASSWORD':
        '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92',
        'SNAME': '乌大郎',
        'DEPARTMENT': '炸天帮',
        'MAJOR': '玄学',
        'PUNISHED': 0
    }
    app = QApplication(sys.argv)
    ex = StudentInfo(stu_msg)
    ex.show()
    sys.exit(app.exec_())
