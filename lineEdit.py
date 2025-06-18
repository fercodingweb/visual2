from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(635, 477)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 591, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.ButtonSetText = QtWidgets.QPushButton(Form)
        self.ButtonSetText.setGeometry(QtCore.QRect(190, 160, 93, 28))
        self.ButtonSetText.setObjectName("ButtonSetText")
        self.ButtonSetText.clicked.connect(self.fungsiSetText)

        self.ButtonClear = QtWidgets.QPushButton(Form)
        self.ButtonClear.setGeometry(QtCore.QRect(40, 80, 93, 28))
        self.ButtonClear.setObjectName("ButtonClear")
        self.ButtonClear.clicked.connect(self.fungsiClear)

        self.ButtonCopy = QtWidgets.QPushButton(Form)
        self.ButtonCopy.setGeometry(QtCore.QRect(40, 120, 93, 28))
        self.ButtonCopy.setObjectName("ButtonCopy")
        self.ButtonCopy.clicked.connect(self.fungsiCopy)

        self.ButtonCut = QtWidgets.QPushButton(Form)
        self.ButtonCut.setGeometry(QtCore.QRect(40, 160, 93, 28))
        self.ButtonCut.setObjectName("ButtonCut")
        self.ButtonCut.clicked.connect(self.fungsiCut)

        self.ButtonPaste = QtWidgets.QPushButton(Form)
        self.ButtonPaste.setGeometry(QtCore.QRect(40, 200, 93, 28))
        self.ButtonPaste.setObjectName("ButtonPaste")
        self.ButtonPaste.clicked.connect(self.fungsiPaste)

        self.ButtonRedo = QtWidgets.QPushButton(Form)
        self.ButtonRedo.setGeometry(QtCore.QRect(190, 80, 93, 28))
        self.ButtonRedo.setObjectName("ButtonRedo")
        self.ButtonRedo.clicked.connect(self.fungsiRedo)

        self.ButtonUndo = QtWidgets.QPushButton(Form)
        self.ButtonUndo.setGeometry(QtCore.QRect(190, 200, 93, 28))
        self.ButtonUndo.setObjectName("ButtonUndo")
        self.ButtonUndo.clicked.connect(self.fungsiundo)
        
        self.ButtonSelectAll = QtWidgets.QPushButton(Form)
        self.ButtonSelectAll.setGeometry(QtCore.QRect(190, 120, 93, 28))
        self.ButtonSelectAll.setObjectName("ButtonSelectAll")
        self.ButtonSelectAll.clicked.connect(self.fungsiselectAll)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonSetText.setText(_translate("Form", "ButtonSetText"))
        self.ButtonClear.setText(_translate("Form", "ButtonClear"))
        self.ButtonCopy.setText(_translate("Form", "ButtonCopy"))
        self.ButtonCut.setText(_translate("Form", "ButtonCut"))
        self.ButtonPaste.setText(_translate("Form", "ButtonPaste"))
        self.ButtonRedo.setText(_translate("Form", "ButtonRedo"))
        self.ButtonUndo.setText(_translate("Form", "ButtonUndo"))
        self.ButtonSelectAll.setText(_translate("Form", "ButtonSelectAll"))

    def fungsiSetText(self):
        self.lineEdit.setText("Ini adalah teks yang ditetapkan")
    def fungsiClear(self):
        self.lineEdit.clear()
    def fungsiselectAll(self):
        self.lineEdit.selectAll()
    def fungsiCopy(self):
        self.lineEdit.copy()
    def fungsiCut(self):
        self.lineEdit.cut()
    def fungsiPaste(self):
        self.lineEdit.paste()
    def fungsiundo(self):
        self.lineEdit.undo()
    def fungsiRedo(self):
        self.lineEdit.redo()

if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())