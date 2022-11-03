from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys

class App(QWidget):

    def __init__(self):
        self.start()
        self.button()

    def start(self):
        self.main_menu = uic.loadUi("mainmanu.ui")
        self.main_menu.show()

    def click_lit(self,day_or_night,count):
        self.vivod_lit = uic.loadUi("lit.ui")
        self.vivod_lit.show()
        self.vivod_lit.textBrowser.setText("замес номер {}".format(count))

    def lit_button(self):
        self.menu_lit = uic.loadUi("menu_lit.ui")
        self.menu_lit.show()
        self.menu_lit.pushButton.clicked.connect(lambda: self.click_lit(self.menu_lit.comboBox.currentText(),self.menu_lit.comboBox_2.currentText()))

    def click_tonn(self,line,proiz,weight,num_beg):

        self.vivod_tonn = uic.loadUi("tonn.ui")
        self.vivod_tonn.show()
        self.vivod_tonn.textBrowser.setText("Номер бега {} будет готов в {}".format(num_beg,123))

    def tonn_button(self):
        self.menu_tonn = uic.loadUi("menu_tonn.ui")
        self.menu_tonn.show()
        self.menu_tonn.pushButton.clicked.connect(lambda: self.click_tonn(self.menu_tonn.comboBox_2.currentText(),self.menu_tonn.lineEdit.text(),self.menu_tonn.lineEdit_2.text(),self.menu_tonn.comboBox_3.currentText()))

    def bunk_button(self):
        # self.menu_bunk = uic.loadUi("menu_tonn.ui")
        # self.menu_bunk.show()
        pass

    def button(self):
        self.main_menu.pushButton_4.clicked.connect(lambda: self.lit_button())
        self.main_menu.pushButton_3.clicked.connect(lambda: self.tonn_button())
        self.main_menu.pushButton_5.clicked.connect(lambda: self.bunk_button())

if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
