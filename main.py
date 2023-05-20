import sqlite3, os
from flask import Flask, render_template, request, url_for, flash, redirect, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LeZeyede'


def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn


def get_book(book_id):
  conn = get_db_connection()
  book = conn.execute('SELECT * FROM books WHERE id = ?',
                      (book_id, )).fetchone()
  conn.close()
  if book is None:
    abort(404)
  return book


def get_order(order_id):
  conn = get_db_connection()
  order = conn.execute('SELECT * FROM orders WHERE id = ?',
                       (order_id, )).fetchone()
  conn.close()
  if order is None:
    abort(404)
  return order


def get_member(member_id):
  conn = get_db_connection()
  member = conn.execute('SELECT * FROM members WHERE id = ?',
                        (member_id, )).fetchone()
  conn.close()
  if member is None:
    abort(404)
  return member


def get_supplier(supplier_id):
  conn = get_db_connection()
  supplier = conn.execute('SELECT * FROM suppliers WHERE id = ?',
                          (supplier_id, )).fetchone()
  conn.close()
  if supplier is None:
    abort(404)
  return supplier


# @app.route('/index')
# def index():
#   return render_template('index.html', books=books)

@app.route('/')
def books():
  search_query = request.args.get('search_query', '')
  author_filter = request.args.get('author_filter', '')
  published_year_filter = request.args.get('published_year_filter', '')
  isbn_filter = request.args.get('isbn_filter', '')
  supplier_id_filter = request.args.get('supplier_id_filter', '')
  conn = get_db_connection()

  if search_query:
    books = conn.execute("SELECT * FROM books WHERE title LIKE ?",
                         ('%' + search_query + '%', )).fetchall()

  elif author_filter:
    base_query = " SELECT * FROM books WHERE author LIKE ?"
    query_args = ('%' + author_filter + '%', )

    if published_year_filter:
      base_query += " AND published_year LIKE ?"
      query_args += ('%' + published_year_filter + '%', )

    if isbn_filter:
      base_query += " AND isbn LIKE ?"
      query_args += ('%' + isbn_filter + '%', )

    if supplier_id_filter:
      base_query += " AND supplier_id LIKE ?"
      query_args += ('%' + supplier_id_filter + '%', )

    books = conn.execute(base_query, query_args).fetchall()

  else:
    books = conn.execute('SELECT * FROM books').fetchall()
  conn.close()
  return render_template('books.html', books=books)


@app.route('/orders')
def orders():
  search_query = request.args.get('search_query', '')
  conn = get_db_connection()
  if search_query:
    orders = conn.execute(
      'SELECT orders.id, books.title as book_title, members.name as member_name, orders.order_date, orders.return_date FROM orders JOIN books ON orders.book_id = books.id JOIN members ON orders.member_id = members.id WHERE book_title LIKE ?',
      ('%' + search_query + '%', )).fetchall()
  else:
    orders = conn.execute(
      'SELECT orders.id, books.title as book_title, members.name as member_name, orders.order_date, orders.return_date FROM orders JOIN books ON orders.book_id = books.id JOIN members ON orders.member_id = members.id'
    ).fetchall()
  conn.close()
  return render_template('orders.html', orders=orders)


@app.route('/members')
def members():
  search_query = request.args.get('search_query', '')
  conn = get_db_connection()
  if search_query:
    members = conn.execute("SELECT * FROM members WHERE name LIKE ?",
                           ('%' + search_query + '%', )).fetchall()
  elif search_query == '' or search_query == ' ':
    members = conn.execute('SELECT * FROM members').fetchall()
  else:
    members = conn.execute('SELECT * FROM members').fetchall()
  conn.close()
  return render_template('members.html', members=members)


@app.route('/suppliers')
def suppliers():
  search_query = request.args.get("search_query", '')
  conn = get_db_connection()
  if search_query:
    suppliers = conn.execute('SELECT * FROM suppliers WHERE name LIKE ?',
                             ('%' + search_query + '%', )).fetchall()
  else:
    suppliers = conn.execute('SELECT * FROM suppliers').fetchall()
  conn.close()
  return render_template('suppliers.html', suppliers=suppliers)


