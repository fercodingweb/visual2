import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox, QDateEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QGroupBox
)
from PyQt5.QtCore import QDate


class FormInput(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Input Sederhana")
        self.initUI()

    def initUI(self):
        # --- Form Input ---
        form_group = QGroupBox("Input Form")

        self.name_input = QLineEdit()
        self.gender_input = QComboBox()
        self.gender_input.addItems(["Laki-laki", "Perempuan"])
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()

        save_btn = QPushButton("Save")
        delete_btn = QPushButton("Delete")

        save_btn.clicked.connect(self.save_data)
        delete_btn.clicked.connect(self.delete_data)

        form_layout = QVBoxLayout()
        form_layout.addLayout(self.hbox("Name:", self.name_input))
        form_layout.addLayout(self.hbox("Gender:", self.gender_input))
        form_layout.addLayout(self.hbox("Date of Birth:", self.date_input))
        form_layout.addLayout(self.hbox("Phone Number:", self.phone_input))
        form_layout.addLayout(self.hbox("Email:", self.email_input))
        form_layout.addLayout(self.hbox("", save_btn, delete_btn))

        form_group.setLayout(form_layout)

        # --- Table ---
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Gender", "Date of Birth", "Phone Number", "Email"])

        # --- Main Layout ---
        main_layout = QVBoxLayout()
        main_layout.addWidget(form_group)
        main_layout.addWidget(QLabel("Data Table"))
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    def hbox(self, label_text, *widgets):
        layout = QHBoxLayout()
        if label_text:
            layout.addWidget(QLabel(label_text))
        for widget in widgets:
            layout.addWidget(widget)
        return layout

    def save_data(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.name_input.text()))
        self.table.setItem(row, 1, QTableWidgetItem(self.gender_input.currentText()))
        self.table.setItem(row, 2, QTableWidgetItem(self.date_input.date().toString("yyyy-MM-dd")))
        self.table.setItem(row, 3, QTableWidgetItem(self.phone_input.text()))
        self.table.setItem(row, 4, QTableWidgetItem(self.email_input.text()))

        # Clear input
        self.name_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.date_input.setDate(QDate.currentDate())
        self.phone_input.clear()
        self.email_input.clear()

    def delete_data(self):
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormInput()
    window.show()
    sys.exit(app.exec_())