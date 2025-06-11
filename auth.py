'''import bcrypt
from db_config import get_connection

def register_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed))
        conn.commit()
        print("✅ Registration successful.")
    except:
        print("❌ Email already exists.")
    conn.close()

def login(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, password, role FROM users WHERE email = %s AND status = 'active'", (email,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode(), user[2].encode()):
        print(f"\n👋 Welcome, {user[1]} ({user[3]})")
        return {'id': user[0], 'name': user[1], 'role': user[3]}
    else:
        print("❌ Invalid credentials or account frozen.")
        return None'''
from db_config import get_connection
import hashlib

def register_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # optional: hash password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, hashed_password))
        conn.commit()
        print("✅ Registration successful.")
    except Exception as e:
        conn.rollback()
        print(f"❌ Registration failed: {e}")
    finally:
        conn.close()

def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT id, name, password, email FROM users WHERE email = %s AND password = %s",
                       (email, hashed_password))
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return None
    finally:
        conn.close()


print("auth successful......")
