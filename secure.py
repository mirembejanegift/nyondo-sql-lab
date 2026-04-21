import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# Secure product search using parameterised query
def search_product_safe(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, ('%' + name + '%',)).fetchall()
    return rows


# -------------------
# TESTS (same attacks as before)
# -------------------

print("Test 1:", search_product_safe("' OR 1=1--"))
print("Test 2:", search_product_safe("' OR '1'='1"))
print("Test 3:", search_product_safe("anything' OR 'x'='x"))