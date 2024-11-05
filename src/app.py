from flask import Flask, jsonify, request
import sqlite3
import os

# Create the Flask app instance
app = Flask(__name__)

# Load the configuration from the Config class in config.py
app.config.from_object('config.Config')  # This loads the Config class from config.py

# Example of accessing the database URI from the config
db = app.config['DATABASE_URI']

def get_db():
    """Open a new database connection."""
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row 
    return con

def anilox_table():
    """Create the anilox table if it doesn't exist."""
    with get_db() as con:
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS anilox (
                "roller" TEXT,
                "lpi" INTEGER,
                "bcm" REAL,
                "clean_cycles" INTEGER DEFAULT 0,
                "milage" INTEGER DEFAULT 0,
                PRIMARY KEY("roller")
            );
        ''')
        con.commit()
# Run function to ensure table is created upon server startup if it doesn't already exist.
anilox_table()

@app.route('/')
def index():
    return 'AniTrac is running'

@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404

@app.route('/anilox_list', methods=['GET'])
def anilox_list():
    '''Return list of anilox data for display.'''
    with get_db() as con:
        cur = con.cursor()
        sort_metric = request.args.get('sort')
        sort_order = request.args.get('method')
        data = ['roller','asc']
        if sort_metric in ['anilox', 'milage','clean_cycles']:
            data[0] = sort_metric
        if sort_order in ['asc', 'desc']:
            data[1] = sort_order
        cur.execute(f'SELECT * FROM anilox order by {data[0]} {data[1]}')
        anilox = cur.fetchall()
    return jsonify([dict(roller) for roller in anilox]), 200

@app.route('/add_anilox', methods=['POST'])
def new_anilox() -> None:
    '''Add new anilox to database.'''
    record = request.json
    with get_db() as con:
        cur = con.cursor()
        check = cur.execute('select * from anilox where roller = ?', (record['roller'],)).fetchone()
        if check == None:
            cur.execute('INSERT INTO anilox (roller, lpi, bcm) VALUES (?, ?, ?)',
                        (record['roller'], record['lpi'], record['bcm']))
            con.commit()
            con.close()
            return jsonify({'message':'Anilox successfully added.', 'recieved' : record}), 201
        else:
            con.close()
            return jsonify({'message':'Anilox already exist.'}), 201

if __name__ == '__main__':
    app.run()
