# Smoke N Slice

Smoke N Slice is a modular Django-based restaurant order and payment management system that simulates a real-world internal restaurant workflow.

The system is designed for staff usage where employees can manage menu items, create customer orders, apply discounts, process payments, and track transactions efficiently.

---

## Core Features

### Authentication & Staff Control
- Staff-only login system  
- Role-based access using Django authentication  
- Secure session management  

### Menu Management
- Category-based item organization  
- Price management  
- Availability control  

### Order Processing
- Dynamic order creation  
- Automatic total calculation  
- Percentage-based discount support  
- Order status tracking (Pending → Paid)  

### Payment System
- Card / Mobile banking simulation  
- Transaction ID generation  
- Payment record storage  
- Automatic order status update after payment  

---

## System Workflow

1. Staff logs in  
2. Selects items from the menu  
3. System calculates total  
4. Optional discount applied  
5. Payment processed  
6. Order marked as Paid  
7. Transaction stored in database  

---

## Project Architecture (Django MVT Pattern)

Client (Browser)  
↓  
Views (Controller Logic)  
↓  
Models (Business Logic & ORM)  
↓  
SQLite Database  

---

## App-Based Modular Structure

| App Name  | Responsibility |
|-----------|---------------|
| accounts  | Staff authentication & profiles |
| menu      | Item & category management |
| orders    | Order & discount logic |
| payments  | Payment processing & transaction storage |

---

## Project Structure

```
smoke_n_slice/
│
├── accounts/
├── menu/
├── orders/
├── payments/
├── smoke_n_slice/  (project settings)
└── manage.py
```

---

## Technologies Used

- Python 3  
- Django  
- SQLite  
- Django ORM  
- HTML / CSS  
- Session-based Authentication  

---

## Installation Guide

### 1. Clone Repository
```
git clone https://github.com/alamin-safadi/Smoke_N_Slice.git
cd Smoke_N_Slice
```

### 2. Create Virtual Environment
```
python -m venv smoke_env
smoke_env\Scripts\activate   # Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User
```
python manage.py createsuperuser
```

### 6. Run Server
```
python manage.py runserver
```

Visit:
```
http://127.0.0.1:8000/
```

Admin Panel:
```
http://127.0.0.1:8000/admin/
```

---

## Architecture Principles

- Separation of Concerns  
- Modular App Design  
- Relational Database Modeling  
- Clean Django MVT Structure  
- Session-Based State Handling  

---

## Future Improvements

- Real payment gateway integration (Stripe)  
- REST API using Django REST Framework  
- JWT Authentication  
- Sales analytics dashboard  
- Cloud deployment  

---

## Author

Developed as a real-world restaurant workflow simulation project using Django to demonstrate backend architecture, modular system design, and clean application structure.
