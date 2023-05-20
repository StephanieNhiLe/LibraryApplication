import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('The Alchemist', 'Paulo Coelho', 1988, '0061122416', 20, 15, 2,
   'A novel that follows the journey of a shepherd boy who seeks his personal legend through a series of omens.',
   'alchemist.jpg'))

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('To Kill a Mockingbird', 'Harper Lee', 1960, '0446310786', 20, 15, 3,
   'A novel set in the Southern United States during the Great Depression, and is narrated by the protagonist, a young girl named Scout Finch.',
   'TKLMB.jpg'))

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('The 48 Laws of Power', 'Robert Greene', 1998, '0140280197', 25, 20, 4,
   'A non-fiction book that teaches readers how to gain and maintain power through the use of 48 laws that apply in politics, business, and everyday life.',
   '48LAWS.jpg'))

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('The Hobbit', 'J.R.R. Tolkien', 1937, '054792822X', 30, 25, 1,
   'A fantasy novel that follows the adventure of Bilbo Baggins, a hobbit who embarks on a quest to reclaim the lost treasure of Erebor.',
   'hobbit.jpg'))

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('Pride and Prejudice', 'Jane Austen', 1813, '1503290561', 15, 10, 5,
   'A romantic novel that follows the story of Elizabeth Bennet, one of five daughters of a country gentleman, as she navigates issues of manners, upbringing, morality, education, and marriage.',
   'pride.jpg'))

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('The Da Vinci Code', 'Dan Brown', 2003, '1400079179', 35, 30, 3,
   'A mystery novel that follows symbologist Robert Langdon and cryptologist Sophie Neveu as they investigate a murder in Paris and uncover a conspiracy to protect a secret that has been guarded by a clandestine society for two thousand years.',
   'davinci.jpg'))

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('The Catcher in the Rye', 'J.D. Salinger', 1951, '0316769487', 20, 18, 6,
   'A novel that follows the story of Holden Caulfield, a teenager who is expelled from his school and roams around New York City.',
   'catcher.jpg'))

cur.execute(
  "INSERT INTO books (title, author, published_year, isbn, total_copies, available_copies, supplier_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
  ('The Picture of Dorian Gray', 'Oscar Wilde', 1890, '0141439573', 20, 15, 3,
   'A novel that tells the story of a young man named Dorian Gray, who becomes obsessed with his own beauty and youthfulness and is willing to do anything to maintain them, even if it means committing immoral acts.',
   'dorian.jpg'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('John Doe', 'johndoe@example.com', '123-456-7890', '123 Main St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Jane Smith', 'janesmith@example.com', '123-456-7890', '456 Oak St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Bob Johnson', 'bobjohnson@example.com', '123-456-7890', '789 Maple St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Sara Davis', 'saradavis@example.com', '234-567-8901', '321 Elm St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Mike Brown', 'mikebrown@example.com', '234-567-8901', '654 Pine St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Emily Nguyen', 'emilynguyen@example.com', '234-567-8901', '987 Cedar St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('David Lee', 'davidlee@example.com', '234-567-8901', '741 Birch St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Grace Kim', 'gracekim@example.com', '234-567-8901', '852 Oakwood St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Adam Patel', 'adampatel@example.com', '234-567-8901', '963 Elmwood St'))

cur.execute(
  "INSERT INTO members (name, email, phone_number, address) VALUES (?, ?, ?, ?)",
  ('Lily Chen', 'lilychen@example.com', '234-567-8901', '159 Maplewood St'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)",
  (3, 3, '2022-01-15', '2022-02-15'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)",
  (4, 4, '2022-02-05', '2022-03-05'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date) VALUES (?, ?, ?)",
  (5, 5, '2022-04-20'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)",
  (6, 6, '2022-05-01', '2022-06-01'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date) VALUES (?, ?, ?)",
  (7, 7, '2022-06-15'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)",
  (8, 8, '2022-07-01', '2022-08-01'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)",
  (9, 9, '2022-09-01', '2022-10-01'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)",
  (1, 1, '2022-01-01', '2022-02-01'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)",
  (1, 2, '2022-03-01', '2022-04-01'))

cur.execute(
  "INSERT INTO orders (book_id, member_id, order_date) VALUES (?, ?, ?)",
  (2, 2, '2022-05-01'))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('ABC Company', 'abc@example.com', '123-456-7890',
   '123 Main St, Anytown, USA', 103))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('XYZ Corporation', 'xyz@example.com', '555-555-5555',
   '456 Broadway, Anytown, USA', 73))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('123 Enterprises', '123@example.com', '987-654-3210',
   '789 Elm St, Anytown, USA', 50))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('Book Haven', 'bookhaven@example.com', '123-456-7890',
   '1234 Main St, Anytown, USA', 250))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('The Bookshelf', 'bookshelf@example.com', '555-555-5555',
   '456 Oak St, Anytown, USA', 180))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('Readers Choice', 'readerschoice@example.com', '987-654-3210',
   '789 Maple St, Anytown, USA', 110))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('Book Paradise', 'bookparadise@example.com', '123-456-7890',
   '321 Elm St, Anytown, USA', 320))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('Book World', 'bookworld@example.com', '555-555-5555',
   '789 Broadway, Anytown, USA', 140))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('Reader Haven', 'readerhaven@example.com', '987-654-3210',
   '1234 Oak St, Anytown, USA', 90))

cur.execute(
  "INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)",
  ('Books R Us', 'booksrus@example.com', '123-456-7890',
   '789 Main St, Anytown, USA', 200))

connection.commit()
connection.close()
