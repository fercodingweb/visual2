# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(792, 545)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 101, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 100, 101, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 180, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 180, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 230, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.labelBilanganpertama = QtWidgets.QLabel(Form)
        self.labelBilanganpertama.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.labelBilanganpertama.setObjectName("labelBilanganpertama")
        self.label_2BilanganKedua = QtWidgets.QLabel(Form)
        self.label_2BilanganKedua.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_2BilanganKedua.setObjectName("label_2BilanganKedua")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 140, 200, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Tambahkan koneksi tombol ke fungsi operasi
        self.pushButton_3.clicked.connect(self.penjumlahan)
        self.pushButton.clicked.connect(self.pengurangan)
        self.pushButton_2.clicked.connect(self.perkalian)
        self.pushButton_4.clicked.connect(self.pembagian)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Pengurangan"))
        self.pushButton_2.setText(_translate("Form", "Perkalian"))
        self.pushButton_3.setText(_translate("Form", "Penjumlahan"))
        self.pushButton_4.setText(_translate("Form", "Pembagian"))
        self.labelBilanganpertama.setText(_translate("Form", "Bilangan Pertama"))
        self.label_2BilanganKedua.setText(_translate("Form", "Bilangan Kedua"))
        self.label.setText(_translate("Form", "Hasil"))

    def penjumlahan(self):
        try:
            a = float(self.lineEdit.text())
            b = float(self.lineEdit_2.text())
            hasil = a + b
            self.label.setText(f"Hasil: {hasil}")
        except ValueError:
            self.label.setText("Input tidak valid!")

    def pengurangan(self):
        try:
            a = float(self.lineEdit.text())
            b = float(self.lineEdit_2.text())
            hasil = a - b
            self.label.setText(f"Hasil: {hasil}")
        except ValueError:
            self.label.setText("Input tidak valid!")

    def perkalian(self):
        try:
            a = float(self.lineEdit.text())
            b = float(self.lineEdit_2.text())
            hasil = a * b
            self.label.setText(f"Hasil: {hasil}")
        except ValueError:
            self.label.setText("Input tidak valid!")

    def pembagian(self):
        try:
            a = float(self.lineEdit.text())
            b = float(self.lineEdit_2.text())
            if b == 0:
                self.label.setText("Tidak bisa dibagi 0!")
            else:
                hasil = a / b
                self.label.setText(f"Hasil: {hasil}")
        except ValueError:
            self.label.setText("Input tidak valid!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())