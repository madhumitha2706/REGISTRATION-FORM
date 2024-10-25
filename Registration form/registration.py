import streamlit as st
import sqlite3
from datetime import datetime

# Initialize database connection
def create_table():
    con = sqlite3.connect('registrations.db')
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (name TEXT, email TEXT, password TEXT, age INTEGER, gender TEXT,phone_number INTEGER,Address TEXT, country TEXT, date TEXT)''')
    con.commit()
    con.close()

def add_user(name, email, password, age, gender,phone_number,Address, country, date):
    con = sqlite3.connect('registrations.db')
    c = con.cursor()
    c.execute("INSERT INTO users (name, email, password, age, gender,phone_number,address, country, date) VALUES (?,?,?,?,?,?,?,?,?)", 
              (name, email, password, age, gender,phone_number,Address,country, date))
    con.commit()
    con.close()

# Streamlit registration form
def main():
    st.title("User Registration Form")

    # Form fields
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    gender = st.radio("Gender", ("Male", "Female", "Other"))
    phone_number=st.text_input("Phone number :")
    Address=st.text_area("Address",height=100)
    country = st.selectbox("Country", ["United States", "Canada", "India", "Other"])
    terms = st.checkbox("I agree to the Terms and Conditions")

    # Submit Button
    if st.button("Register"):
        if terms:
            create_table()  # Ensure the table exists
            current_date = datetime.now().strftime("%Y-%b-%d %H:%M:%S")
            add_user(name, email, password, age, gender,phone_number,Address, country, current_date)
            st.success("Registration successful!")
            st.write("Thank you for registering.")
        else:
            st.error("You must agree to the Terms and Conditions to register.")

if __name__ == "__main__":
    main()
