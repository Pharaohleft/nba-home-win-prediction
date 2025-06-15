from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'change-this-secret-key'

# Simple in-memory product catalog
PRODUCTS = [
    {
        'id': 1,
        'name': 'T-Shirt',
        'category': 'clothes',
        'price': 19.99,
        'image': 'https://via.placeholder.com/150'
    },
    {
        'id': 2,
        'name': 'Jeans',
        'category': 'clothes',
        'price': 39.99,
        'image': 'https://via.placeholder.com/150'
    },
    {
        'id': 3,
        'name': 'Sneakers',
        'category': 'shoes',
        'price': 59.99,
        'image': 'https://via.placeholder.com/150'
    },
    {
        'id': 4,
        'name': 'Boots',
        'category': 'shoes',
        'price': 79.99,
        'image': 'https://via.placeholder.com/150'
    },
]


def get_cart():
    """Return the shopping cart from session or create a new one."""
    if 'cart' not in session:
        session['cart'] = {}
    return session['cart']


@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)


@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    cart = get_cart()
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))


@app.route('/cart')
def cart():
    cart = get_cart()
    items = []
    total = 0
    for pid, qty in cart.items():
        product = next((p for p in PRODUCTS if p['id'] == int(pid)), None)
        if product:
            subtotal = product['price'] * qty
            total += subtotal
            items.append({'product': product, 'qty': qty, 'subtotal': subtotal})
    return render_template('cart.html', items=items, total=total)


if __name__ == '__main__':
    app.run(debug=True)
