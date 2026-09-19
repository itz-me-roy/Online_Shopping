# Online Shopping (Django)

A small but complete e-commerce storefront: product catalog, categories,
session-based cart, checkout, order history, and user accounts.

## Features
- **Catalog** — categories + products, with an admin-managed image, price, and stock.
- **Cart** — session-based (works for anonymous visitors), add/update/remove items.
- **Checkout** — collects shipping details, creates an `Order` + `OrderItem`s, decrements stock.
- **Accounts** — sign up, log in/out, and a "My orders" history page for logged-in users.
- **Admin** — full Django admin for managing categories, products, and orders (with inline order items).

## Project layout
```
online_shopping/
├── manage.py
├── requirements.txt
├── shopping_project/       # settings, root urls
├── shop/                   # the app: models, views, cart, forms, admin, templates
│   └── management/commands/seed_data.py   # optional sample data
├── templates/base.html     # shared site layout
└── static/css/style.css
```

## Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations shop
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data          # optional: adds sample categories/products
python manage.py runserver
```
Visit http://127.0.0.1:8000/ for the storefront and
http://127.0.0.1:8000/admin/ to manage products/orders.

## How the cart works
`shop/cart.py` defines a `Cart` class that stores `{product_id: {quantity, price}}`
in the session (`request.session['cart']`) — no login required, and it survives
across page loads for that browser. A context processor
(`shop.context_processors.cart`) makes it available in every template, which is
how the header cart-count badge works.

## Notes / where to take it further
- Payments aren't wired up — `order_create` just records the order as `pending`.
  Adding Stripe/PayPal would mean creating a payment intent after the order is
  saved and redirecting to a payment page before showing the confirmation.
- Product search/filtering is minimal (category only) — easy to extend with a
  search box using `Product.objects.filter(name__icontains=...)`.
- No pagination on the product list yet — add Django's `Paginator` once the
  catalog grows.
