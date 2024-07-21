from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

from list_themes import *
from Week_fun import *


# from Week import *

class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Week.ui')
        self.ui.lineEdit_1.textChanged.connect(self.handleCalc)
        self.ui.lineEdit_2.textChanged.connect(self.handleCalc)
        self.ui.lineEdit_3.textChanged.connect(self.handleCalc)

    def handleCalc(self):
        self.ui.lineEdit_4.clear()
        y = int(self.ui.lineEdit_1.text())
        m = int(self.ui.lineEdit_2.text())
        d = int(self.ui.lineEdit_3.text())
        out = str(week(y, m, d))
        self.ui.lineEdit_4.setText(out)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[18], extra=extra, invert_secondary=True)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
