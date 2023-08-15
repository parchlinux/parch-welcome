#!/usr/bin/python
#!/usr/bin/python

import os,subprocess

# Create Qrc file
listrc = os.listdir('UI')
listrc.remove('res.qrc')
f = open('UI/res.qrc', 'w')
f.write("""<RCC><qresource prefix="/">""")
for i in listrc:
    f.write(f"<file>{i}</file>")
f.write("""</qresource></RCC>""")
f.close()

# Compile Qrc & Create onefile script & run it
subprocess.run("""rcc -g python UI/res.qrc -o Res.py && sed -i 's/PySide2/PyQt6/g' Res.py && echo "#!/usr/bin/python" > Welcome && cat Res.py >> Welcome && cat Welcome.py >> Welcome && chmod +x Welcome && sed -i 's/import Res//g' Welcome && mv Welcome ../build/parch-welcome/usr/bin""",shell=True)