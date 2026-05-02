# 🚀 Admin Portal (Flask Project)

## 📌 Project Overview

Admin Portal is a web-based application built using **Flask (Python)** that allows administrators to manage opportunities efficiently.
It includes authentication features and full CRUD operations.

---

## ✨ Features

### 🔐 Authentication

* Admin Sign Up
* Admin Login
* Forgot Password
* Reset Password

### 📊 Opportunity Management

* View all opportunities
* Add new opportunity
* View opportunity details
* Edit opportunity
* Delete opportunity
* Data persists after login

---

## 🛠️ Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite (Database)
* HTML, CSS (Jinja2 Templates)

---

## 📁 Project Structure

```
AdminPortal/
│
├── app/
│   ├── routes/
│   ├── models.py
│   ├── extensions.py
│   └── __init__.py
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
│
├── static/
│   └── images/
│
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/SaiAmulya13/AdminPortal.git
cd AdminPortal
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Application

```
python run.py
```

---

## 🌐 Usage

* Open browser → `http://127.0.0.1:5000`
* Register as admin
* Login and manage opportunities

---


## 📌 Future Improvements

* Email-based password reset
* Role-based authentication
* UI improvements
* Deployment (Render/Heroku)

---



Give it a ⭐ on GitHub!
