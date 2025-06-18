# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(120, 130, 171, 31))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(40, 90, 71, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(40, 140, 71, 20))
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(150, 190, 93, 28))
        self.login.setObjectName("login")
        self.label_status = QtWidgets.QLabel(Form)
        self.label_status.setGeometry(QtCore.QRect(120, 240, 200, 30))
        self.label_status.setObjectName("label_status")
        self.label_status.setText("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.login.clicked.connect(self.fungsilogin)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form Login"))
        self.username.setText(_translate("Form", "Username"))
        self.password.setText(_translate("Form", "Password"))
        self.login.setText(_translate("Form", "Login"))

    def fungsilogin(self):
        username = self.lineEdit.text()
        password = self.lineEdit_password.text()
        if username == "admin" and password == "123":
            self.label_status.setText("Login Berhasil")
        else:
            self.label_status.setText("Login Gagal")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())