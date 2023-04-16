import sqlite3 as sq3
from MyProfile import MyProfile
import json

# Connect to the database & create cursor
database = sq3.connect("./data/user_profiles.db")
cursor = database.cursor()

# Create the table
# cursor.execute("""CREATE TABLE user_profiles(
#     name TEXT,
#     year INTEGER,
#     majors TEXT,
#     classes TEXT,
#     hometown TEXT,
#     live TEXT,
#     clubs TEXT,
#     classPref TEXT,
#     pref TEXT
# )""")




p1 = MyProfile("Alice", 1, str(["Computer Science", "Psychology"]), "Taipei", "South", str(["x"]), 2, 2, 2)

p2 = MyProfile("Sam", 1, ["Computer Science"], "Chicago", "South", ["b"], 4, 4, 4)

cursor.execute("INSERT INTO user_profiles VALUES (?,?,?,?,?,?,?,?,?)", (p1.name, p1.year, p1.majors, p1.classes, p1.hometown, p1.live, p1.clubs, p1.classPref, p1.pref))



cursor.execute("INSERT INTO user_profiles VALUES(:name, :year, :majors, :classes, :hometown, :live, :clubs, :classPref, :pref)", 
                                                {
                                                'name': p1.name, 
                                                'year': p1.year, 
                                                'majors': p1.majors, 
                                                'classes': p1.classes, 
                                                'hometown': p1.hometown, 
                                                'live': p1.live, 
                                                'clubs': p1.clubs, 
                                                'classPref': p1.classPref, 
                                                'pref': p1.pref
                                                })
print(str)






# Commit commands & close connection to database
database.commit()
database.close()


