#include "processhandler.h"

ProcessHandler::ProcessHandler(QObject *parent) : QObject(parent)
{
    connect(&m_process, QOverload<int, QProcess::ExitStatus>::of(&QProcess::finished),
            this, &ProcessHandler::processFinished);
}

void ProcessHandler::startProcess()
{
    m_process.start("sudo", QStringList() << "sh" << "/etc/calamares/launch.sh");
    m_process.waitForFinished();
    emit processFinished(m_process.exitCode(), m_process.exitStatus());
}
