import shutil, os

shutil.make_archive("welcome", "gztar", "welcome")
os.system("makepkg -f")
os.remove("welcome.tar.gz")