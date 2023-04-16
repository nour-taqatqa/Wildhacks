import sqlite3 as sq3

# Connect to the database & create cursor
database = sq3.connect("Wildhacks/data/user_profiles.db")
cursor = database.cursor()

# Create the table
cursor.execute("""CREATE TABLE user_profiles(
    username TEXT,
    first_name TEXT,
    last_name TEXT
)""")

cursor.execute("INSERT INTO user_profiles VALUES ('March7th', 'Michael', 'Lee')")












# Commit commands & close connection to database
database.commit()
database.close()


