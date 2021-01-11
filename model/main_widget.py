import sys
sys.path.append('./')
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from model import login
from model import signup
from model import database
from model import student
from model import administrator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setLogin()

        self.setGeometry(200, 200, 1920, 1080)
        #self.setFixedSize(1280, 720)
        self.setMinimumSize(1920, 1080)
        self.setMyStyle()

    # 创建登录菜单
    def setLogin(self):
        self.login = login.Login()
        self.login.setParent(self)
        self.login.move(480, 120)
        self.login.loginButton.clicked.connect(self.loginFunction)
        self.login.signup.clicked.connect(self.signupViewFunction)

    # 创建注册菜单
    def setSignup(self):
        self.signup = signup.Signup()
        self.signup.setParent(self)
        self.signup.setVisible(True)
        self.signup.move(680, 190)
        self.signup.back.clicked.connect(self.backToLogin)
        self.signup.submit.clicked.connect(self.signupFunction)

    # 登录按钮按下
    def loginFunction(self):
        user_mes = {
            'ID': self.login.accountInput.text(),
            'PASSWORD': database.encrypt(self.login.passwordInput.text())
        }
        if self.login.accountInput.text() == '':
            self.errorBox('用户名不能为空！')
            return
        if self.login.passwordInput.text() == '':
            self.errorBox('密码不能为空！')
            return
        if len(self.login.accountInput.text()) > 15:
            self.errorBox('用户名不能大于15位')
            return
        for i in range(len(self.login.accountInput.text())):
            if not self.login.accountInput.text()[i].isalpha(
            ) and not self.login.accountInput.text()[i].isdigit(
            ) and self.login.accountInput.text()[i] != '_':
                self.errorBox('用户名只能为字母、数字或下划线')
                return
        self.user = database.signin(user_mes)
        if self.user is None:
            self.errorBox('不存在此用户！')
        else:
            if self.user['PASSWORD'] != user_mes['PASSWORD']:
                self.errorBox('密码错误！')
            else:
                self.login.setVisible(False)
                self.display()

    # 显示注册界面
    def signupViewFunction(self):
        self.login.setVisible(False)
        self.setSignup()

    # 注册按钮按下
    def signupFunction(self):
        '''
        获取信息后先检查
        加密密码
        '''
        self.user = self.signup.getInfo()
        res = database.check_user_info(self.user)
        if res['res'] == 'fail':
            self.errorBox(res['reason'])
            return
        self.user['PASSWORD'] = database.encrypt(self.user['PASSWORD'])
        self.user['REPASSWORD'] = database.encrypt(self.user['REPASSWORD'])
        ans = database.signup(self.user)
        if ans == '用户已存在':
            self.errorBox('用户已存在')
            return
        self.user['class'] = 'stu'
        self.user.pop('PASSWORD')
        if ans:
            self.signup.setVisible(False)
            print('成功')
            self.display()
        else:
            self.errorBox('注册失败')

    def backToLogin(self):
        self.signup.setVisible(False)
        self.login.setVisible(True)

    def logout(self):
        self.body.close()
        self.login.setVisible(True)

    def display(self):
        # 显示学生信息
        if self.user['class'] == 'stu':
            self.body = student.StudentPage(self.user)
            self.body.setParent(self)
            self.body.setVisible(True)
            self.body.out.clicked.connect(self.logout)
        else:
            self.body = administrator.AdministratorPage(self.user)
            self.body.setParent(self)
            self.body.setVisible(True)
            self.body.out.clicked.connect(self.logout)

    def errorBox(self, mes: str):
        msgBox = QMessageBox(
            QMessageBox.Warning,
            "警告!",
            mes,
            QMessageBox.NoButton,
        )
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.exec_()

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
