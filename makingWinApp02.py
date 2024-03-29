# 여기서 부터 line 9까지
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # Qt Designer에서 제작한 ui 모듈 불러옴

form_class = uic.loadUiType("ui/first240329.ui")[0]  # Qt Designer에서 제작한 ui를 불러옴

class MyWindow(QMainWindow, form_class):  # 다중상속 / 여기까지는 공통 모듈
#=======================================================================================================
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 위에서 불러온 test.ui 연결
        self.setWindowTitle("연습프로그램")

        self.setWindowIcon(QIcon("img/flower.png"))

        self.statusBar().showMessage('made by David 2024-03-29')

        self.button01.clicked.connect(self.button01_click)  # self.button01_click 끝에 () 절대 안됨--> error
        ## button01이 click되면 button01_click 메소드 호출
        self.button02.clicked.connect(self.button02_click)


    def button01_click(self):
        self.label01.setText("Hello World!!")

    def button02_click(self):
        self.label01.setText("Let's make a app!!")


# 항상 모듈화해야 할 부분==================================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

