import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QLabel, QLineEdit, QToolButton,
                             QPushButton)
from PyQt5.QtCore import Qt


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.bodyLayout = QGridLayout()

        # 欢迎登陆图书馆系统标题
        self.titleText = QLabel(self)
        self.titleText.setText('图书管理系统')
        self.titleText.setAlignment(Qt.AlignCenter)
        self.titleText.setFixedSize(900, 120)

        # 账号标题
        account = QLabel()
        account.setText('用户名')
        account.setStyleSheet('*{font-size: 25px;}')

        # 密码标题
        password = QLabel()
        password.setText('密码')
        password.setStyleSheet('*{font-size: 25px;}')

        # 学号输入框
        self.accountInput = QLineEdit()
        self.accountInput.setFixedSize(800, 100)
        self.accountInput.setText('请输入用户名')
        self.accountInput.setTextMargins(5, 5, 5, 5)
        self.accountInput.mousePressEvent = lambda x: self.inputClick(
            self.accountInput)
        self.accountInput.setClearButtonEnabled(True)
        self.accountInput.setStyleSheet('*{font-size: 25px;}')

        # 密码输入框
        self.passwordInput = QLineEdit()
        self.passwordInput.setFixedSize(800, 100)
        self.passwordInput.setText('请输入密码')
        self.passwordInput.setTextMargins(5, 5, 5, 5)
        self.passwordInput.mousePressEvent = lambda x: self.inputClick(
            self.passwordInput)

        self.passwordInput.setClearButtonEnabled(True)  # 清空按钮
        self.passwordInput.setStyleSheet('*{font-size: 25px;}')

        # 注册按钮
        self.signup = QPushButton()
        self.signup.setText('注 册')
        self.signup.setFixedSize(180, 100)

        # 登录按钮
        self.loginButton = QToolButton()
        self.loginButton.setText('登  录')
        self.loginButton.setFixedSize(180, 100)

        # 注册和登录
        self.clickBox = QHBoxLayout()
        self.clickBox.addWidget(self.signup)
        self.clickBox.addWidget(self.loginButton)

        # 把上面定义的元素加入大框
        self.inputBoxLayout = QVBoxLayout()
        self.inputBoxLayout.addWidget(account)
        self.inputBoxLayout.addWidget(self.accountInput)
        self.inputBoxLayout.addWidget(password)
        self.inputBoxLayout.addWidget(self.passwordInput)
        self.inputBoxLayout.addLayout(self.clickBox)

        # 下面一个大框
        self.inputBox = QWidget()
        self.inputBox.setObjectName('inputBox')
        self.inputBox.setContentsMargins(30, 30, 30, 30)
        self.inputBox.setFixedSize(900, 700)
        self.inputBox.setLayout(self.inputBoxLayout)

        # 把大标题和下面输入框加入self
        self.bodyLayout.addWidget(self.titleText, 0, 0)
        self.bodyLayout.addWidget(self.inputBox, 1, 0)
        self.setLayout(self.bodyLayout)
        self.setFixedSize(900, 900)
        self.setMyStyle()

    def inputClick(self, e):
        if e.text() == '请输入用户名':
            e.setText('')
            return
        elif e.text() == '请输入密码':
            e.setText('')
            e.setEchoMode(QLineEdit.Password)  # 黑点覆盖

    def setMyStyle(self):
        self.setStyleSheet('''
            QWidget{
                background-color:white;
            }
        ''')
        self.titleText.setStyleSheet('''
            *{
                color: rgba(63, 101, 114, 1);
                width: 200px;
                background-color: rgba(203, 231, 245, 1);
                border: 1px solid rgba(220, 243, 249, 1);
                border-radius: 10px;
                font-size: 45px;
            }
        ''')
        self.inputBox.setStyleSheet('''
        QWidget#inputBox{
            border-radius: 5px;
            border: 1px solid rgba(229, 229, 229, 1);
        }
        QLineEdit{
            color: grey;
            border-radius: 5px;
            border: 1px solid rgba(229, 229, 229, 1);
        }
        QToolButton{
            border-radius: 10px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        QPushButton{
            border-radius: 10px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())
