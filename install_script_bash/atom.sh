#!/bin/bash

echo "Install Atom :"
echo "* download"
cd ~/Downloads
wget https://atom.io/download/deb -O atom.deb
echo "* Install dpkg"
dpkg -i atom.deb
rm atom.deb
echo "Atom Installed"
echo ''
