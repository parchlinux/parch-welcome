#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QResource>
#include <QQmlContext>
#include <QObject>
#include <QQuickItem>
#include <QQuickView>
#include <QProcess>
#include "processhandler.h" // Include the ProcessHandler class header

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;

    // Register the ProcessHandler class with the QML engine
    qmlRegisterType<ProcessHandler>("com.parch", 1, 0, "ProcessHandler");

    // Load the QML content from the resource
    QResource::registerResource(":/resources.rcc");

    // Load the QML file
    engine.load(QUrl("qrc:/ParchLinux.qml"));

    // Set App Icon 
    app.setWindowIcon(QIcon("icon.png"));

    return app.exec();
}