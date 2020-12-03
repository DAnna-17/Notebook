from window21 import Window2
import sys
import csv
import sqlite3
from dialog1 import Dialog
from errors import SameThemeError, SameNameError

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example1(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.initUI()

    #ui файл
    def setupUi(self):
        self.setStyleSheet("background-color: rgb(221, 215, 255);")
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(QRect(0, 90, 391, 291))
        self.scrollArea.setStyleSheet("background-color: rgb(221, 215, 255);")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 374, 291))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pbn = QPushButton(self)
        self.pbn.setGeometry(QRect(320, 10, 75, 31))
        self.pbn.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.pbn.setObjectName("pbn")
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(40, 50, 141, 31))
        self.comboBox.setStyleSheet("background-color: rgb(194, 240, 241);")
        self.comboBox.setObjectName("comboBox")
        self.pbn_2 = QPushButton(self)
        self.pbn_2.setGeometry(QRect(230, 10, 75, 31))
        self.pbn_2.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.pbn_2.setObjectName("pbn_2")
        self.pbn_add = QPushButton(self)
        self.pbn_add.setGeometry(QRect(230, 50, 161, 31))
        self.pbn_add.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.pbn_add.setAutoRepeat(False)
        self.pbn_add.setObjectName("pbn_add")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(10, 10, 211, 31))
        self.label.setObjectName("label")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pbn.setText(_translate("Form", "Создать"))
        self.pbn_2.setText(_translate("Form", "Обновить"))
        self.pbn_add.setText(_translate("Form", "Добавить тему"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Выберете тему:</span></p></body></html>"))


    def initUI(self):
        y, x = QDesktopWidget().availableGeometry().height(), QDesktopWidget().availableGeometry().width()
        self.setGeometry(x // 2 - 200, y // 2 - 186, 400, 392)
        self.setWindowTitle('Заметки')

        self.pbn.clicked.connect(self.addButton)
        self.pbn_2.clicked.connect(self.place_button)
        self.pbn_add.clicked.connect(self.theme_add)

        self.place_themes()
        self.place_button()

        self.show()

    #расположение тем в crollbox
    def place_themes(self):
        with open('themes.txt', encoding="utf8") as f:
            themes = f.read().split(';')
        self.comboBox.addItems(themes[0:2])
        self.comboBox.addItems(themes[3:])

    #добавление новой темы с помощью кнопки
    def theme_add(self):
        try:
            text, ok = QInputDialog.getText(self, 'Новая тема', 'Введите тему:')

            if ok:
                with open('themes.txt', encoding="utf-8") as f:
                    themes = f.read().split(';')
                if text in themes:
                    raise SameThemeError()
                themes.append(text)
                with open('themes.txt', 'w', encoding="utf-8") as f:
                    f.write(';'.join(themes))

                self.comboBox.addItem(text)
        except SameThemeError as error:
            a = 'Такая тема уже существует'
            ret = QMessageBox.warning(self, 'MessageBox', a, QMessageBox.Yes)

    #распологаем кнопки на гланом окне
    def place_button(self):
        self.layout1 = QFormLayout(self)
        #чтобы кнопки не тянулись
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.con = sqlite3.connect("files.sqlite")
        cur = self.con.cursor()

        self.theme = self.comboBox.currentText()

        if self.theme == 'всё':
            result = cur.execute("SELECT * FROM файлы").fetchall()
        else:
            result = cur.execute("""SELECT * FROM файлы WHERE тема = '{}'""".format(self.theme)).fetchall()

        self.con.close()

        result = sorted(result, key=lambda x: -x[3])

        for n, i in enumerate(result):
            if i == []:
                continue
            self.btn = QPushButton(self)
            self.line = QLabel(self)
            self.btn_del = QPushButton(self)
            self.btn_del.setText(str(i[0]))
            self.line.setText(' '.join([str(i) for i in i[1:3]]))
            #добавляю невидимый номер для определения какая кнопка была нажата
            self.btn.setText(str(i[0]))
            self.btn.clicked.connect(self.run)
            self.btn_del.clicked.connect(self.delete)

            #задаю размер
            self.line.setMinimumSize(280, 25)
            self.btn_del.setMinimumSize(30, 25)
            self.btn.setMinimumSize(30, 25)
            self.btn_del.setMaximumSize(30, 25)
            self.btn.setMaximumSize(30, 25)
            self.btn.setStyleSheet('QPushButton {background-color: rgb(228, 196, 255); color: rgb(247, 201, 255);}')
            self.btn_del.setStyleSheet('QPushButton {background-color: rgb(228, 196, 255); color: rgb(247, 201, 255);}')

            # чтобы кнопки не тянулись
            sizePolicy.setHeightForWidth(self.btn.sizePolicy().hasHeightForWidth())
            self.btn.setSizePolicy(sizePolicy)
            sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
            self.btn_del.setSizePolicy(sizePolicy)

            #добавляю иконки
            self.btn.setIcon(QIcon('image.png'))
            self.btn.setIconSize(QSize(40, 35))
            self.btn_del.setIcon(QIcon('image1.png'))
            self.btn_del.setIconSize(QSize(25, 20))

            #добавляю всё в layout
            self.layout = QHBoxLayout(self)
            self.layout.setSpacing(10)
            self.layout.addWidget(self.btn)
            self.layout.addWidget(self.btn_del)
            self.layout1.addRow(self.line, self.layout)

        w = QWidget()
        w.setLayout(self.layout1)
        self.scrollArea.setWidget(w)

    #добавление записи в базу
    def add_file(self, n, nname, theme):
        self.con = sqlite3.connect("files.sqlite")
        cur = self.con.cursor()
        n += 1
        print(n)
        cur.execute("INSERT INTO файлы VALUES (?, ?, ?, ?)", (n, str(nname), str(theme), 0)).fetchall()

        self.con.commit()
        self.con.close()

    #получение значений из диалогового окна(отдельная функци нужна для добавления аргумента)
    def findValues(self):
        self.d.findValues(self)

    #создание файла с заметкой, сначала создаётся пустым
    def create_file(self, n):
        f = open(str(n + 1) + '.txt', 'w', encoding="utf-8")
        f.write('')
        f.close()

    #вызов окна, для создания заметки
    def addButton(self):
        self.d = Dialog(self)

    #добавление файла в базу и кнопки на главное окно
    def addButton2(self):
        self.con = sqlite3.connect("files.sqlite")
        cur = self.con.cursor()
        self.name, self.tame = self.d.getValues()
        n = len(cur.execute('SELECT * FROM файлы WHERE id > 0').fetchall())
        self.create_file(n)
        #файл
        self.add_file(n, self.name, self.tame)
        #кнопка
        self.place_button()

        self.con.close()

    #открываем окно редактирования
    def run(self):

        sender = self.sender()

        self.w2 = Window2(sender.text(), self)
        self.w2.show()
        self.place_button()

    #удаление файла
    def delete(self):
        sender = self.sender().text()
        a = 'Вы точно хотите удалить файл?'
        ret = QMessageBox.question(self, 'MessageBox', a, QMessageBox.Yes | QMessageBox.No)

        if ret == QMessageBox.Yes:
            self.con = sqlite3.connect("files.sqlite")
            cur = self.con.cursor()
            cur.execute('DELETE FROM файлы WHERE id = {}'.format(sender))
            self.con.commit()

            self.con.close()

            self.place_button()




def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example1()
    ex.show()
    sys.exit(app.exec())