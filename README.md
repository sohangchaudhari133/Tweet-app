# 🐦 Tweet App (Django)

A simple Django-based web application that allows users to share their thoughts as tweets (short text posts). Think of it as a mini Twitter clone!

---

## 🚀 Features

- User registration and authentication (login/logout)
- Create, edit, and delete tweets
- View all tweets (public feed)
- Clean UI using Bootstrap

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default) or switch to PostgreSQL/MySQL
- **Frontend:** HTML, CSS, Bootstrap (or Tailwind)
- **Authentication:** Django built-in auth system

---

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/sohangchaudhari133/Tweet-app.git
```
2. **Create a virtual environment**
```
# On Mac:
python3 -m venv .venv
source .venv/bin/activate
```
```
 # On Windows:
python -m venv .venv
 .venv\Scripts\activate
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Set up environment variables**
- Create a .env file in the root directory and add:
  ```
  SECRET_KEY=your-secret-key
  DEBUG=True
  ```
5. **Run migrations**
  ```
python manage.py migrate
  ```
6. **Run the development server**
  ```
  python manage.py runserver
  ```
7. **Access the app**
  - Visit http://127.0.0.1:8000 in your browser. 
