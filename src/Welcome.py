import subprocess
import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtQml import *

import Res


class Quick(QQmlApplicationEngine):
    def setProperty(self, name, value):
        self.rootObjects()[0].setProperty(name, value)

    def property(self, name):
        return self.rootObjects()[0].property(name)

    def findChild(self, name, **kwargs):
        return self.rootObjects()[0].findChild(QObject, name)

    def close(self):
        self.rootObjects()[0].close()

    def __init__(self):
        super(Quick, self).__init__()


class Main(Quick):
    browser = "firefox"

    def b1_(self):
        self.close()
        subprocess.call(f'{self.browser} https://github.com/parchlinux', shell=True)

    def b2_(self):
        self.close()
        subprocess.call(f'{self.browser} https://twitter.com/bssfoss', shell=True)

    def b3_(self):
        self.close()
        subprocess.call(f'{self.browser} https://t.me/parchlinux', shell=True)

    def b4_(self):
        self.close()
        subprocess.call(f'{self.browser} https://discord.gg/9RW5cRByAM', shell=True)

    def b5_(self):
        self.close()
        subprocess.call(f'{self.browser} https://mas.to/@bssfoss', shell=True)

    def b6_(self):
        self.close()
        subprocess.call(f'{self.browser} https://coffeete.ir/parchlinux', shell=True)

    def b7_(self):
        self.close()
        subprocess.call(f'{self.browser} https://parchlinux.ir', shell=True)

    def b8_(self):
        self.close()
        subprocess.call('firefox https://parchlinux.ir/parchwiki/', shell=True)

    def install_(self):
        self.close()
        subprocess.call('sudo sh /etc/calamares/launch.sh',shell=True)

    def __init__(self):
        super(Main, self).__init__()

        self.load(":/ParchLinux.qml")

        self.b1 = self.findChild("b1")
        self.b1.clicked.connect(self.b1_)

        self.b2 = self.findChild("b2")
        self.b2.clicked.connect(self.b2_)

        self.b3 = self.findChild("b3")
        self.b3.clicked.connect(self.b3_)

        self.b4 = self.findChild("b4")
        self.b4.clicked.connect(self.b4_)

        self.b5 = self.findChild("b5")
        self.b5.clicked.connect(self.b5_)

        self.b6 = self.findChild("b6")
        self.b6.clicked.connect(self.b6_)

        self.b7 = self.findChild("b7")
        self.b7.clicked.connect(self.b7_)

        self.b8 = self.findChild("b8")
        self.b8.clicked.connect(self.b8_)

        self.install = self.findChild('install')
        self.install.clicked.connect(self.install_)


app = QGuiApplication([])
app.setWindowIcon(QIcon(":/ParchLogo.svg"))
m = Main()
app.exec()