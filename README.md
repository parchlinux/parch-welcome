# Parch Linux Dorood
Parch dorood (/do-rood/, درود, pronunciation) which is Persian word for "Greetings", is a welcome app in the Parch distribution. Dorood features:

- Showing Parch Linux pages on social media
- Running the installer program
- Updating Parch repositories
This program is still on beta stages and it is semi complete and ready to use.

## Build the package on Arch machines

```shell
makepkg -f
```

### Install the package
- For installing this pacakge run:
```shell
cd build
sudo pacman -U ./parch-welcome*
```