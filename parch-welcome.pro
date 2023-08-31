QT += core widgets gui qml quickcontrols2

CONFIG += release
TARGET = parch-welcome
TEMPLATE = app

SOURCES += src/main.cpp src/processhandler.cpp

HEADERS += src/processhandler.h

RESOURCES += src/assets/res.qrc
