import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#create/connect to DB and table
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

#insert sample rows
cursor.executemany("""
insert into Sales(product, quantity, price)values(?,?,?)""",
[("Mobile",30,15000),
 ("Laptop",9,55000),
 ("Earphones",40,800),
 ("Mobile",10,15000),
 ("Laptop",5,55000),
 ("charger", 25,500),
 ("Earphones",30,800),
 ("charger", 20,500)
 ])

conn.commit()

#run sql and load into pandas
query = """select product,
sum(quantity) as total_qty,
sum(quantity * price) as revenue
from Sales
group by product 
"""

df = pd.read_sql_query(query,conn)
print(df)

# 4. plot revenue by product
ax = df.plot(kind='bar', x='product', y='revenue', legend=True)
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# 5. close the connection
conn.close()