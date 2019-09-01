#!/bin/bash

echo "Vim Packages:"
echo "  * APT Vim"
curl -sL https://raw.githubusercontent.com/egalpin/apt-vim/master/install.sh | sh

echo "  * nerdtree"
apt-vim install -y https://github.com/scrooloose/nerdtree.git
echo "Vim Packages Installed"
echo ''
