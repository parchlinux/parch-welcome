# Parch Linux Dorood
Parch dorood (/do-rood/, درود, pronunciation) which is Persian word for "Greetings", is a welcome app in the Parch distribution. Dorood features:

- Showing Parch Linux pages on social media
- Running the installer program
- Updating Parch repositories
This program is still on alpha stages and it is not completely ready to use.
## Install
- **Step 1**: Copy files

for installing jump to `rootcopy` directory and copy `usr` folder to `/` by:
```shell
sudo sh Install.sh
```

- **Step 2**: Set as **start up** application
after installing we should set `/usr/share/applications/welcome.desktop` as a startup application

## Build

- **Step 1**: Generate **Qt Resource** from `src/UI` directory
```shell
python 01-Generate.py
```

- **Step 2**: Compile Generated **Qt Resource** `src/UI/res.qrc` file
```shell
sh 02-Compile.sh
```

- **Step 3**: Build one-file python
```shell
sh 03-Build.sh
```