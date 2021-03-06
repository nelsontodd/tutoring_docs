import sqlite3
import csv
conn = sqlite3.connect('example.db')
c    = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

#All of the above code is straight from the python documentation

#Write our results to a csv
with open('stocks.csv', 'w') as csvfile:
    stockswriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            stockswriter.writerow(row)

