


# 🛍️ Puddle - Online Marketplace

A modern Django-based marketplace where users can buy and sell items with features like shopping cart, reviews, and real-time messaging.

![Django](https://img.shields.io/badge/Django-4.1.5-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38bdf8)

## ✨ Features

### 🛒 Shopping & Browsing
- Browse items with category filtering
- Advanced search functionality
- Shopping cart with quantity management
- Product reviews and ratings
- Related items recommendations
- Responsive design for all devices

### 👤 User Management
- User registration and authentication
- Personal dashboard for sellers
- Profile management
- Secure login/logout

### 💬 Communication
- Direct messaging system between buyers and sellers
- Conversation inbox
- Real-time message notifications

### 📊 Seller Features
- Add, edit, and delete items
- Mark items as sold
- View all listed items in dashboard
- Upload product images
- Set prices and descriptions

### 🎨 UI/UX Improvements
- Modern, clean interface with Tailwind CSS
- Consistent card designs across all pages
- Fixed-size product images (uniform display)
- Success/error message notifications
- Smooth hover effects and transitions
- Mobile-responsive navigation
- Professional color scheme

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
pip (Python package manager)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/puddle.git
cd puddle
```

2. **Install dependencies**
```bash
pip install Django==4.1.5
pip install Pillow
```

3. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create a superuser**
```bash
python manage.py createsuperuser
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Access the application**
- Main site: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
puddle/
├── core/                   # Core app (home, auth, about, contact)
│   ├── templates/
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── item/                   # Items app (products, cart, reviews)
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── conversation/           # Messaging system
│   ├── templates/
│   ├── models.py
│   └── views.py
├── dashboard/              # User dashboard
│   ├── templates/
│   └── views.py
├── media/                  # User-uploaded files
├── puddle/                 # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3             # SQLite database
└── manage.py
```

## 🗄️ Database Models

### Item App Models:
- **Category**: Product categories
- **Item**: Product listings with price, description, images
- **Cart**: User shopping carts
- **CartItem**: Items in cart with quantities
- **Review**: Product reviews and ratings

### Conversation App Models:
- **Conversation**: Chat threads between users
- **ConversationMessage**: Individual messages

## 🎨 UI Features

- **Uniform Card Sizes**: All product cards have consistent dimensions (h-64 for images)
- **Object-fit Cover**: Images maintain aspect ratio without distortion
- **Hover Effects**: Smooth scale and shadow transitions
- **Status Badges**: Visual indicators for available/sold items
- **Responsive Grid**: Adapts to different screen sizes (1-3 columns)
- **Loading States**: Placeholder for missing images
- **Success Messages**: Toast-style notifications for user actions

## 🛠️ Technologies Used

- **Backend**: Django 4.1.5
- **Database**: SQLite3
- **Frontend**: HTML5, Tailwind CSS (CDN)
- **Image Processing**: Pillow
- **Authentication**: Django's built-in auth system

## 📝 Commands Reference

### Database Management
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

### User Management
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword <username>
```

### Development
```bash
# Run development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Collect static files (for production)
python manage.py collectstatic
```

## 🔐 Security Notes

⚠️ **Important**: This is a development version. Before deploying to production:

1. Create a `.env` file and set secure values
2. Set `DJANGO_DEBUG=False`
3. Configure `DJANGO_ALLOWED_HOSTS`
4. Configure `DJANGO_CSRF_TRUSTED_ORIGINS`
5. Use a production database (`DATABASE_URL`)
6. Collect static files (WhiteNoise enabled)
7. Enable HTTPS and security flags (`DJANGO_SECURE=True`)
8. Rotate secrets regularly and add rate limiting

## 🏁 Production Setup

### 1) Dependencies
```bash
pip install -r requirements.txt
```

### 2) Environment variables (.env)
Create a file named `.env` in the project root:
```env
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=replace-with-a-long-random-string
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
DJANGO_SECURE=True
# DATABASE_URL examples
# sqlite (dev): sqlite:///db.sqlite3
# postgres (prod): postgres://USER:PASS@HOST:5432/DBNAME
DATABASE_URL=postgres://USER:PASS@HOST:5432/DBNAME
```

### 3) Database
`settings.py` auto-detects `DATABASE_URL`. If missing, it falls back to SQLite.

### 4) Static files
WhiteNoise is configured; collect static files before starting:
```bash
python manage.py collectstatic
```

### 5) Run
For development:
```bash
python manage.py runserver
```

For production behind a reverse proxy (example on Linux):
```bash
# Install Gunicorn (optional for Linux servers)
pip install gunicorn

# Run with Gunicorn
gunicorn puddle.wsgi:application --bind 0.0.0.0:8000
```

### 6) Notes
- `ALLOWED_HOSTS` must include the domain/IP serving the app.
- `CSRF_TRUSTED_ORIGINS` requires scheme (http/https) and no trailing slash.
- Set `DJANGO_SECURE=True` to enable HSTS, secure cookies, SSL redirect.

## 🐛 Known Issues & Future Improvements

### To Be Implemented:
- [ ] Payment gateway integration
- [ ] Order management system
- [ ] Email notifications
- [ ] Pagination for product listings
- [ ] Advanced filtering (price range, sort by)
- [ ] Wishlist functionality
- [ ] Product image gallery (multiple images)
- [ ] User ratings/reputation system
- [ ] Search autocomplete
- [ ] Real-time chat with WebSockets

### Bug Fixes:
- [x] Fixed `Review.__str__` method (item.title → item.name)
- [x] Added validation for sold items in cart
- [x] Prevented users from adding own items to cart
- [x] Added success/error messages throughout the app

## 📄 License

This project is part of an educational assignment.

## 🙏 Acknowledgments

- Django Documentation
- Tailwind CSS
- The Python/Django community

---

Made with ❤️ using Django
