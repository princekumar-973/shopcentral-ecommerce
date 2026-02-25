# shopcentral-ecommerce
A full-featured ecommerce website built with Django — dark premium theme, shopping cart, user authentication, order management and admin panel.

# 🛒 ShopCentral

> A full-featured Django ecommerce website with dark premium theme, shopping cart, user authentication and order management.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 🏠 **Homepage** — Hero section, featured products, categories
- 🛍️ **Product Catalog** — Browse and filter by category
- 🛒 **Shopping Cart** — Session-based cart with quantity management
- 👤 **User Authentication** — Register with email, login, logout
- 📦 **Order Management** — Place orders, track order history
- 📍 **Delivery Address** — Enter address at checkout, saved to profile
- 💳 **Payment Options** — UPI, Card, Net Banking, Cash on Delivery
- 🎨 **Dark Premium Theme** — Obsidian + gold aesthetic
- 📱 **Responsive Design** — Works on mobile, tablet and desktop
- ⚙️ **Admin Panel** — Manage products, categories, orders and users

---

## 🖥️ Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.14 | Backend language |
| Django | 6.0 | Web framework |
| Bootstrap | 5.3 | Frontend styling |
| SQLite | Default | Database |
| Pillow | Latest | Image handling |
| Google Fonts | — | Typography (Cormorant Garamond + Syne) |

---

## 📁 Project Structure

```
shopcentral/
├── ecommerce/              ← Django config
│   ├── settings.py         ← project settings
│   ├── urls.py             ← main URL router
│   └── wsgi.py
├── store/                  ← products & orders app
│   ├── models.py           ← Category, Product, Order, OrderItem
│   ├── views.py            ← page logic
│   ├── urls.py             ← store routes
│   ├── cart.py             ← session cart
│   └── admin.py
├── accounts/               ← user auth app
│   ├── models.py           ← Profile model
│   ├── views.py            ← register, profile, dashboard
│   ├── forms.py            ← RegisterForm, ProfileUpdateForm
│   ├── urls.py             ← accounts routes
│   ├── signals.py          ← auto-create profile on register
│   └── admin.py
├── templates/              ← all HTML templates
│   ├── base.html           ← navbar + footer
│   ├── registration/
│   │   └── login.html
│   ├── store/
│   │   ├── home.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── order_success.html
│   │   └── my_orders.html
│   └── accounts/
│       ├── register.html
│       ├── dashboard.html
│       └── profile.html
├── static/
│   └── css/
│       └── style.css       ← dark theme CSS
├── .gitignore
├── requirements.txt
└── manage.py
```

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/shopcentral.git
cd shopcentral
```

### 2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Open in browser
```
http://127.0.0.1:8000/
```

---

## 🔗 URL Map

| URL | Page |
|---|---|
| `/` | Homepage |
| `/products/` | All products |
| `/product/<slug>/` | Product detail |
| `/cart/` | Shopping cart |
| `/order/place/` | Place order |
| `/order/success/<id>/` | Order success |
| `/orders/` | My orders |
| `/accounts/register/` | Register |
| `/accounts/login/` | Login |
| `/accounts/dashboard/` | Account dashboard |
| `/accounts/profile/` | Edit profile |
| `/admin/` | Admin panel |

---

## ⚙️ Admin Panel

Visit `/admin/` and login with your superuser credentials.

You can manage:
- ✅ **Categories** — add/edit/delete product categories
- ✅ **Products** — add products with images, price, stock
- ✅ **Orders** — view all orders, update order status
- ✅ **Users** — manage registered users and their profiles

---

## 🗃️ Database Models

### Category
```
name, slug
```

### Product
```
category, name, slug, description,
price, original_price, image, stock, available
```

### Order
```
user, status, payment_method, total_amount,
address, city, state, pincode, created_at
```

### OrderItem
```
order, product, quantity, price
```

### Profile
```
user, phone, address, city,
state, pincode, avatar
```

---

## 🛒 How It Works

```
Customer Journey:

Register/Login
     ↓
Browse Products
     ↓
Add to Cart (session-based)
     ↓
Enter Delivery Address
     ↓
Select Payment Method
     ↓
Place Order (saved to database)
     ↓
Order Success Page
     ↓
View in My Orders
```

---

## 🎨 Theme

- **Background** — Deep obsidian `#0a0a0f`
- **Accent** — Electric gold `#c9a84c`
- **Text** — Warm white `#f0ede8`
- **Font (Display)** — Cormorant Garamond
- **Font (Body)** — Syne

---

## 📸 Media Files

Product images and user avatars are stored in the `media/` folder.

Make sure `settings.py` has:
```python
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🔒 Environment Variables

For production, move these to a `.env` file:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
```

---

## 📦 Requirements

```
Django==6.0.2
Pillow
```

Generate with:
```bash
pip freeze > requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch `git checkout -b feature/your-feature`
3. Commit changes `git commit -m "Add your feature"`
4. Push to branch `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built with ❤️ using Django and Bootstrap 5.

---

⭐ If you found this helpful, give it a star on GitHub!
