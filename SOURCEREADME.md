# BUILD CODE

Build `NetworkWatcher` using this command

```sh
pyinstaller NetworkWatcher.py
```

Build `NetworkWatcherMonitor` using this command

```sh
pyinstaller NetworkWatcherMonitor.py
```

# ORGANIZE FILES

Navigate to `dist` folder, and then copy both `NetworkWatcher` and `NetworkWatcherMonitor` folders into a folder with name `Network-Watcher`

Then, copy `icon.svg` from root folder into `dist/Network-Watcher/lib/NetworkWatcher/icon.png`

# BUILD NETWORK_WATCHER INTO DEB PACKAGE

In `dist` folder, run this command

```sh
fpm -s dir -t deb -n NetworkWatcher -v 1.2 -C ./ --prefix /usr/bin --after-install ../postInstall.sh .
```
