#ifndef PROCESSHANDLER_H
#define PROCESSHANDLER_H

#include <QObject>
#include <QProcess>
class ProcessHandler : public QObject
{
    Q_OBJECT

public:
    explicit ProcessHandler(QObject *parent = nullptr);

public slots:
    void startProcess();

signals:
    void processFinished(int exitCode, QProcess::ExitStatus exitStatus);

private:
    QProcess m_process;
};

#endif // PROCESSHANDLER_H
