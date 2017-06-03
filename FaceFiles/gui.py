import os,sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
window.setGeometry(0,0,500,500)
pic = QtGui.QLabel(window)
pic.setGeometry(0,0,500,500)
pic.setPixmap(QtGui.QPixmap(os.getcwd()))
label = QtGui.QLabel()
pixmap=QtGui.QPixmap('C:\\Users\\MY PC\\PycharmProjects\\untitled\\face.jpg')
window.show()
sys.exit(app.exec_())