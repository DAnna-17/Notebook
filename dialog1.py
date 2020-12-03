from window21 import Window2
from errors import SameThemeError
import sys

from PyQt5.QtWidgets import *
from  PyQt5 import QtCore
from PyQt5 import uic


class Dialog(QDialog):
    def __init__(self, widg):
        self.widg = widg
        super().__init__()
        self.setupUi()
        self.initUI()

    def setupUi(self):
        Dialog = self
        Dialog.setStyleSheet("background-color: rgb(221, 215, 255);")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 120, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 221, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(194, 240, 241);")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 80, 221, 22))
        self.comboBox.setStyleSheet("background-color: rgb(194, 240, 241);")
        self.comboBox.setObjectName("comboBox")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 81, 131, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Введите название:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Выберете тему:</span></p></body></html>"))

    def initUI(self):
        y, x = QDesktopWidget().availableGeometry().height(), QDesktopWidget().availableGeometry().width()
        self.setGeometry(x // 2 - 188, y // 2 - 94, 376, 188)
        self.setWindowTitle('Новая заметкаю')

        self.buttonBox.accepted.connect(self.findValues)

        with open('themes.txt', encoding="utf8") as f:
            themes = f.read().split(';')
        self.comboBox.addItems(themes[1:])

        self.show()

    #получение значений
    def findValues(self):
        self.name = self.lineEdit.text()
        self.theme = self.comboBox.currentText()

        try:
            #добавление новой темы из окна создание заметки
            if self.theme == 'Новая тема':
                self.theme, ok = QInputDialog.getText(self, 'Новая тема', 'Введите тему:')
                with open('themes.txt', encoding="utf-8") as f:
                    themes = f.read().split(';')
                if self.theme in themes:
                    raise SameThemeError()
                themes.append(self.theme)
                with open('themes.txt', 'w', encoding="utf-8") as f:
                    f.write(';'.join(themes))
                self.widg.comboBox.addItem(self.theme)
        #есди такая тема уже существует
        except SameThemeError as error:
            a = 'Такая тема уже существует'
            ret = QMessageBox.warning(self, 'MessageBox', a, QMessageBox.Yes)


        self.widg.addButton2()

    #вызывается из главного окна
    def getValues(self):
        return (self.name, self.theme)

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QtWidget.QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example1()
    ex.show()
    sys.exit(app.exec())