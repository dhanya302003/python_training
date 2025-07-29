import mysql.connector

def insert_data(id, name, email):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="roottoor",
            database="dhanya_ece"
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO user (id, name, email) VALUES (%s, %s, %s)"
        val = (id, name, email)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error as err:
        print("Database error:", err)

    finally:
        mycursor.close()
        mydb.close()

# Input handling
try:
    id = int(input("Enter the ID (integer): "))
    name = input("Enter the name: ")
    email = input("Enter the email: ")

    insert_data(id, name, email)

except ValueError:
    print("Invalid ID. Please enter an integer.")
