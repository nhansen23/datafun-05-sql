import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root directory project
db_file = pathlib.Path("project.db")

def create_database():
    '''Function to create a database. Connecting for the 
       first time will create a new database file if it 
       doesn't exist yet.  Close the connection after
       creating the database to avoid locking the file.'''
    try:
        connection = sqlite3.connect(db_file)
        connection.close
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    '''Function to read and execute SQL statements
       to create tables'''
    try:
        with sqlite3.connect(db_file) as connection:
            sql_file = pathlib.Path("sql","create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            connection.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    '''Function to use pandas to read data from CSV file
       in data folder and insert the recods into the 
       appropriate table.'''
    try:
        author_data_path = pathlib.Path("data","authors.csv")
        book_data_path = pathlib.Path("data","books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as connection:
            authors_df.to_sql("authors", connection, if_exists="replace", index=False)
            books_df.to_sql("books", connection, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
