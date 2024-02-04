DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- Create the authors table first as it has no foreign keys

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT, 
    last_name TEXT,
    year_born INTEGER
);

-- Create the books table

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);