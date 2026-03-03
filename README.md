🟠 Smoke N Slice

Smoke N Slice is a modular Django-based restaurant order and payment management system that simulates a real-world restaurant workflow.

The system is designed for internal staff usage where employees can manage menu items, create customer orders, apply discounts, process payments, and track transactions efficiently.

🚀 Core Features
🔐 Authentication & Staff Control

Staff-only login system

Role-based access using Django authentication

Secure session management

🍕 Menu Management

Category-based item organization

Price management

Availability control

🛒 Order Processing

Create orders dynamically

Automatic total calculation

Percentage-based discount support

Order status tracking (Pending → Paid)

💳 Payment System

Card / Mobile banking simulation

Transaction ID generation

Payment record storage

Order status auto-update

📦 Inventory (Optional)

Stock deduction after successful payment

Auto-disable items when stock is zero

🧠 System Workflow (Step-by-Step)

1️⃣ Staff logs in
2️⃣ Selects items from the menu
3️⃣ System calculates total
4️⃣ Optional discount applied
5️⃣ Payment processed
6️⃣ Order marked as Paid
7️⃣ Transaction stored in database
8️⃣ Inventory updated (if enabled)

🏗️ Project Architecture (Django MVT Pattern)

Client (Browser)
⬇
Views (Controller Logic)
⬇
Models (Business Logic & ORM)
⬇
SQLite Database

🧩 App-Based Modular Structure
App Name	Responsibility
accounts	Staff profiles & authentication
menu	Item & category management
orders	Order & discount logic
payments	Payment processing & transaction storage
inventory (optional)	Stock tracking
🗂️ Project Structure
smoke_n_slice/
│
├── accounts/
├── menu/
├── orders/
├── payments/
├── inventory/
├── smoke_n_slice/ (settings)
└── manage.py
🛠️ Technologies Used

Python 3

Django

SQLite

Django ORM

HTML / CSS

Session-based Authentication

Stripe-ready payment structure

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/alamin-safadi/Smoke_N_Slice.git
cd smoke-n-slice
2️⃣ Create Virtual Environment
python -m venv smoke_env
smoke_env\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Admin User
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Visit:

http://127.0.0.1:8000/

Admin Panel:

http://127.0.0.1:8000/admin/
🔐 Admin Panel Capabilities

The Django Admin Panel provides full backend control.

👤 Accounts Section
Staff Profiles

Add new staff member

Edit staff information

Delete staff

Assign roles

Users

Create new users

Change passwords

Assign staff status

Manage permissions

Activate / deactivate accounts

Groups

Create role-based groups

Assign permissions to groups

Attach users to groups

🍕 Menu Section
Categories

Add new category (e.g., Pizza, Drinks)

Edit category

Delete category

Items

Add menu item

Set price

Assign category

Mark available/unavailable

Upload item image

Edit or delete items

🛒 Orders Section
Orders

Create new order manually

View order details

Update order status

Apply discount

View total amount

Track which staff created the order

Order Items

View items inside each order

Adjust quantity

Modify price (if needed)

💳 Payments Section
Payments

View payment history

See transaction ID

Check payment method

Confirm payment status

Link payment to order

Delete or edit payment record (if needed)

📊 Recent Admin Actions

Admin can see:

Recently added items

Edited users

Added categories

Updated orders

Payment records

This provides full audit visibility.

🧩 Database Relationship Overview

User
⬇
Order
⬇
OrderItem
⬇
Item

Order
⬇
Payment

🎯 Architecture Principles Used

✔ Separation of Concerns
✔ Modular App Design
✔ Relational Database Modeling
✔ Clean MVC (Django MVT) Structure
✔ Session-Based State Handling
✔ Extendable Payment Layer

📌 Future Improvements

Real Stripe Integration

REST API (Django REST Framework)

JWT Authentication

Sales Analytics Dashboard

Multi-branch support

Cloud deployment (AWS / Railway)

👨‍💻 Author

Developed as a real-world restaurant workflow simulation project using Django to demonstrate full-stack backend architecture and modular system design.
