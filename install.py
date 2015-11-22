#!/usr/bin/python
#By: Magno Tutor
#Date: 21/11/2015
#BETA

from os import system
from time import sleep

print("INSTALANDO ARCH LINUX\n\n\n")
sleep(5)
system("clear")

print("MUDANDO LAYOUT DO TECLADO PARA br-abnt2\n")
sleep(5)
system("loadkeys br-abnt2")
system("clear")

print("VEFIFICANDO E INICIANDO A CONEXAO COM A INTERNET - DHCPCD\n")
sleep(6)
system("systemctl status dhcpcd")
system("systemctl start dhcpcd")
system("clear")

print("CRIE AS PARTICOES: Raiz e Swap\n")
sleep(5)
system("cfdisk")
system("clear")
print("FORMATANDO E MONTANDO 'RAIZ' \n")
sleep(4)
system("mkfs.ext4 /dev/sda1")
system("mount -t ext4 /dev/sda1 /mnt")
system("clear")
print("SWAP - ATIVAR\n")
sleep(2)
system("mkswap /dev/sda2")
system("swapon /dev/sda2")
system("clear")

print("LISTA DE ESPELHOS DOS REPOSITORIOS - BRASIL\n")
sleep(5)
print("DECA ATE A LINHA DO BRAZIL E COPIE O 'SERVER' COM CONTROL+K E CONTROL+U PARA COLAR -> COLE LA EM CIMA\n")
sleep(13)
system("nano /etc/pacman.d/mirrorlist")
system("clear")

print("INSTALANDO SISTEMA BASE\n")
print("ISSO PODE DEMORAR UM POUCO\n")
sleep(7)
system("pacstrap /mnt base base-devel")
system("clear")

print("GERANDO FSTAB\n")
sleep(2)
system("genfstab /mnt >> /mnt/etc/fstab")
system("clear")

print ("ENTRANDO NO NOVO SISTEMA")
sleep(3)
system("arch-chroot /mnt")
system("clear")

print("MUDANDO LAYOUT DO TECLADO DENTRO DO CHROOT\n")
sleep(5)
system("loadkeys br-abnt2")
system("clear")

print("MUDAR A LINGUAGEM DO SISTEMA\n")
sleep(3)
print("APERTE CONTROL+W E PESQUISE POR pt_BR.UTF-8 E RETIRE O # DA LINHA")
sleep(10)
system("nano /etc/locale.gen")
system("clear")

print("GERANDO LOCALE.GEN")
sleep(3)
system("locale-gen")
system("clear")

print("ECHO E EXPORT LANG\n")
sleep(2)
system("echo LANG=pt_BR.UTF-8 > /etc/locale.conf")
system("export LANG=pt_BR.UTF-8")
system("clear")

print("GERANDO LINK SIMBOLICO/HORA\n")
sleep(4)
system("ln -s /usr/share/zoneinfo/Brazil/East /etc/localtime")
system("date")
system("clear")

print("INSIRA UMA SENHA PARA ROOT\n")
sleep(3)
system("passwd")
system("clear")

print("BAIXANDO GRUB\n")
sleep(2)
system("pacman -S grub")
print ("INSTALANDO GRUB\n")
sleep(2)
system("grub-install /dev/sda")
system("clear")

print("RODANDO MKINITCPIO\n")
sleep(2)
system("mkinitcpio -p linux")
system("clear")

print("GRUB-COFIG\n")
sleep(2)
system("grub-mkconfig -o /boot/grub/grub.cfg\n")
system("clear")

print ("SAINDO DO CHROOT\n")
sleep(2)
system("exit")
system("clear")

print("DESMONTANDO TODAS AS PARTICOES\n")
sleep(3)
system("umount -a")
system("clear")

print("REINICIANDO... TIRE A MIDIA USB/DVD\n")
sleep(4)
system("clear")
system("reboot")

print("ATIVANDO - INICIANDO - TESTANDO CONEXAO COM A INTERNET\n")
sleep(6)
system("systemctl enable dhcpcd.service")
system("systemctl start dhcpcd")
system("ping -c3 google.com")
system("clear")

print("INSTALANDO DRIVER DE SOM\n")
sleep(3)
system("pacman -S alsa-utils pulseaudio")
system("clear")

print("INSTALANDO XORG")
sleep(2)
system("pacman -S xorg-server xorg-xinit xorg-server-utils xorg-twm xorg-xclock xterm")
system("clear")

print("INSTALANDO DRIVER DE VIDEO\n")
sleep(3)
system("lspci | grep VGA")
print("\n")
system("pacman -S xf86-video-vesa")
system("clear")

print("INSTALANDO MESA\n")
sleep(2)
system("pacman -S mesa")
system("clear")

print("INSTALANDO FONTES\n")
sleep(2)
system("pacman -S ttf-dejavu")
system("clear")

print("INSTALANDO GNOME")
print("ISSO PODE DEMORAR DEPENDE DE SUA INTERNET\n")
sleep(8)
system("pacman -S gnome")
system("clear")

print("INSTALANDO - ATIVANDO LXDM UM DISPLAY MANAGER\n")
sleep(5)
system("pacman -S lxdm")
system("systemctl enable lxdm.service")
system("clear")

print("INSTALANDO PROGRAMAS ESSENCIAIS PARA SEU ARCH-LINUX :3\n")
sleep(5)
system("pacman -S leafpad audacious unzip unrar file-roller chromium geany")
system("clear")

print("DEIXANDO FULL SCREEN A TELA - VIRTUALBOX\n")
sleep(4)
system("pacman -S virtualbox-guest-utils virtualbox-guest-dkms")
system("clear")

print("FINALIZANDO INSTALADOR - REINICIANDO...")
print("SAINDO AQUI GENTE :3\n")
sleep(8)
system("clear")
system("reboot")
