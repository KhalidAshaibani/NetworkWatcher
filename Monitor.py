# Monitor the system traffic and records it into the database

#!/usr/bin/env python3
import time
import os
import sqlite3
from datetime import datetime
import psutil
from DBConnection import conn

# Create the table in the database
def createTable(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dailyStats (
                        id INTEGER PRIMARY KEY,
                        ssid TEXT NOT NULL,
                        date DATE NOT NULL,
                        sent INTEGER NOT NULL,
                        recieved INTEGER NOT NULL,
                        usage INTEGER NOT NULL
                        )''')
    conn.commit()

# returns the connected network ssid (Network Name)
def getNetworkName():
    ssid = os.popen("iwgetid -r").read().strip()
    return ssid

# returns network stats counters
def getNetworkUsage(interface):
    counters = psutil.net_io_counters(pernic=True)
    if interface in counters:
        data = counters[interface]
        return {
            'sent': data.bytes_sent,
            'recieved': data.bytes_recv,
            'total': data.bytes_recv + data.bytes_sent,
        }
    return {
        'sent': 0,
        'recieved': 0,
        'total': 0,
    }

# updates the database records for a specified network for today
# if the network doesn't exist in the database or doesn't have stats for today yet 
# create a new record
def updateNetworkUsage(conn, ssid, sent, recieved, usage):
    today = datetime.now().date()
    cursor = conn.cursor()
    # retrive today record for the specified network
    cursor.execute(
        "SELECT * FROM dailyStats WHERE ssid=? AND date=?", (ssid, today))
    row = cursor.fetchone()

    # check if record exists and update it if it does or create new record if it doesn't
    if row:
        newSent = row[3] + sent
        newRecieved = row[4] + recieved
        newUsage = row[5] + usage
        cursor.execute(
            "UPDATE dailyStats SET sent=?, recieved=?, usage=? WHERE id=?", (newSent, newRecieved, newUsage, row[0]))
    else:
        cursor.execute(
            "INSERT INTO dailyStats (ssid, date, sent, recieved, usage) VALUES (?, ?, ?, ?, ?)", (ssid, today, sent, recieved, usage))
    conn.commit()


def main():
    prevNetwork = ""
    prevUsage = {
        'sent': 0,
        'recieved': 0,
        'total': 0,
    }
    createTable(conn)
    # print info into terminal
    print("Network Watcher v0.1\nMonitoring Your Network...\nPress CTRL+Z to exit")

    # start monitoring loop
    while True:
        currentNetwork = getNetworkName()
        # if network exists an has an ssid
        if(len(currentNetwork)):
            interface = "wlp2s0"

            # if current connected network is not the same network monitored in the previous iteration
            # update the current network and get it's current usage
            if currentNetwork != prevNetwork:
                prevNetwork = currentNetwork
                prevUsage = getNetworkUsage(interface)
            # else get the usage of the current network in one second and update the database
            else:
                currentUsage = getNetworkUsage(interface)

                sent = currentUsage['sent'] - prevUsage['sent']
                recieved = currentUsage['recieved'] - prevUsage['recieved']
                total = currentUsage['total'] - prevUsage['total']

                updateNetworkUsage(conn, currentNetwork, sent, recieved, total)
                prevUsage = currentUsage

            time.sleep(1)


main()
