from DBConnection import conn

class Stat:
    cursor = conn.cursor()
    REFRESH_TIMEOUT = 2000
    dailyTable = None
    root = None

    def __init__(self, root, dailyTable):
        self.root = root
        self.dailyTable = dailyTable

    # convert data into a readable format
    def getDataAmount(self, data):
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
    
    # fill the daily stats table from the database
    def fillDailyTable(self):
        # get records
        self.cursor.execute("SELECT * FROM dailyStats ORDER BY date desc")
        rows = self.cursor.fetchall()
        # clear all existing data from the table
        self.dailyTable.delete(*self.dailyTable.get_children())
        # fill new data
        for i, row in enumerate(rows):
            self.dailyTable.insert(parent='', index='end', iid=None, values=(
                i+1, row[2], row[1], self.getDataAmount(row[4]), self.getDataAmount(row[3]), self.getDataAmount(row[5])))
        # keep doing this again and again
        self.root.after(self.REFRESH_TIMEOUT, self.fillDailyTable)