import tkinter as tk
from tkinter import ttk

class Table:
    table = None
    # initialize the table columns and headers
    def __init__(self, columns, titles, root):
        self.table = ttk.Treeview(root)
        self.table['columns'] = tuple(columns.keys())
        self.table.column('#0', stretch=tk.NO, width=0)
        for (column, properties) in columns.items():
            self.table.column(
                column,
                stretch=(properties.get('stretch') if ('stretch' in properties) else tk.TRUE),
                anchor=(properties.get('anchor') if ('anchor' in properties) else tk.CENTER),
                width=(properties.get('width') if ('width' in properties) else 0)
            )
        
        for (column,i) in columns.items():
            if(titles.get(column)):
                self.table.heading(column, text=str(titles.get(column)))