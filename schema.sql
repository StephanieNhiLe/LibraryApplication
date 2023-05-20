DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    author TEXT NOT NULL,
    published_year INTEGER NOT NULL,
    isbn TEXT,
    total_copies INTEGER,
    available_copies INTEGER,
    image TEXT,
    supplier_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

DROP TABLE IF EXISTS members;
CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    address TEXT NOT NULL,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS suppliers;
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    address TEXT NOT NULL,
    num_books_supplied INTEGER NOT NULL
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);
