# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pythonProject\Pyqt5\menu_tonn.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(265, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 40, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 240, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 270, 161, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тонн за смену"))
        self.label.setText(_translate("MainWindow", "Какая линия?"))
        self.label_2.setText(_translate("MainWindow", "Сколько в биг-бэге"))
        self.label_3.setText(_translate("MainWindow", "Какая производительность?"))
        self.label_4.setText(_translate("MainWindow", "Какой № биг-бэга"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "60"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "61"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox_3.setItemText(19, _translate("MainWindow", "20"))
        self.pushButton.setText(_translate("MainWindow", "Ввод"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())