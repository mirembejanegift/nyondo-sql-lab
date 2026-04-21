import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# A
print(conn.execute("SELECT * FROM products").fetchall())

# B
print(conn.execute("SELECT name, price FROM products").fetchall())

# C
print(conn.execute("SELECT * FROM products WHERE id=3").fetchall())

# D
print(conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall())

# E
print(conn.execute("SELECT * FROM products ORDER BY price DESC").fetchall())

# F
print(conn.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall())

# G
conn.execute("UPDATE products SET price=38000 WHERE id=1")
conn.commit()
print(conn.execute("SELECT * FROM products").fetchall())