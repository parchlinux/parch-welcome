import QtQuick 6.0
import QtQuick.Controls 6.0
import QtQuick.Controls.Material 6.0
import com.parch 1.0
ApplicationWindow {
    width: 900
    height: 500
    flags: Qt.FramelessWindowHint
    visible: true
    id: parch

    color: "transparent"
    function link(url) {
        Qt.openUrlExternally(url);
    }
    ProcessHandler {
        id: processHandler

        onProcessFinished: {
            // console.log("Process finished with exit code:", exitCode, "Exit status:", exitStatus);
            parch.close()
        }
    }
    Rectangle {
        anchors.centerIn: parent
        width: 900
        height: 500
        radius: 20
        color: "#DD010409"

        Row {
            anchors.right: parent.right
            anchors.top: parent.top

            ToolButton {
                icon.color: "white"
                icon.source: "x-lg.svg"
                onClicked: {
                    parch.close()
                }
            }
        }

        Column {
            anchors.centerIn: parent

            Image {
                source: "ParchLogo.svg"
                width: 128
                height: 128
                anchors.horizontalCenter: parent.horizontalCenter
            }
            Rectangle {
                width: parent.width
                height: 12
                color: "transparent"
            }
            Text {
                text: "<strong>Parch Linux</strong>"
                color: "white"
                font.family: "Ubuntu"
                font.pixelSize: 30
                anchors.horizontalCenter: parent.horizontalCenter
            }
             Rectangle {
                width: parent.width
                height: 8
                color: "transparent"
            }
            Text {
                text: "<strong><font color='#3b82f6'>Parch Linux</font></strong> is an open-source, Arch-based Linux distribution,"
                color: "white"
                verticalAlignment: Text.AlignVCenter
                font.family: "Ubuntu Light"
                font.pixelSize: 14
                anchors.horizontalCenter: parent.horizontalCenter
            }
            Text {
                color: "white"
                text: "that tried to be pretty, easy to use, light, fast and stable."
                verticalAlignment: Text.AlignVCenter
                font.family: "Ubuntu Light"
                font.pixelSize: 14
                anchors.horizontalCenter: parent.horizontalCenter
            }
            Rectangle {
                width: parent.width
                height: 8
                color: "transparent"
            }
            Row {
                anchors.horizontalCenter: parent.horizontalCenter
                ToolButton {
                    icon.color: "white"
                    icon.source: "github.svg"
                    objectName: "b1"
                    onClicked: {
                        link("https://github.com/parchlinux")
                    }
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "tw.svg"
                    objectName: "b2"
                    onClicked: {
                        link("https://twitter.com/bssfoss")
                    }
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "tele.svg"
                    objectName: "b3"
                    onClicked: {
                        link("https://t.me/parchlinux")
                    }
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "discord.svg"
                    objectName: "b4"
                    onClicked: {
                        link("https://discord.gg/9RW5cRByAM")
                    }
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "masto.svg"
                    objectName: "b5"
                    onClicked: {
                        link("https://mas.to/@bssfoss")
                    }
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "cafe.svg"
                    objectName: "b6"
                    // Replace with Daramet platform due to Coffeete platform is unavailable
                    onClicked: {
                        link("https://daramet.com/parchlinux")
                    }
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "website.svg"
                    objectName: "b7"
                    onClicked: {
                        link("https://parchlinux.ir")
                    }
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "book.svg"
                    objectName: "b8"
                    onClicked: {
                        link("https://parchlinux.ir/parchwiki/")
                    }
                }
            }
            Rectangle {
                width: parent.width
                height: 20
                color: "transparent"
            }
            Rectangle {
                color: "#4063eb"
                width: 160
                height: 40
                radius: 15
                anchors.horizontalCenter: parent.horizontalCenter
                ToolButton {
                    anchors.fill: parent
                    objectName: "install"
                    id: installBtn
                    onClicked: {
                        // Start the process through the ProcessHandler object
                        processHandler.startProcess();
                    }
                }

                Row {
                    anchors.centerIn: parent

                    Rectangle {
                        width: 18
                        height: 20

                        color: "transparent"
                    }

                    Text {
                        color: "white"
                        font.family: "Ubuntu"
                        text: "Install Parch"
                        font.pixelSize: 14
                        anchors.verticalCenter: parent.verticalCenter
                        id: installBtnText
                    }
                    ToolButton {
                        width: 40
                        height: 40
                        anchors.verticalCenter: parent.verticalCenter
                        icon.color: "white"
                        icon.source: "install.svg"
                        onClicked: {
                            // Start the process through the ProcessHandler object
                            processHandler.startProcess();
                        }
                    }
                }
            }
        }
    }
}
