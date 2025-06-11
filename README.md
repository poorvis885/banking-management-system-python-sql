# 🏦 Banking Management System 

A command-line based Banking Management System built using Python and MySQL. This project supports essential banking operations like registration, login, deposit, withdrawal, money transfer, balance checking, and viewing transaction history. The system is modular, secure, and ready for commercial scalability.

---

## 📌 Features

- 🧾 User Registration & Login (with password hashing)
- 💳 Deposit, Withdraw, and Transfer Money
- 📈 View Transaction History
- 🔐 Admin and User Role Support (customizable)
- 🗃️ MySQL Database Integration with Foreign Key Constraints
- 📤 Well-structured modular code (`auth.py`, `transactions.py`, etc.)
- 📊 Ready for GUI / Web App / Data Visualization extensions

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3.13
- **Database:** MySQL Workbench
- **Libraries:**
  - `mysql-connector-python`
  - `hashlib` (for password encryption)
  - `datetime`
  - `getpass` (for secure input)

---

## 🗂️ Project Structure

banking-management-system/
│
├── main.py # CLI application entry point
├── auth.py # Handles user registration & login
├── transactions.py # Deposit, withdraw, transfer logic
├── db_config.py # MySQL DB connection setup
├── schema.sql # SQL script to create users & transactions tables


---

## 🧪 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/poorvis885/banking-management-system-python-sql.git
cd banking-management-system-python-sql
