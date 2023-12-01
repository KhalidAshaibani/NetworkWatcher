#!/bin/bash

# copy files
mv /usr/bin/Network-Watcher/lib/NetworkWatcher /lib/NetworkWatcher
ln -s /usr/bin/Network-Watcher/NetworkWatcher/NetworkWatcher /usr/bin/NetworkWatcher
ln -s /usr/bin/Network-Watcher/NetworkWatcherMonitor/NetworkWatcherMonitor /usr/bin/NetworkWatcherMonitor

# add the App to Application menu
cat > home/$(logname)/.local/share/applications/NetworkWatcher.desktop << EOF
[Desktop Entry]
Version=1.1
Type=Application
Name=NetworkWatcher
Comment=Network Watcher Watches Your Network and gives you a statistics on the data usage
TryExec=NetworkWatcher
Exec=NetworkWatcher
Icon=/lib/NetworkWatcher/icon.png
Actions=Editor
EOF

# Run the program after installation myprogram & Add the program to the autostart menu
mkdir -p home/$(logname)/.config/autostart
cat > home/$(logname)/.config/autostart/NetworkWatcher.desktop << EOF
[Desktop Entry]
Type=Application
Exec=NetworkWatcherMonitor
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Network Watcher Monitor
Comment=Run Network Watcher Monitor
EOF

# Set the correct ownership and permissions for the autostart file
chown $USER:$USER home/$(logname)/.config/autostart/NetworkWatcher.desktop
chmod +x home/$(logname)/.config/autostart/NetworkWatcher.desktop

# Create DB file and set owner to current user
touch /lib/NetworkWatcher/NetworkWatcher.db
chown $(logname):$(logname) /lib/NetworkWatcher/
chown $(logname):$(logname) /lib/NetworkWatcher/NetworkWatcher.db
