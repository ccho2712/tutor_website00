# Tutor Website – Django Education Center Platform

## 📋 Overview
**Python Web Framework Development Certificate (QF Level 4) Capstone Project**

Full-stack Django application for an education center/tutor website with user authentication, course management, and admin dashboard. Demonstrates complete Django MVT workflow from models to deployment.

## ✨ Features
- **User Authentication**: Registration, login/logout, role-based permissions
- **Course Management**: Browse courses, view details, student enrollment/interest forms
- **Admin Dashboard**: Full CRUD operations for courses, users, and enquiries
- **Responsive Design**: Mobile-friendly frontend with modern CSS layouts
- **Database Integration**: PostgreSQL with normalized models and relationships

## 🛠 Tech Stack
Backend: Python 3.x, Django 5.x
Frontend: HTML5, CSS3 (SCSS/Less), JavaScript
Database: PostgreSQL (full CRUD implementation)
Tools: Git, Django Admin, Bootstrap, VS Code

text

## 📁 Project Structure
tutor_website/
├── manage.py
├── tutor_website/ # Main Django project
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── accounts/ # User authentication app
├── courses/ # Course management app
├── core/ # Main pages (home, about)
├── static/ # CSS, JS, images
│ ├── css/
│ ├── js/
│ └── scss/less/
└── templates/ # HTML templates

text

## 🎓 Key Learning Outcomes
✅ Django project setup and configuration  
✅ Model design (ORM relationships, migrations)  
✅ Views, URLs, templates (MVT architecture)  
✅ User authentication & permissions  
✅ Forms validation & error handling  
✅ Admin interface customization  
✅ Static files & responsive frontend  
✅ Local deployment & testing  

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL (or SQLite for development)
- Git

### Installation
Clone repository
git clone https://github.com/ccho2712/tutor_website.git
cd tutor_website

Create virtual environment
python -m venv venv
source venv/bin/activate # Linux/Mac

venv\Scripts\activate # Windows
Install dependencies
pip install -r requirements.txt

Database setup
python manage.py makemigrations
python manage.py migrate

Create superuser
python manage.py createsuperuser

Run server
python manage.py runserver

text

**Visit:** http://127.0.0.1:8000/
