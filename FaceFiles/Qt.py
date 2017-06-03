import sys
from PyQt4 import QtGui,QtCore

class window(QtGui.QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Face Recognition")
        self.setWindowIcon(QtGui.QIcon('vit.png'))
        self.home()
    def home(self):
        btn = QtGui.QPushButton("Face Detect",self)
        btn.clicked.connect()
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = window()
    sys.exit(app.exec_())
run()