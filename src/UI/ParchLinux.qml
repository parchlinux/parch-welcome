import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow {
    width: 900
    height: 500
    flags: Qt.FramelessWindowHint
    visible: true
    id: parch

    color: "transparent"

    Rectangle {
        anchors.fill: parent
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
                verticalAlignment: Text.AlignCenter
                font.family: "Ubuntu Light"
                font.pixelSize: 14
                anchors.horizontalCenter: parent.horizontalCenter
            }
            Text {
                color: "white"
                text: "that tried to be pretty, easy to use, light, fast and stable."
                verticalAlignment: Text.AlignCenter
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
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "tw.svg"
                    objectName: "b2"
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "tele.svg"
                    objectName: "b3"
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "discord.svg"
                    objectName: "b4"
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "masto.svg"
                    objectName: "b5"
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "cafe.svg"
                    objectName: "b6"
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "website.svg"
                    objectName: "b7"
                }
                ToolButton {
                    icon.color: "white"
                    icon.source: "book.svg"
                    objectName: "b8"
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
                    }
                    ToolButton {
                        width: 40
                        height: 40
                        anchors.verticalCenter: parent.verticalCenter
                        icon.color: "white"
                        icon.source: "install.svg"
                    }
                }
            }
        }
    }
}
