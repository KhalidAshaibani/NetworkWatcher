# View the stats from the database

#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from Table import Table
from Stat import Stat

def main():
    #  create the window frame
    root = tk.Tk(className='Network Watcher')
    # create the daily stats table
    dailyTable = Table({
                "id": {'stretch':tk.YES,'anchor':tk.CENTER,'width':20},
                "Date": {'anchor':tk.CENTER,'width':100},
                "Network": {'anchor':tk.CENTER,'width':100},
                "Recieved": {'anchor':tk.CENTER,'width':100},
                "Sent": {'anchor':tk.CENTER,'width':100},
                "Total": {'anchor':tk.CENTER,'width':100},
            },
            {
                'id':'',
                'Date':'Date',
                'Network':'Network',
                'Recieved':'Recieved',
                'Sent':'Sent',
                'Total':'Total'
            },
            root
            ).table
    
    # create Stat object to deal with data
    stat = Stat(root, dailyTable)
    # set the app icon and title
    img  = PhotoImage(file='/lib/NetworkWatcher/icon.png')
    root.title('Network Watcher v1.0')
    root.wm_iconphoto(True, img)

    # fill data into the table
    stat.fillDailyTable()
    dailyTable.pack(expand=True, fill='both')
    # start the window
    root.mainloop()

main()