# ...existing code...
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(698, 447)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 80, 113, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButtonlogin = QtWidgets.QPushButton(Form)
        self.pushButtonlogin.setGeometry(QtCore.QRect(30, 170, 93, 28))
        self.pushButtonlogin.setObjectName("pushButtonlogin")
        self.pushButton_2logout = QtWidgets.QPushButton(Form)
        self.pushButton_2logout.setGeometry(QtCore.QRect(220, 170, 93, 28))
        self.pushButton_2logout.setObjectName("pushButton_2logout")
        # Tambahkan label status
        self.label_status = QtWidgets.QLabel(Form)
        self.label_status.setGeometry(QtCore.QRect(30, 220, 300, 30))
        self.label_status.setObjectName("label_status")
        self.label_status.setText("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Koneksi tombol
        self.pushButtonlogin.clicked.connect(self.login)
        self.pushButton_2logout.clicked.connect(self.logout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "password"))
        self.pushButtonlogin.setText(_translate("Form", "login"))
        self.pushButton_2logout.setText(_translate("Form", "logout"))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == "admin" and password == "12345":
            self.label_status.setText("Login Berhasil")
        else:
            self.label_status.setText("username atau password salah")

    def logout(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label_status.setText("Logout Berhasil")
# ...existing code...

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets, QtCore
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
# ...existing code...