from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import random
import datetime
class App(QWidget):

    def __init__(self):
        self.start()
        self.button()

    def start(self):
        self.main_menu = uic.loadUi("mainmanu.ui")
        self.main_menu.show()

    def click_lit(self,day_or_night,count):
        self.lit_time = {
            6: [75, 80],
            7: [60, 65],
            8: [50, 60],
            9: [42, 48],
            10: [37, 42],

        }

        self.vivod_lit = uic.loadUi("lit.ui")

        num = int(count)

        if day_or_night == 'День':
            self.date = datetime.datetime(2022, 11, 11, 7, 00)

        else:
            self.date = datetime.datetime(2022, 11, 11, 19, 00)

        self.vivod_lit.textBrowser.setText("Начало работы")
        self.vivod_lit.show()

        for i in range(1,num + 1):
            self.date += datetime.timedelta(minutes=20)
            self.vivod_lit.textBrowser.append("Замес №{} засыпал добавки: {}  ".format(i, self.date.strftime("%H:%M")))
            if i == 4:
                self.date += datetime.timedelta(minutes=60)
                self.vivod_lit.textBrowser.append("Обед")

            self.date += datetime.timedelta(minutes=random.randint(self.lit_time[num][0], self.lit_time[num][1]))
            self.vivod_lit.textBrowser.append("Почистил бочку {}".format(self.date.strftime("%H:%M")))

    def lit_button(self):
        self.menu_lit = uic.loadUi("menu_lit.ui")
        self.menu_lit.show()
        self.menu_lit.pushButton.clicked.connect(lambda: self.click_lit(self.menu_lit.comboBox.currentText(),self.menu_lit.comboBox_2.currentText()))

    def click_tonn(self,line,proiz,weight,num_beg,ob_beg):

        self.vivod_tonn = uic.loadUi("tonn.ui")
        self.vivod_tonn.show()

        date = datetime.datetime.now()
        line = int(line)
        proizvod = int(proiz)
        weight_beg = int(weight)
        num_beg = int(num_beg)
        ob_beg = int(ob_beg)
        if line == 60:
            proizvod += proizvod * 4.5 / 100

        for i in range(num_beg, 20):
            if i == num_beg:
                tonn_in_min = round((ob_beg - weight_beg) / (proizvod / 60), 2)
                self.vivod_tonn.textBrowser.setText("Эту тонну нужно добить осталось {} минут(а)".format(round(tonn_in_min)))
            else:
                tonn_in_min = round(ob_beg / (proizvod / 60), 2)
            date += datetime.timedelta(minutes=tonn_in_min)
            self.vivod_tonn.textBrowser.append("{} тонна будет готова в {}".format(i, date.strftime("%d.%m %H:%M")))

    def tonn_button(self):
        self.menu_tonn = uic.loadUi("menu_tonn.ui")
        self.menu_tonn.show()
        self.menu_tonn.pushButton.clicked.connect(lambda: self.click_tonn(self.menu_tonn.comboBox_2.currentText(),self.menu_tonn.lineEdit.text(),self.menu_tonn.lineEdit_2.text(),self.menu_tonn.comboBox_3.currentText(),self.menu_tonn.comboBox.currentText()))

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
