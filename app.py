from flask import Flask, render_template, request, g
import sqlite3
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'static'),
)

app.config.setdefault('DATABASE', os.path.join(app.root_path, 'brands.db'))


def get_db():
    if 'db' not in g:
        db_path = app.config['DATABASE']

        g.db = sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
        
    return g.db

@app.teardown_appcontext
def close_db(exception):
    """Close the database connection for the current request if it exists."""
    db = g.pop('db', None)

    if db is not None:
        db.close()

@app.route('/')
def home():
    # Home
    db = get_db()
    cursor = db.cursor()
    sql = "SELECT * FROM brands"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("home.html", results = results)

@app.route("/brand/<int:brand_id>")
def brand(brand_id):
    db = get_db()
    cursor = db.cursor()
    sql = """
        SELECT brands.brand_id, brands.brand, brands.net_worth, brands.founded, brands.logo, ceo.name, fastest_car.fastest_car FROM brands
        JOIN ceo ON ceo.ceo_id = brands.ceo_id
        JOIN fastest_car ON fastest_car.fastest_car_id = brands.fastest_car_id
        WHERE brands.brand_id = ?"""
    cursor.execute(sql, (brand_id,))    
    result = cursor.fetchone()
    return render_template("brand.html", brand=result)

if __name__ == "__main__":
    app.run(debug=True)