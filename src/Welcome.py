# Import I/O
import subprocess
import sys

# Import PyQt6 Framework libraries
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtQml import *

# Import Resources of Qt
import Res

# Simple Qt Quick class for loading QML files


class Quick(QQmlApplicationEngine):
    # DO: Set property of object
    def setProperty(self, name, value):
        self.rootObjects()[0].setProperty(name, value)

    # DO: Get property of object
    def property(self, name):
        return self.rootObjects()[0].property(name)

    # DO: find a object
    def findChild(self, name, **kwargs):
        return self.rootObjects()[0].findChild(QObject, name)

    # DO: Close the loader
    def close(self):
        self.rootObjects()[0].close()

    def __init__(self):
        super(Quick, self).__init__()


# Main Class of Parch Welcome Project
class Main(Quick):
    # DO: Button 1 loading link: https://github.com/parchlinux
    def b1_(self):
        self.link("https://github.com/parchlinux")

    # DO: Button 2 loading link: https://twitter.com/bssfoss
    def b2_(self):
        self.link("https://twitter.com/bssfoss")

    # DO: Button 3 loading link: https://t.me/parchlinux
    def b3_(self):
        self.link("https://t.me/parchlinux")

    # DO: Button 4 loading link: https://discord.gg/9RW5cRByAM
    def b4_(self):
        self.link("https://discord.gg/9RW5cRByAM")

    # DO: Button 5 loading link: https://mas.to/@bssfoss
    def b5_(self):
        self.link("https://mas.to/@bssfoss")

    # DO: Button 6 loading link: https://coffeete.ir/parchlinux
    def b6_(self):
        self.link("https://coffeete.ir/parchlinux")

    # DO: Button 7 loading link: https://parchlinux.ir
    def b7_(self):
        self.link("https://parchlinux.ir")

    # DO: Button 8 loading link: https://parchlinux.ir/parchwiki/
    def b8_(self):
        self.link("https://parchlinux.ir/parchwiki/")

    # DO: Run Calamares Installer
    def install_(self):
        self.close()
        subprocess.Popen("sudo sh /etc/calamares/launch.sh", shell=True)

    # DO: Loading link in `xdg-open` function
    async def link(self, url):
        self.close()
        await subprocess.Popen(f"xdg-open {url}", shell=True)

    # DO: Init Function
    def __init__(self):
        super(Main, self).__init__()

        # Load Main QML file
        self.load("UI/ParchLinux.qml")

        self.b1 = self.findChild("b1")  # Find Button 1
        self.b1.clicked.connect(self.b1_)  # Action: Connect Button 1 action to b1_

        self.b2 = self.findChild("b2")  # Find Button 2
        self.b2.clicked.connect(self.b2_)  # Action: Connect Button 2 action to b2_

        self.b3 = self.findChild("b3")  # Find Button 3
        self.b3.clicked.connect(self.b3_)  # Action: Connect Button 3 action to b3_

        self.b4 = self.findChild("b4")  # Find Button 4
        self.b4.clicked.connect(self.b4_)  # Action: Connect Button 4 action to b4_

        self.b5 = self.findChild("b5")  # Find Button 5
        self.b5.clicked.connect(self.b5_)  # Action: Connect Button 5 action to b5_

        self.b6 = self.findChild("b6")  # Find Button 6
        self.b6.clicked.connect(self.b6_)  # Action: Connect Button 6 action to b6_

        self.b7 = self.findChild("b7")  # Find Button 7
        self.b7.clicked.connect(self.b7_)  # Action: Connect Button 7 action to b7_

        self.b8 = self.findChild("b8")  # Find Button 8
        self.b8.clicked.connect(self.b8_)  # Action: Connect Button 8 action to b8_

        self.install = self.findChild("install")  # Find Install Button
        self.install.clicked.connect(
            self.install_
        )  # Action: Connect to install_ function


if __name__ == "__main__":
    # Start Qt Qui Application loop
    app = QGuiApplication([])
    # Set Qt Window Icon
    app.setWindowIcon(QIcon(":/ParchLogo.svg"))
    # Loading Main Class
    m = Main()
    # Set loop exec
    app.exec()
