# VehicleBazaar

VehicleBazaar is a Django-based vehicle marketplace web application where users can register, log in, post car listings, edit their own ads, save favorites, and contact sellers. The platform also includes an admin panel for managing listings, users, and messages.

## Project Description

This project was developed as a Django term project. The aim is to provide a clean and functional vehicle listing platform similar to online automotive marketplaces. Users can browse listings, view vehicle details, contact sellers, and manage their own ads through a dashboard-style workflow.

## Main Features

- User registration, login, and logout
- Add, edit, and delete car listings
- Archive and reactivate listings
- View car details
- Favorite system
- Messaging system for contacting sellers
- Admin panel for managing data
- Search and filtering
- Featured listings and user listings
- Image support with listing image URLs
- Responsive Bootstrap-based interface

## Technologies Used

- Python
- Django
- PostgreSQL / SQLite
- HTML
- CSS
- Bootstrap 5
- Git & GitHub
- Render

## Project Structure

- `cars/` → main application logic
- `templates/` → HTML templates
- `static/` → static files
- `config/` → Django project settings and URL configuration
- `manage.py` → Django project entry point
- `requirements.txt` → project dependencies

## Database Design

The project uses relational database logic through Django models.

### Main Models

- **Brand**
  - Stores vehicle brand name and country

- **Car**
  - Stores listing information such as title, model, year, price, mileage, fuel type, transmission, color, description, image, image URL, listing status, and owner

- **Message**
  - Stores buyer-seller communication for listings

- **Favorite**
  - Stores user favorite listings

### Relationships

- One **Brand** can have many **Cars**
- One **User** can own many **Cars**
- One **Car** can have many **Messages**
- One **User** can favorite many **Cars**

## Core Functionalities

### Authentication
Users can create accounts, log in, and log out securely.

### Authorization
Only the owner of a listing or the admin can edit, archive, activate, or delete that listing.

### Listing Management
Users can:
- create new listings
- update their own listings
- archive and reactivate listings
- view detailed vehicle pages

### Favorites
Users can add or remove listings from favorites.

### Messaging
Users can send messages to listing owners through the listing detail page.

### Admin Panel
The admin panel allows management of:
- users
- brands
- cars
- messages
- favorites

## User Interface

The interface is designed with Bootstrap for a clean and responsive layout. Main pages include:

- Home page
- Site's Ads page
- Car detail page
- Dashboard
- Login and Register pages
- Admin panel

## Setup Instructions

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/myd14/vehiclebazaar-django.git  
cd vehiclebazaar-django

### 2. Create and activate environment
conda create -n carlisting python=3.11  
conda activate carlisting

### 3. Install dependencies
pip install -r requirements.txt

### 4. Apply migrations
python manage.py makemigrations  
python manage.py migrate

### 5. Create superuser
python manage.py createsuperuser

### 6. Run the server
python manage.py runserver

## Deployment

The project is deployed on Render.

**Live URL:**  
https://vehiclebazaar-django.onrender.com/

## Sample Features Demonstrated

- Vehicle listing creation
- Listing detail pages
- Search and filter
- Favorites
- Seller messaging
- Admin-based management
- Persistent online deployment with PostgreSQL support

## Basic Test Scenarios

The following core scenarios were manually tested:

- user registration works
- user login works
- user logout works
- listing creation works
- listing editing works
- listing archive / activate works
- favorite add / remove works
- messaging works
- admin panel access works
- deployed site loads successfully

## Design Choices

- Django ORM was used for structured model relationships
- Bootstrap was used for responsive UI
- Admin panel was kept active for data management
- Image URL support was added to make listing visuals more flexible and deployment-friendly
- Listing ownership control was implemented for authorization
- PostgreSQL support was added for persistent deployed data storage

## Future Improvements

- Advanced statistics dashboard
- Vehicle expertise diagram
- Better chart-based reporting
- More advanced messaging inbox
- Payment / premium listing system
- API integration for vehicle data
- Full production media storage

## Screenshots

Screenshots can be added here:
- Home page
- Car listing page
- Car detail page
- Dashboard
- Admin panel

## Author

**Mustafa Mayda**

## Course Project Note

This application was prepared as a Django term project and focuses on practical CRUD operations, database relations, authentication, authorization, deployment, and user interaction features.