@app.route('/addBook/', methods=('GET', 'POST'))
def addBook():
  if request.method == 'POST':
    title = request.form['title']
    description = request.form['description']
    published_year = request.form['published_year']
    author = request.form['author']
    isbn = request.form['isbn']
    available_copies = request.form['available_copies']
    total_copies = request.form['total_copies']
    supplier_id = request.form['supplier_id']
    image = request.files.get('image')

    if not title:
      flash('Title is required!', 'error')
    elif not description:
      flash('Description is required!', 'error')
    elif not published_year:
      flash('Publication year is required!', 'error')
    elif not author:
      flash('Author Name is required!', 'error')
    elif not isbn:
      flash('ISBN is required!', 'error')
    elif not available_copies:
      flash('Available Copies is required!', 'error')
    elif not total_copies:
      flash('Total copies is required!', 'error')
    elif not supplier_id:
      flash('Supplier_ID is required!', 'error')
    else:
      image.save(os.path.join('static/images', image.filename))
      conn = get_db_connection()
      conn.execute(
        'INSERT INTO books (title, description, published_year, author, isbn, available_copies, total_copies, supplier_id, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (title, description, published_year, author, isbn, available_copies,
         total_copies, supplier_id, image.filename))
      conn.commit()
      conn.close()
      flash('Book added successfully!', 'success')
      return redirect(url_for('books'))

  return render_template('addBook.html')


@app.route('/addOrder/', methods=('GET', 'POST'))
def addOrder():
  if request.method == 'POST':
    book_id = request.form['book_id']
    member_id = request.form['member_id']
    order_date = request.form['order_date']
    return_date = request.form['return_date']

    if not book_id:
      flash('book ID is required!', 'error')
    elif not member_id:
      flash('member ID is required!', 'error')
    elif not order_date:
      flash('Order date is required!', 'error')
    else:
      conn = get_db_connection()
      conn.execute(
        'INSERT INTO orders (book_id, member_id, order_date, return_date) VALUES (?, ?, ?, ?)',
        (book_id, member_id, order_date, return_date))

      conn.commit()
      conn.close()
      flash('Order added successfully!', 'success')
      return redirect(url_for('orders'))

  return render_template('addOrder.html')


@app.route('/addMember/', methods=('GET', 'POST'))
def addMember():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    address = request.form['address']
    registration_date = request.form['registration_date']

    if not name:
      flash('Name is required!', 'error')
    elif not email:
      flash('Email is required!', 'error')
    elif not phone_number:
      flash('Phone number is required!', 'error')
    elif not address:
      flash('Address is required!', 'error')
    elif not registration_date:
      flash('Registration date is required!', 'error')
    else:
      conn = get_db_connection()
      conn.execute(
        'INSERT INTO members (name, email, phone_number, address, registration_date) VALUES (?, ?, ?, ?, ?)',
        (name, email, phone_number, address, registration_date))

      conn.commit()
      conn.close()
      flash('Member added successfully!', 'success')
      return redirect(url_for('members'))

  return render_template('addMember.html')


@app.route('/addSupplier/', methods=('GET', 'POST'))
def addSupplier():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    address = request.form['address']
    num_books_supplied = request.form['num_books_supplied']

    if not name:
      flash('Name is required!', 'error')
    elif not email:
      flash('Email is required!', 'error')
    elif not phone_number:
      flash('Phone number is required!', 'error')
    elif not address:
      flash('Address is required!', 'error')
    elif not num_books_supplied:
      flash('Total books supplied is required!', 'error')
    else:
      conn = get_db_connection()
      conn.execute(
        'INSERT INTO suppliers (name, email, phone_number, address, num_books_supplied) VALUES (?, ?, ?, ?, ?)',
        (name, email, phone_number, address, num_books_supplied))

      conn.commit()
      conn.close()
      flash('Supplier added successfully!', 'success')
      return redirect(url_for('suppliers'))

  return render_template('addSupplier.html')


@app.route('/<int:id>/editBook/', methods=('GET', 'POST'))
def editBook(id):
  book = get_book(id)

  if request.method == 'POST':
    title = request.form['title']
    description = request.form['description']
    published_year = request.form['published_year']
    author = request.form['author']

    if not title:
      flash('Title is required!', 'error')

    elif not description:
      flash('Description is required!', 'error')

    elif not published_year:
      flash('Publication year is required!', 'error')

    elif not author:
      flash('Author Name is required!', 'error')

    else:
      conn = get_db_connection()
      conn.execute(
        'UPDATE books SET title = ?, description = ?, published_year = ?, author = ?'
        ' WHERE id = ?', (title, description, published_year, author, id))
      conn.commit()
      conn.close()
      flash('Book edited successfully!', 'success')
      return redirect(url_for('books'))

  return render_template('editBook.html', book=book)


