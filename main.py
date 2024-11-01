from flask import Flask, request, jsonify
import sqlite3 as sq3
import os

database = os.path.join(os.getcwd(),'data', 'anitrac.db')

app = Flask(__name__)

def get_db() -> None:
  """Create a connection to the anilox database."""
    con = sq3.connect(database)
    con.row_factory = sq3.Row
    return con

@app.route('/')
def index():
  """Create homepage for website."""
    # This will eventually be udpated to display information about anitrac.
    return "Welcome to Anitrac", 200

def create_anilox_table() -> None:
  """Create database and anilox table."""
    con = get_db()
    cur = con.cursor()
    cur.execute(
            '''CREATE TABLE IF NOT EXISTS anilox (
                "roller"	TEXT,
                "lpi"	INTEGER,
                "bcm"	REAL,
                "clean_cycles"	INTEGER DEFAULT 0,
                "milage"	INTEGER DEFAULT 0,
                PRIMARY KEY("roller")
            );''')
    con.commit()
    con.close()

@app.route('/anilox_list', methods=['GET'])
def anilox_list():
  """Return list of anilox with their clean cycle and recorded milage."""
    con = get_db()
    cur = con.cursor()
    # Grab search queries from url to organize data from sql query
    sort_metric = request.args.get('sort')
    sort_order = request.args.get('method')
    # Set default data to populate in case no filtering is required from the end user. 
    data = ['roller','asc']
    # Simplstic protection against sql injection via verifying search against acceptable values.
    if sort_metric in ['anilox', 'milage','clean_cycles']:
        data[0] = sort_metric
    if sort_order in ['asc', 'desc']:
        data[1] = sort_order
    cur.execute(f'SELECT * FROM anilox order by {data[0]} {data[1]}')
    anilox = cur.fetchall()
    con.close()
    return jsonify([dict(roller) for roller in anilox]), 200

    
if __name__ == '__main__':
    # Verify database and table existance, else create database and table
    if not os.path.exists(database):
        with open(database, 'w'):
            create_anilox_table()
    # Run flask server.
    app.run()
