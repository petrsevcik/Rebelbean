import sqlite3

def save_email_to_db(email):
    con = sqlite3.connect("rebelbean.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS emails (`email_id` INTEGER PRIMARY KEY, `email` varchar(255))""")
    cur.execute("""INSERT INTO emails
            ('email')
        VALUES
            (?)""", (email,))
    con.commit()
    con.close()
    print(f"email {email} saved to db!")
    return True

def save_test_roast_availability(date, availability):
    con = sqlite3.connect("rebelbean.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS testroast (`date` datetime, `availability` varchar(255))""")
    cur.execute("""INSERT INTO testroast
                ('date', 'status')
            VALUES
                (?, ?)""", date, availability)
    con.commit()
    con.close()
    print(f"data saved to db!")