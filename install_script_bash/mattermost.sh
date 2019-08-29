#!/bin/bash

echo "In /opt"
echo ''

echo "Install Mattermost :"
echo "* download"
curl -o mattermost-desktop-4.2.1-linux-x64.tar.gz  https://releases.mattermost.com/desktop/4.2.1/mattermost-desktop-4.2.1-linux-x64.tar.gz
echo "* extract"
tar -zxf mattermost-desktop-4.2.1-linux-x64.tar.gz
echo "* clean .tar.gz"
rm mattermost-desktop-4.2.1-linux-x64.tar.gz
echo "* Execute the script file to create a Mattermost.desktop file"
/opt/mattermost-desktop-4.2.1-linux-x64/create_desktop_file.sh
echo "* move to  ~/.local/share/applications/"
mv Mattermost.desktop ~/.local/share/applications/
echo "Mattermost Installed"
echo ''
