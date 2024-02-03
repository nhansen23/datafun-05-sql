import sqlite3
import pandas as pd
import pathlib

connection = sqlite3.connect("project.sqlite3")
'''
query1 = pd.read_sql('SELECT * FROM authors', connection, index_col=['author_id'])
print(f"Query 1 results: \n", query1)

query2 = pd.read_sql(
    'SELECT DISTINCT last, first FROM authors ORDER BY last, first', connection
    )
print(f"Query 2 results: \n", query2)

query3 = pd.read_sql(
    'SELECT book_id, title, year_published FROM books', connection
    )
print(f"Query 3 results: \n",query3)

query4 = pd.read_sql(
    'SELECT year_published, title, first, last FROM books INNER JOIN authors on books.author_id = authors.author_id ORDER BY year_published DESC', connection
    )
print(f"Query 4 results: \n",query4)

query5 = pd.read_sql(
    'SELECT year_published, title, first, last FROM books INNER JOIN authors on books.author_id = authors.author_id WHERE year_published < 1960 ORDER BY year_published DESC', connection
    )
print(f"Query 5 results: \n",query5)


query6 = pd.read_sql(
    'SELECT COUNT(*) FROM authors', connection
    )
print(f"Query 6 results: \n",query6)

query7 = pd.read_sql(
    'SELECT COUNT(*) FROM books WHERE year_published < 1945', connection
    )
print(f"Query 7 results: \n",query7)
'''
query8 = pd.read_sql(
    'SELECT year_published, COUNT(book_id) FROM books GROUP BY year_published', connection
    )
print(f"Query 8 results: \n", query8)