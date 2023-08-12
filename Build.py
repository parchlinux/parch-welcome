#!/usr/bin/python
import os,subprocess

# Jump to Src
os.chdir("src/")

# Create Qrc file
listrc = os.listdir('UI')
listrc.remove('res.qrc')
f = open('UI/res.qrc', 'w')
f.write("""<RCC><qresource prefix="/">""")
for i in listrc:
    f.write(f"<file>{i}</file>")
f.write("""</qresource></RCC>""")
f.close()

# Compile Qrc & Create onefile script & Build Parch Package
subprocess.run("""rcc -g python UI/res.qrc -o Res.py && sed -i 's/PySide2/PyQt6/g' Res.py && echo "#!/usr/bin/python" > Welcome && cat Res.py >> Welcome && cat Welcome.py >> Welcome && chmod +x Welcome && cp Welcome ../build/parch-welcome/usr/bin/ && cd ../build && chmod +x parch-welcome/usr/bin/* && tar -czvf parch-welcome.tar.gz parch-welcome/ && makepkg -f && cd .. && rm -rf build/pkg build/src build/*.tar.gz && rm -rf src/Welcome""",shell=True)