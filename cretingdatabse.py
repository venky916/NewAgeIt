import os
import sqlite3

current_dir = os.getcwd()
two_steps_back_dir = os.path.dirname(current_dir)
db_file_path = os.path.join(two_steps_back_dir, "projects", "execution_folder", "config_folder", "config_file_abc9003.db")

conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Create the 'testdatatable' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS testdatatable (
        title TEXT,
        data TEXT
    )
''')

values = ["channel", "proposalno", "salutation", "dob", "gender", "annutype", "defermentperiod", "subplan",
          "annuitypayoutfreq", "purchaseprice", "annuitypurchaseprice", "joint", "sys_id", "Product name",
          "Proposal Category", "SA", "Frequency", "Country", "Nationality", "AgeProofDocument",
          "Hazard", "SBI", "Deferment period", "HEIGHT", "WEIGHT", "BP", "Smoking", "Proofofidentity",
          "channel2", "Premium Payment Term", "Proposal Category1", "Date", "MaritalStatus", "Resident",
          "PostalCode", "Payout period", "Guarrented income", "Policy term", "occupation2"]

for val in values:
    title = val
    data = None  # Set data to None for now, you can change this as needed
    print(title, data)
    cursor.execute('''
        INSERT INTO testdatatable (title, data) VALUES (?, ?)
    ''', (title, data))
    
# Commit the changes to the database
conn.commit()
conn.close()

print("Table created and data inserted.")
