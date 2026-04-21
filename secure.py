import sqlite3

conn = sqlite3.connect('nyondo_stock.db')


# ---------------------------
# VALIDATION
# ---------------------------

def validate_input(text):
    return (
        isinstance(text, str)
        and len(text) >= 2
        and "<" not in text
        and ">" not in text
        and ";" not in text
    )


# ---------------------------
# SECURE FUNCTION
# ---------------------------

def search_product_safe(name):

    if not validate_input(name):
        print("Invalid input detected!")
        return None

    query = "SELECT * FROM products WHERE name LIKE ?"
    return conn.execute(query, ('%' + name + '%',)).fetchall()


# ---------------------------
# TEST CASES (TASK 5 REQUIREMENT)
# ---------------------------

print("Test 1:", search_product_safe("cement"))
print("Test 2:", search_product_safe(""))
print("Test 3:", search_product_safe("<script>"))
print("Test 4:", search_product_safe("' OR 1=1--"))