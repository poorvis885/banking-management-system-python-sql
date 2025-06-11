from db_config import get_connection

def view_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, balance, status FROM users")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def freeze_account(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET status = 'frozen' WHERE email = %s", (email,))
    conn.commit()
    conn.close()
    print("🧊 Account frozen.")

def activate_account(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET status = 'active' WHERE email = %s", (email,))
    conn.commit()
    conn.close()
    print("✅ Account activated.")

print("admin successful...")
