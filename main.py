from PyQt6 import QtWidgets, uic,QtGui,QtCore
import sys, os


class MyWindow(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        uic.loadUi("./main.ui", self)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.setObjectName("main")
    cssFile = "main.css"
    with open(cssFile, "r") as fh:
        main.setStyleSheet(fh.read())
    main.setWindowIcon(QtGui.QIcon())
    main.show()
    sys.exit(app.exec())
