#!/bin/bash
# Zorg er van te voren voor dat python verwijst naar python 3.5 doormiddel van een symlink of een alias
#
# Voer dit commando uit `~/.bashrc` en voeg dit toe aan het einde van het bestand `alias python=python3.5`

sudo apt-get install mpg321 -y
amixer cset numid=3 1
amixer set PCM -- -400
sudo apt-get install libjpeg-dev -y
pip install Pillow -y