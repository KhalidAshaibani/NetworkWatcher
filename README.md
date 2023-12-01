# NetworkWatcher

Network Watcher makes it easy to monitor your networks usage, it provide a detailed daily usage statistics on sent, recieved and total usage for each Wifi connection on (wlp2s0) interface.

### Installation

#### Download the .deb file

[NetworkWatcher_1.2_amd64.deb](https://github.com/khalidalshaibani/NetworkWatcher/releases/download/v1.2/NetworkWatcher_1.2_amd64.deb)

#### Install the file you just downloaded

```sh
sudo apt install ./NetworkWatcher_1.2_amd64.deb
```

#### Start Monitoring

Network Watcher will start automatically after restart to monitor your network traffic, but if it didn't, you can run the following command in the terminal

```sh
NetworkWatcherMonitor
```

#### See Statistics

Network Watcher is automatically added to application menu, and can be run from there
However, you can also do this by running the following command in the terminal

```sh
NetworkWatcher
```
