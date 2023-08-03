#!/usr/bin/bash
chmod +x parch-welcome/usr/bin/*
tar -czvf parch-welcome.tar.gz parch-welcome/
makepkg -f