@app.route('/editOrder/<int:id>', methods=('GET', 'POST'))
def editOrder(id):
  order = get_order(id)

  if request.method == 'POST':
    book_id = request.form['book_id']
    member_id = request.form['member_id']
    order_date = request.form['order_date']
    return_date = request.form['return_date']

    if not book_id:
      flash('Book ID is required!', 'error')
    elif not member_id:
      flash('Member ID is required!', 'error')
    elif not order_date:
      flash('Order_date is required!', 'error')
    else:
      conn = get_db_connection()
      conn.execute(
        'UPDATE orders SET book_id = ?, member_id = ?, order_date = ?, return_date = ? WHERE id = ?',
        (book_id, member_id, order_date, return_date, id))
      conn.commit()
      conn.close()
      flash('Order edited successfully!', 'success')
      return redirect(url_for('orders'))

  return render_template('editOrder.html', order=order)


@app.route('/editMember/<int:id>', methods=('GET', 'POST'))
def editMember(id):
  member = get_member(id)

  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    address = request.form['address']
    registration_date = request.form['registration_date']

    if not name:
      flash('Name is required!', 'error')
    elif not email:
      flash('Email is required!', 'error')
    elif not phone_number:
      flash('Phone number is required!', 'error')
    elif not address:
      flash('Address is required!', 'error')
    elif not registration_date:
      flash('Registration date is required!', 'error')
    else:
      conn = get_db_connection()
      conn.execute(
        'UPDATE members SET name = ?, email = ?, phone_number = ?, address = ?, registration_date = ?'
        ' WHERE id = ?',
        (name, email, phone_number, address, registration_date, id))
      conn.commit()
      conn.close()
      flash('Member edited successfully!', 'success')
      return redirect(url_for('members'))

  return render_template('editMember.html', member=member)


@app.route('/editSupplier/<int:id>/', methods=('GET', 'POST'))
def editSupplier(id):
  supplier = get_supplier(id)

  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    address = request.form['address']
    num_books_supplied = request.form['num_books_supplied']

    if not name:
      flash('Name is required!', 'error')
    elif not email:
      flash('Email is required!', 'error')
    elif not phone_number:
      flash('Phone number is required!'), 'error'
    elif not address:
      flash('Address is required!', 'error')
    elif not num_books_supplied:
      flash('Total books supplied is required!', 'error')
    else:
      conn = get_db_connection()
      conn.execute(
        'UPDATE suppliers SET name = ?, email = ?, phone_number = ?, address = ?, num_books_supplied = ? WHERE id = ?',
        (name, email, phone_number, address, num_books_supplied, id))

      conn.commit()
      conn.close()
      flash('Supplier edited successfully!', 'success')
      return redirect(url_for('suppliers'))

  return render_template('editSupplier.html', supplier=supplier)


@app.route('/<int:id>/deleteBook/', methods=('POST', ))
def deleteBook(id):
  book = get_book(id)
  conn = get_db_connection()
  imagePath = 'static/images/' + book['image']
  os.remove(imagePath)
  conn.execute('DELETE FROM books WHERE id = ?', (id, ))
  conn.commit()
  conn.close()
  flash('"{}" was successfully deleted!'.format(book['title']), 'success')
  return redirect(url_for('books'))


@app.route('/orders/<int:id>/deleteOrder/', methods=('POST', ))
def deleteOrder(id):
  order = get_order(id)
  conn = get_db_connection()
  conn.execute('DELETE FROM orders WHERE id = ?', (id, ))
  conn.commit()
  conn.close()
  flash(
    'Order #{} for "{}" was successfully deleted!'.format(
      order['id'], order['id']), 'success')
  return redirect(url_for('orders'))


@app.route('/members/<int:id>/deleteMember/', methods=('POST', ))
def deleteMember(id):
  member = get_member(id)
  conn = get_db_connection()
  conn.execute('DELETE FROM members WHERE id = ?', (id, ))
  conn.commit()
  conn.close()
  flash('{} was successfully deleted!'.format(member['name']), 'success')
  return redirect(url_for('members'))


@app.route('/suppliers/<int:id>/deleteSupplier/', methods=('POST', ))
def deleteSupplier(id):
  supplier = get_supplier(id)
  conn = get_db_connection()
  conn.execute('DELETE FROM suppliers WHERE id = ?', (id, ))
  conn.commit()
  conn.close()
  flash('{} was successfully deleted!'.format(supplier['name']), 'success')
  return redirect(url_for('suppliers'))

if __name__ == "__main__":  
  app.run(host='0.0.0.0', port=81)
