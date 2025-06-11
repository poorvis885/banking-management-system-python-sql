'''from db_config import get_connection

def get_balance(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

def deposit(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, user_id))
        cursor.execute("""
            INSERT INTO transactions (user_id, type, amount)
            VALUES (%s, 'deposit', %s)
        """, (user_id, amount))
        conn.commit()
        balance = get_balance(user_id)
        print(f"✅ Deposit successful. 💰 New balance: ₹{balance:.2f}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Deposit failed: {e}")
    finally:
        conn.close()

def withdraw(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]

    if balance < amount:
        print("❌ Not enough balance.")
        conn.close()
        return

    try:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, user_id))
        cursor.execute("""
            INSERT INTO transactions (user_id, type, amount)
            VALUES (%s, 'withdraw', %s)
        """, (user_id, amount))
        conn.commit()
        new_balance = get_balance(user_id)
        print(f"✅ Withdrawal successful. 💸 Remaining balance: ₹{new_balance:.2f}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Withdrawal failed: {e}")
    finally:
        conn.close()

def transfer(user_id, to_email, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (to_email,))
    recipient = cursor.fetchone()

    if not recipient:
        print("❌ Recipient not found.")
        conn.close()
        return

    to_user_id = recipient[0]
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]

    if balance < amount:
        print("❌ Not enough balance.")
        conn.close()
        return

    try:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, user_id))
        cursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, to_user_id))
        cursor.execute("""
            INSERT INTO transactions (user_id, type, amount, to_user)
            VALUES (%s, 'transfer', %s, %s)
        """, (user_id, amount, to_user_id))
        conn.commit()
        new_balance = get_balance(user_id)
        print(f"✅ ₹{amount:.2f} transferred to {to_email}. 🏦 New balance: ₹{new_balance:.2f}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Transfer failed: {e}")
    finally:
        conn.close()'''
from db_config import get_connection

def get_balance(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

def deposit(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, user_id))
        cursor.execute("""
            INSERT INTO transactions (user_id, type, amount)
            VALUES (%s, 'deposit', %s)
        """, (user_id, amount))
        conn.commit()
        balance = get_balance(user_id)
        print(f"✅ Deposit successful. 💰 New balance: ₹{balance:.2f}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Deposit failed: {e}")
    finally:
        conn.close()

def withdraw(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]

    if balance < amount:
        print("❌ Not enough balance.")
        conn.close()
        return

    try:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, user_id))
        cursor.execute("""
            INSERT INTO transactions (user_id, type, amount)
            VALUES (%s, 'withdraw', %s)
        """, (user_id, amount))
        conn.commit()
        new_balance = get_balance(user_id)
        print(f"✅ Withdrawal successful. 💸 Remaining balance: ₹{new_balance:.2f}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Withdrawal failed: {e}")
    finally:
        conn.close()

def transfer(user_id, to_email, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (to_email,))
    recipient = cursor.fetchone()

    if not recipient:
        print("❌ Recipient not found.")
        conn.close()
        return

    to_user_id = recipient[0]
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]

    if balance < amount:
        print("❌ Not enough balance.")
        conn.close()
        return

    try:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, user_id))
        cursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, to_user_id))
        cursor.execute("""
            INSERT INTO transactions (user_id, type, amount, to_user)
            VALUES (%s, 'transfer', %s, %s)
        """, (user_id, amount, to_user_id))
        conn.commit()
        new_balance = get_balance(user_id)
        print(f"✅ ₹{amount:.2f} transferred to {to_email}. 🏦 New balance: ₹{new_balance:.2f}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Transfer failed: {e}")
    finally:
        conn.close()

def view_transactions(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, type, amount, to_user, timestamp 
            FROM transactions 
            WHERE user_id = %s 
            ORDER BY timestamp DESC
        """, (user_id,))
        rows = cursor.fetchall()

        if not rows:
            print("📭 No transactions found.")
        else:
            print("\n📋 Transaction History:")
            print("-" * 60)
            for row in rows:
                trans_id, trans_type, amount, to_user, ts = row
                if trans_type == "transfer":
                    print(f"ID: {trans_id} | Type: {trans_type} | ₹{amount:.2f} to UserID {to_user} | {ts}")
                else:
                    print(f"ID: {trans_id} | Type: {trans_type} | ₹{amount:.2f} | {ts}")
            print("-" * 60)
    except Exception as e:
        print(f"❌ Failed to retrieve transactions: {e}")
    finally:
        conn.close()



print("transaction successful...")
