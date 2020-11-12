#QDateEdit和QTimeEdit控件使用
from PyQt5.QtWidgets import QDateEdit,QDateTimeEdit,QTimeEdit, QCalendarWidget, QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon,QPixmap,QFont
from PyQt5.QtCore import  QDate

import sys

class WindowClass(QWidget):

    def __init__(self,parent=None):

        super(WindowClass, self).__init__(parent)
        self.btn=QPushButton(self)#self参数则让该按钮显示当前窗体中
        self.btn.setText("点击获取日期信息")
        self.btn.clicked.connect(self.showdate)

        self.dateEdit=QDateEdit(self)
        self.timeEdit=QTimeEdit(self)
        self.dateTimeEdit=QDateTimeEdit(self)
        self.dateEdit.setCalendarPopup(True)
        #self.timeEdit.setCalendarPopup(True)#弹出界面是失效的注意；
        #self.dateTimeEdit.setCalendarPopup(True)#时间是无法选择的
        self.dateEdit.move(10,200)
        self.timeEdit.move(10,100)
        self.dateTimeEdit.move(10,300)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.timeEdit.setDisplayFormat("HH:mm:ss")
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.setWindowTitle("QDateEdit和QDateTimeEdit控件使用")

    def showdate(self):
        print(self.dateEdit.text())

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowClass()
    win.show()
    sys.exit(app.exec_())