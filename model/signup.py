import sys
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QToolButton, QGroupBox)


class Signup(QGroupBox):
    def __init__(self):
        super().__init__()

        self.title = QLabel()
        self.title.setText('注册用户')

        self.subTitle = QLabel()
        self.subTitle.setText('创建一个新的账户')

        self.account = QLabel()
        self.account.setText('学号:')

        self.name = QLabel()
        self.name.setText('姓名:')

        self.password = QLabel()
        self.password.setText('密码:')

        self.repPassword = QLabel()
        self.repPassword.setText('重复密码:')

        self.dept = QLabel()
        self.dept.setText('院系:')

        self.major = QLabel()
        self.major.setText('专业:')

        # 学号输入框
        self.accountInput = QLineEdit()
        self.accountInput.setFixedSize(600, 60)
        self.accountInput.setText('请输入用户名')
        self.accountInput.initText = '请输入用户名'
        self.accountInput.setTextMargins(5, 5, 5, 5)
        self.accountInput.mousePressEvent = lambda x: self.inputClick(
            self.accountInput)

        # 姓名输入框
        self.nameInput = QLineEdit()
        self.nameInput.setFixedSize(600, 60)
        self.nameInput.setText('请输入姓名')
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

        self.passwordBox = QHBoxLayout()
        self.passwordBox.addWidget(self.password)
        self.passwordBox.addWidget(self.passwordInput)

        # 重复密码
        self.repPasswordInput = QLineEdit()
        self.repPasswordInput.setFixedSize(600, 60)
        self.repPasswordInput.setText('请重复输入密码')
        self.repPasswordInput.initText = '请重复输入密码'
        self.repPasswordInput.setTextMargins(5, 5, 5, 5)
        self.repPasswordInput.mousePressEvent = lambda x: self.inputClick(
            self.repPasswordInput)

        # 院系
        self.deptInput = QLineEdit()
        self.deptInput.setFixedSize(600, 60)
        self.deptInput.setText('请输入所在院系')
        self.deptInput.initText = '请输入所在院系'
        self.deptInput.setTextMargins(5, 5, 5, 5)
        self.deptInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                   deptInput)

        # 专业
        self.majorInput = QLineEdit()
        self.majorInput.setFixedSize(600, 60)
        self.majorInput.setText('请输入专业')
        self.majorInput.initText = '请输入专业'
        self.majorInput.setTextMargins(5, 5, 5, 5)
        self.majorInput.mousePressEvent = lambda x: self.inputClick(self.
                                                                    majorInput)

        # 提交
        self.submit = QToolButton()
        self.submit.setText('提交')
        self.submit.setFixedSize(600, 60)

        # 返回登录
        self.back = QToolButton()
        self.back.setText('返回登录')
        self.back.setFixedSize(600, 60)

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.addWidget(self.title)
        self.bodyLayout.addWidget(self.subTitle)
        self.bodyLayout.addWidget(self.accountInput)
        self.bodyLayout.addWidget(self.nameInput)
        self.bodyLayout.addWidget(self.passwordInput)
        self.bodyLayout.addWidget(self.repPasswordInput)
        self.bodyLayout.addWidget(self.deptInput)
        self.bodyLayout.addWidget(self.majorInput)
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
                e.setEchoMode(QLineEdit.Password)  # 黑点覆盖

    def initUI(self):
        self.setFixedSize(650, 700)
        self.setWindowTitle('注册')
        self.setMyStyle()

    def getInfo(self):
        for i in range(2, 8):
            item = self.bodyLayout.itemAt(i).widget()
            if item.text() == item.initText:
                item.setText('')

        info = {
            'SID': self.accountInput.text(),
            'PASSWORD': self.passwordInput.text(),
            'REPASSWORD': self.repPasswordInput.text(),
            'SNAME': self.nameInput.text(),
            'DEPARTMENT': self.deptInput.text(),
            'MAJOR': self.majorInput.text(),
            'PUNISHED': 0
        }
        return info

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        QLineEdit{
            border:0px;
            border-bottom: 1px solid rgba(229, 229, 229, 1);
            color: grey;
        }
        QToolButton{
            border:0;
            background-color:rgba(50, 198, 212, 1);
            color: white;
            font-size: 20px;
            font-family: Tahoma,Helvetica,Arial,'宋体',sans-serif;
        }
        QGroupBox{
            border: 1px solid rgba(229, 229, 229, 1);
            border-radius: 5px;
        }
        *{
            font-size: 25px;
        }
        ''')
        self.title.setStyleSheet('''
        *{
            color: rgba(113, 118, 121, 1);
            font-size: 45px;
            font-family: Tahoma,Helvetica,Arial,'宋体',sans-serif;
        }
        ''')
        self.subTitle.setStyleSheet('''
        *{
            color: rgba(184, 184, 184, 1);
            font-size: 30px;
        }
        ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Signup()
    ex.show()
    sys.exit(app.exec_())
