#!/usr/bin/env python3
# View the stats from the database

import tkinter as tk
from tkinter import ttk
from tkinter import *
from Table import Table
from Stat import Stat
from Consts import APP_VERSION


def main():
    #  create the window frame
    root = tk.Tk(className="Network Watcher")
    # create the daily stats table
    dailyTable = Table(
        {
            "id": {"stretch": tk.YES, "anchor": tk.CENTER, "width": 20},
            "Date": {"anchor": tk.CENTER, "width": 100},
            "Network": {"anchor": tk.CENTER, "width": 100},
            "Received": {"anchor": tk.CENTER, "width": 100},
            "Sent": {"anchor": tk.CENTER, "width": 100},
            "Total": {"anchor": tk.CENTER, "width": 100},
        },
        {
            "id": "",
            "Date": "Date",
            "Network": "Network",
            "Received": "Received",
            "Sent": "Sent",
            "Total": "Total",
        },
        root,
    ).table
    # create table for summary table
    summaryTable = Table(
        {
            "empty1": {"stretch": tk.YES, "anchor": tk.CENTER, "width": 20},
            "empty2": {"anchor": tk.CENTER, "width": 100},
            "Date": {"anchor": tk.CENTER, "width": 100},
            "Received": {"anchor": tk.CENTER, "width": 100},
            "Sent": {"anchor": tk.CENTER, "width": 100},
            "Total": {"anchor": tk.CENTER, "width": 100},
        },
        {},
        root,
    ).table
    style = ttk.Style()
    style.configure("summaryStats.Treeview.Heading", font=("", 1), background="none")
    summaryTable.configure(style="summaryStats.Treeview", height=3)

    # create Stat object to deal with data
    stat = Stat(root, dailyTable, summaryTable)
    # set the app icon and title
    img = PhotoImage(file="/lib/NetworkWatcher/icon.png")
    root.title("Network Watcher v" + APP_VERSION)
    root.wm_iconphoto(True, img)

    # fill data into the table
    stat.fillDailyTable()
    stat.fillSummaryTable()
    dailyTable.pack(expand=True, fill="both")
    summaryTable.pack(fill="x", side="bottom")
    # start the window
    root.mainloop()


main()
