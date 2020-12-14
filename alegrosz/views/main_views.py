from flask import Blueprint, render_template

from alegrosz.dbs.dbs import get_db

bp_main = Blueprint('main', __name__, url_prefix=('/'))


@bp_main.route('/')
def index():
    conn = get_db()
    c = conn.cursor()

    c.execute('''SELECT 
        i.id, i.title, i.price, i.image, c.name, s.name
        FROM
        item AS i
        INNER JOIN category AS c ON i.category_id = c.id
        INNER JOIN subcategory AS s ON i.subcategory_id = s.id
    ''')

    items_from_db = c.fetchall()

    items = []

    for row in items_from_db:
        item = {
            'id': row[0],
            'title': row[1],
            'price': row[2],
            'image': row[3],
            'category': row[4],
            'subcategory': row[5],
        }
        items.append(item)

    return render_template('index.html', items=items)
