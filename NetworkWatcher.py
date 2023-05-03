#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from DBConnection import conn

root = tk.Tk(className='Network Watcher')
table = ttk.Treeview(root)
cursor = conn.cursor()

def getDataAmount(data):
    size = 'Bytes'
    if (data > 1023):
        data = data / 1024
        size = 'KB'
        if (data > 1023):
            data = data / 1024
            size = 'MB'
            if (data > 1023):
                data = data / 1024
                size = 'GB'
    return "{:.2f}".format(data) + size

def fillTableData():
    cursor.execute("SELECT * FROM dailyStats ORDER BY date desc")
    rows = cursor.fetchall()
    table.delete(*table.get_children())
    for row in rows:
        table.insert(parent='', index='end', iid=None, values=(
            row[0], row[2], row[1], getDataAmount(row[4]), getDataAmount(row[3]), getDataAmount(row[5])))
    root.after(5000, fillTableData)

def main():
    img  = PhotoImage(file='/lib/NetworkWatcher/icon.png')
    root.title('Network Watcher v1.0')
    root.wm_iconphoto(True, img)

    table['columns'] = ('id', 'Date', 'Network', 'Recieved', 'Sent', 'Total')

    table.column('#0', stretch=tk.NO, width=0)
    table.column('id', stretch=tk.YES, anchor=tk.CENTER, width=20)
    table.column('Date', anchor=tk.CENTER, width=100)
    table.column('Network', anchor=tk.CENTER, width=100)
    table.column('Recieved', anchor=tk.CENTER, width=100)
    table.column('Sent', anchor=tk.CENTER, width=100)
    table.column('Total', anchor=tk.CENTER, width=100)

    table.heading('#0', text='')
    table.heading('id', text='id')
    table.heading('Date', text='Date')
    table.heading('Network', text='Network')
    table.heading('Recieved', text='Recieved')
    table.heading('Sent', text='Sent')
    table.heading('Total', text='Total')

    fillTableData()
    table.pack(expand=True, fill='both')
    root.mainloop()

main()