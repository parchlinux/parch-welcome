#!/usr/bin/env python

import os

listrc = os.listdir('UI')
listrc.remove('res.qrc')
f = open('UI/res.qrc', 'w')
f.write("""<RCC><qresource prefix="/">""")
for i in listrc:
    f.write(f"<file>{i}</file>")
f.write("""</qresource></RCC>""")
f.close()