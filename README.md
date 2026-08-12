# 📦 Inventory Management System

A web-based **Inventory Management System** built with **Python and Django** for managing, monitoring, and tracking products in an inventory.

The application provides secure user authentication, role-based access, product management, search, pagination, and an interactive dashboard for monitoring stock levels and inventory value.

---

## 🚀 Features

### 🔐 Authentication

- User registration
- User login and logout
- Authentication-protected pages
- Prevents unauthenticated users from accessing the inventory system

### 👥 Role-Based Access

The system supports three types of users:

| Role | View | Search | Add | Update | Delete |
|------|------|--------|-----|--------|--------|
| **Superuser** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Staff** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Normal User** | ✅ | ✅ | ❌ | ❌ | ❌ |

Superusers also have access to Django's built-in administration capabilities.

### 📦 Product Management

Authorized users can manage inventory products through:

- Add products
- View products
- Update products
- Delete products

Product information includes:

- Product ID
- Product Name
- SKU
- Price
- Quantity
- Supplier

### 🔎 Product Search

Products can be searched using a single search box based on:

- Product Name
- SKU

The search supports partial matching using Django's `icontains` lookup.

### 📄 Pagination

The product list uses pagination to display products across multiple pages instead of loading the entire inventory at once.

Search and stock filters are preserved while navigating between pages.

### 📊 Inventory Dashboard

The dashboard acts as the application's home page and provides an overview of the inventory.

It displays:

- **Total Products**
- **Low Stock Products**
- **Out of Stock Products**
- **Total Inventory Value**

Low-stock and out-of-stock statistics are clickable and take the user directly to the corresponding filtered products.

### 📉 Stock Monitoring

The system identifies stock conditions based on product quantity:

- **Out of Stock:** Quantity = 0
- **Low Stock:** Quantity between 1 and 5
- **Normal Stock:** Quantity greater than 5

---

## 🛠️ Tech Stack

### Backend

- **Python** — Primary programming language
- **Django** — Web framework
- **Django ORM** — Database interaction
- **Django Authentication** — User authentication and authorization

### Frontend

- **HTML5**
- **CSS3**
- **Bootstrap 4.5.2**
- **Django Templates**

### Forms & UI

- **Django Forms**
- **Django Crispy Forms**
- **Crispy Bootstrap 5**

### Database

- **SQLite**

### Development Tools

- **Git**
- **GitHub**
- **Visual Studio Code**

---

## 🏗️ Django Concepts Used

This project was built using several important Django concepts:

- MVT Architecture
- Django Apps
- URL Routing
- Function-Based Views
- Django Templates
- Template Inheritance
- Static Files
- Django Models
- Django ORM
- ModelForms
- Form Validation
- Django Authentication
- Login / Logout
- Authentication Decorators
- Authorization
- Django Pagination
- Query Parameters
- `Q` Objects
- ORM Aggregation
- Bootstrap Integration

---

## 🎯 Project Objective

The objective of this project is to build a practical **Inventory Management System** using Django while applying core backend and web development concepts such as:

- Database-driven application development
- CRUD operations
- Django ORM
- User authentication and authorization
- Role-based access control
- Form handling and validation
- Product search and filtering
- Pagination
- Inventory stock monitoring
- Dashboard development
- Bootstrap-based UI development

The project provides a centralized system for managing products and monitoring inventory status through an easy-to-use web interface.

---

## 👨‍💻 About the Author

**Ravada Sandeep** is a Computer Science Engineering student specializing in **Data Science**, with a strong interest in **Python, Django, backend development, databases, and software development**.

This project was developed as a practical application of Django concepts and to strengthen backend development skills by building a real-world inventory management solution.