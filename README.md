# Parch Linux Dorood
Parch dorood (/do-rood/, درود, pronunciation) which is Persian word for "Greetings", is a welcome app in the Parch distribution. Dorood features:

- Showing Parch Linux pages on social media
- Running the installer program
- Updating Parch repositories
This program is still on alpha stages and it is not completely ready to use.

## Build the package
- Jump to `build` directory:
```shell
cd build
```
- Compress `parch-welcome` directory for creating package:
```shell
tar -czvf parch-welcome.tar.gz parch-welcome/
```
- Make package after compressing:
```shell
makepkg -f
```

## Install the package
- For installing this pacakge run:
```shell
cd build
sudo pacman -U ./parch-welcome*
```

## Generate Qt Resources (if edited)
if you made a changes in src you can update the `qrc` by running this command:
```shell
cd src
python QrcGenerate.py
```