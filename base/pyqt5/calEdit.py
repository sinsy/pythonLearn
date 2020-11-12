#QCalendar日历控件使用
from PyQt5.QtWidgets import QCalendarWidget, QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon,QPixmap,QFont


import sys

class WindowClass(QWidget):

    def __init__(self,parent=None):

        super(WindowClass, self).__init__(parent)
        self.btn=QPushButton(self)#self参数则让该按钮显示当前窗体中
        self.btn.setText("选择日期")
        self.btn.move(0,0)
        self.btn.clicked.connect(self.openCalendar)
        self.le=QLabel(self)
        self.cal=QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(2017,1,1))#设置日期最小范围
        self.cal.setMaximumDate(QDate(2019,12,30))#设置日期最大范围
        self.cal.setGridVisible(True)#是否显示日期之间的网格
        self.cal.move(5,30)
        self.cal.hide()#隐藏日期控件
        self.cal.clicked[QDate].connect(self.showDate)#clicked[参数]，即定义showDate是传入的参数类型设置
        date=self.cal.selectedDate()#获取选中日期，默认当前系统时间
        self.le.setText(date.toString('yyyy-MM-dd dddd'))
        self.le.move(100,8)
        self.setGeometry(100,100,400,350)#设置当前窗体位置和大小
        self.setWindowTitle("日历控件使用")

    def showDate(self,date):
        self.le.setText(date.toString("yyyy-MM-dd dddd"))
        self.cal.close()#关闭日期控件
    def openCalendar(self):
        self.cal.show()#显示日期控件

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowClass()
    win.show()
    sys.exit(app.exec_())