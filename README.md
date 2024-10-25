# REGISTRATION-FORM
This registration form is designed to collect user information for account creation. It uses Streamlit for the user interface and SQLite for data storage.
<br>
**Features** <br>
->User-friendly registration form with validation. <br>
->Stores user information in an SQLite database. <br>
->Supports various input types (text, number, radio buttons, dropdowns).


<br>

**Install required library** <br>
            
    pip install streamlit <br>


**How to run the application**<br>

    streamlit run app.py <br>


**To check the data base**<br>
  ->Using SQLite Command Line:<br>

  Open your terminal or command prompt.<br>
  Run the SQLite command line interface:
  
    sqlite3 registrations.db


  **To see the data, you can execute:**  <br>

    SELECT * FROM users;
    
