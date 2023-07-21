from PyQt6 import QtWidgets, uic
import sys, os


class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        uic.loadUi("./main.ui", self)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    cssFile = "main.css"
    with open(cssFile, "r") as fh:
        main.setStyleSheet(fh.read())
    main.show()
    sys.exit(app.exec_())
