import sys
import csv
import sqlite3

from errors import SameNameError

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic



class Window2(QWidget):
    def __init__(self, n, widg):
        super().__init__()
        self.setupUi()

        self.n = n
        self.widg = widg
        self.initUI()

    def setupUi(self):
        Form = self
        Form.setStyleSheet("background-color: rgb(221, 215, 255);")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setGeometry(QRect(10, 133, 461, 291))
        self.textEdit.setStyleSheet("background-color: rgb(194, 240, 241);")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QRect(80, 10, 221, 31))
        self.lineEdit.setFocusPolicy(Qt.TabFocus)
        self.lineEdit.setStyleSheet("background-color: rgb(194, 240, 241);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.pbn = QPushButton(Form)
        self.pbn.setGeometry(QRect(310, 10, 81, 71))
        self.pbn.setFocusPolicy(Qt.TabFocus)
        self.pbn.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.pbn.setObjectName("pbn")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setGeometry(QRect(80, 50, 221, 31))
        self.lineEdit_2.setFocusPolicy(Qt.TabFocus)
        self.lineEdit_2.setStyleSheet("background-color: rgb(194, 240, 241);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pbn_del = QPushButton(Form)
        self.pbn_del.setGeometry(QRect(400, 10, 75, 71))
        self.pbn_del.setFocusPolicy(Qt.TabFocus)
        self.pbn_del.setToolTip("")
        self.pbn_del.setToolTipDuration(0)
        self.pbn_del.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.pbn_del.setObjectName("pbn_del")
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QRect(10, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pbn_txt = QPushButton(Form)
        self.pbn_txt.setGeometry(QRect(370, 90, 101, 31))
        self.pbn_txt.setFocusPolicy(Qt.NoFocus)
        self.pbn_txt.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.pbn_txt.setObjectName("pbn_txt")
        self.pbn_bold = QPushButton(Form)
        self.pbn_bold.setGeometry(QRect(330, 90, 31, 21))
        self.pbn_bold.setStyleSheet("background-color: rgb(206, 253, 255);")
        self.pbn_bold.setObjectName("pbn_bold")
        self.pbn_ital = QPushButton(Form)
        self.pbn_ital.setGeometry(QRect(290, 90, 31, 21))
        self.pbn_ital.setStyleSheet("background-color: rgb(206, 253, 255);")
        self.pbn_ital.setObjectName("pbn_ital")
        self.pbn_line = QPushButton(Form)
        self.pbn_line.setGeometry(QRect(250, 90, 31, 21))
        self.pbn_line.setStyleSheet("background-color: rgb(206, 253, 255);")
        self.pbn_line.setObjectName("pbn_line")
        self.spinBox = QSpinBox(Form)
        self.spinBox.setGeometry(QRect(10, 90, 41, 31))
        self.spinBox.setStyleSheet("background-color: rgb(194, 240, 241);")
        self.spinBox.setObjectName("spinBox")
        self.pbn_size = QPushButton(Form)
        self.pbn_size.setGeometry(QRect(60, 90, 31, 31))
        self.pbn_size.setStyleSheet("background-color: rgb(228, 196, 255);")
        self.pbn_size.setText("")
        self.pbn_size.setObjectName("pbn_size")
        self.pbn_ital_off = QPushButton(Form)
        self.pbn_ital_off.setGeometry(QRect(290, 110, 31, 16))
        self.pbn_ital_off.setStyleSheet("background-color: rgb(255, 203, 206);")
        self.pbn_ital_off.setText("")
        self.pbn_ital_off.setObjectName("pbn_ital_off")
        self.pbn_line_off = QPushButton(Form)
        self.pbn_line_off.setGeometry(QRect(250, 110, 31, 16))
        self.pbn_line_off.setStyleSheet("background-color: rgb(255, 203, 206);")
        self.pbn_line_off.setText("")
        self.pbn_line_off.setObjectName("pbn_line_off")
        self.pbn_bold_off = QPushButton(Form)
        self.pbn_bold_off.setGeometry(QRect(330, 110, 31, 16))
        self.pbn_bold_off.setStyleSheet("background-color: rgb(255, 203, 206);")
        self.pbn_bold_off.setText("")
        self.pbn_bold_off.setObjectName("pbn_bold_off")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setPlaceholderText(_translate("Form", "Что-то"))
        self.pbn.setText(_translate("Form", "Сохранить"))
        self.pbn_del.setText(_translate("Form", "Закрыть"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Название</span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Тема</span></p></body></html>"))
        self.pbn_txt.setWhatsThis(_translate("Form",
                                             "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic; text-decoration: underline;\">изменить стиль</span></p></body></html>"))
        self.pbn_txt.setText(_translate("Form", "изменить стиль"))
        self.pbn_bold.setText(_translate("Form", "bold"))
        self.pbn_ital.setText(_translate("Form", "italic"))
        self.pbn_line.setWhatsThis(_translate("Form",
                                              "<html><head/><body><p><span style=\" text-decoration: underline;\">a</span></p></body></html>"))
        self.pbn_line.setText(_translate("Form", "_"))

    def initUI(self):
        y, x = QDesktopWidget().availableGeometry().height(), QDesktopWidget().availableGeometry().width()
        self.setGeometry(x // 2 - 242, y // 2 - 217, 484, 434)

        self.con = sqlite3.connect("files.sqlite")
        cur = self.con.cursor()

        #определяем название и тему
        self.name = cur.execute("SELECT имя FROM файлы WHERE id = ?", (self.n)).fetchall()[0][0]
        self.theme = cur.execute("SELECT тема FROM файлы WHERE id = ?", (self.n)).fetchall()[0][0]
        self.counter = cur.execute("SELECT колво FROM файлы WHERE id = ?", (self.n)).fetchall()[0][0]
        cur.execute("UPDATE файлы SET колво = ? WHERE id = ?", (int(self.counter) + 1, self.n)).fetchall()
        self.con.commit()
        self.con.close()
        self.setWindowTitle(self.name)

        self.lineEdit.setText(str(self.name))
        self.lineEdit_2.setText(str(self.theme))
        with open(str(self.n) + '.txt', 'r', encoding="utf-8") as f:
            text = f.read()
        self.textEdit.setText(text)

        #подключение функций
        self.pbn.clicked.connect(self.run)
        self.pbn_del.clicked.connect(self.delete)
        self.pbn_txt.clicked.connect(self.edit_text)
        self.pbn_bold.clicked.connect(self.make_bold)
        self.pbn_bold_off.clicked.connect(self.make_bold_off)
        self.pbn_ital.clicked.connect(self.make_italic)
        self.pbn_ital_off.clicked.connect(self.make_italic_off)
        self.pbn_line.clicked.connect(self.make_line)
        self.pbn_line_off.clicked.connect(self.make_line_off)
        self.pbn_size.clicked.connect(self.change_size)

        self.show()

    #сохранение заметки
    def run(self):
        try:
            self.con = sqlite3.connect("files.sqlite")
            cur = self.con.cursor()
            name = self.lineEdit.text()
            cond1 = (name, ) in cur.execute('SELECT имя FROM файлы WHERE id > 0').fetchall()
            cond3 = ([(int(self.n), )] == cur.execute('SELECT id FROM файлы WHERE имя = "{}"'.format(name)).fetchall())

            if cond1 and not cond3:
                raise SameNameError

            cur.execute("UPDATE файлы SET имя = ? WHERE id = ?", (name, self.n)).fetchall()
            cur.execute("UPDATE файлы SET тема = ? WHERE id = ?", (self.lineEdit_2.text(), self.n)).fetchall()

            self.con.commit()
            self.con.close()

            f = open(self.n + '.txt', 'w', encoding='utf-8')
            f.write(self.textEdit.document().toHtml())
            f.close()

            self.widg.place_button()

        except SameNameError:
            a = 'Такое имя уже существует. Выберете другое.'
            ret = QMessageBox.warning(self, 'MessageBox', a, QMessageBox.Yes)

        except UnicodeEncodeError:
            a = 'Символов которые вы ввели нет в кодировке utf-8'
            ret = QMessageBox.warning(self, 'MessageBox', a, QMessageBox.Yes)


    #закрытие файла
    def delete(self):
        self.close()

    #всякие разные стили
    def make_bold(self):
        #тут приходится создавать отдельный объект font из-за того, что функции setfontBold почему-то не существует...
        style = QTextCharFormat()
        font = style.font()
        font.setBold(True)
        style.setFont(font)
        if (self.cursor().hasSelection()):
            self.cursor().mergeCharFormat(style)

    # _off это отключение стиля
    def make_bold_off(self):
        style = QTextCharFormat()
        font = style.font()
        font.setBold(False)
        style.setFont(font)
        if (self.cursor().hasSelection()):
            self.cursor().mergeCharFormat(style)

    # а функция setFontItalic есть...
    def make_italic(self):
        if (self.cursor().hasSelection()):
            print(self.textEdit.document().toHtml())
            style = QTextCharFormat()
            font = style.font()
            style.setFontItalic(True)
            self.cursor().mergeCharFormat(style)
        print(self.textEdit.document().toHtml())


    def make_italic_off(self):
        style = QTextCharFormat()
        font = style.font()
        style.setFontItalic(False)
        if (self.cursor().hasSelection()):
            self.cursor().mergeCharFormat(style)

    # и функция setFontUnderline
    def make_line(self):
        style = QTextCharFormat()
        font = style.font()
        style.setFontUnderline(True)
        if (self.cursor().hasSelection()):
            self.cursor().mergeCharFormat(style)

    def make_line_off(self):
        style = QTextCharFormat()
        font = style.font()
        style.setFontUnderline(False)
        if (self.cursor().hasSelection()):
            self.cursor().mergeCharFormat(style)

    # изменение размера
    def change_size(self):
        style = QTextCharFormat()
        size = self.spinBox.value()
        style.setFontPointSize(size)
        if (self.cursor().hasSelection()):
            self.cursor().mergeCharFormat(style)

    # редактирование текста
    def edit_text(self):
        font, ok = QFontDialog.getFont()
        style = QTextCharFormat()
        style.setFont(font)
        if (self.cursor().hasSelection()):
            self.cursor().mergeCharFormat(style)
        elif ok:
             self.textEdit.setFont(font)


    # функции для определения положения курсора курсора
    def cursor(self):
        return self.textEdit.textCursor()

    def set_text_cursor_pos(self, value):
        tc = self.cursor()
        tc.setPosition(value, QTextCursor.KeepAnchor)
        self.textEdit.setTextCursor(tc)


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
    ex = Example()
    ex.show()
    sys.exit(app.exec())