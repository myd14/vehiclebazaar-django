# Technical Documentation – VehicleBazaar

## 1. Overview

VehicleBazaar is a Django-based web application designed for online vehicle listing and marketplace operations. The system allows users to register, log in, create listings, manage their own ads, add favorites, and communicate with sellers. It also includes an admin panel for data management and moderation.

The project was developed with a focus on core Django architecture, relational database logic, user authentication, authorization, and deployment.

---

## 2. System Architecture

The project follows Django’s MVT (Model–View–Template) architecture:

- **Models** handle the database structure and relationships
- **Views** handle business logic and request/response flow
- **Templates** handle the user interface and rendering
- **URLs** connect user requests to the correct views

Main application components:

- `config/` → project settings, root URLs, deployment configuration
- `cars/` → main business logic, models, forms, views, and app-level URLs
- `templates/` → all HTML pages
- `static/` → static frontend assets
- `README.md` → project overview and setup guide
- `TECHNICAL_DOCUMENTATION.md` → technical design explanation

---

## 3. Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite for local development, PostgreSQL for persistent deployed data
- **Deployment:** Render
- **Version Control:** Git and GitHub

---

## 4. Database Design

The application uses Django ORM for relational model design.

### 4.1 Brand Model
Stores vehicle brand data.

**Fields:**
- `name`
- `country`

### 4.2 Car Model
Stores all listing-related information.

**Main fields:**
- `brand`
- `owner`
- `title`
- `model`
- `vehicle_type`
- `year`
- `price`
- `mileage`
- `fuel_type`
- `transmission`
- `color`
- `description`
- `seller_phone`
- `image`
- `image_url`
- `is_featured`
- `is_active`
- `created_at`
- `updated_at`

### 4.3 Message Model
Used for communication between users regarding a listing.

**Fields:**
- `sender`
- `receiver`
- `car`
- `subject`
- `content`
- `created_at`

### 4.4 Favorite Model
Stores user favorites.

**Fields:**
- `user`
- `car`
- `created_at`

### 4.5 Relationships
- One **Brand** can be linked to many **Cars**
- One **User** can own many **Cars**
- One **Car** can receive many **Messages**
- One **User** can mark many **Cars** as favorites

---

## 5. Core Functional Modules

## 5.1 Authentication Module
The project supports:
- user registration
- login
- logout

Authentication is handled with Django’s built-in authentication system.

## 5.2 Authorization Module
Authorization rules were implemented to control ownership-based actions.

Only:
- the owner of a listing
- or the admin user

can edit, archive, activate, or delete a listing.

This prevents unauthorized users from modifying listings they do not own.

## 5.3 Listing Management Module
Users can:
- create a new vehicle ad
- update their own ads
- archive ads
- reactivate ads
- delete ads
- browse all active ads
- view ad details

The system separates featured listings and user-generated listings.

## 5.4 Favorites Module
Users can add listings to favorites and remove them later.  
This supports a more realistic marketplace interaction.

## 5.5 Messaging Module
Users can contact listing owners through the car detail page.

The message structure includes:
- sender
- receiver
- subject
- content
- listing reference

## 5.6 Admin Module
The admin panel is enabled and used for:
- user management
- brand management
- listing management
- favorite records
- message records

This supports moderation and data control.

---

## 6. User Interface Design

The interface was built with Bootstrap 5 to provide a clean and responsive layout.

### Main Pages
- **Home Page**
  - featured vehicle section
  - category-based listings
- **Site’s Ads Page**
  - all user listings
- **Car Detail Page**
  - detailed listing information
  - favorite and messaging actions
- **Dashboard**
  - user-controlled listing management
- **Login / Register**
  - authentication pages
- **Admin Panel**
  - backend management

The UI was designed to remain simple, readable, and close to a real-world vehicle listing platform.

---

## 7. Search and Filtering

Search and filtering were implemented to improve usability.

Users can search listings by:
- brand
- model
- title
- description

Filtering improves navigation and makes the application more practical for marketplace use.

---

## 8. Image Handling Strategy

The project initially included direct image upload logic, but to keep the deployed version stable and flexible, support for `image_url` was added.

This allows listings to display:
1. a provided image URL,
2. uploaded image if available,
3. fallback empty visual state if no image exists.

This decision improved deployment stability and simplified image rendering in production.

---

## 9. Deployment and Data Persistence

The application is deployed on Render.

To ensure persistent production data:
- PostgreSQL support was added
- deployed environment variables were configured
- database migration and data loading steps were completed

This solved the temporary data-loss behavior caused by non-persistent local database usage in deployment.

---

## 10. Testing and Validation

The project was manually tested in the following areas:

- user registration
- login / logout
- vehicle creation
- edit and delete operations
- archive / activate workflow
- favorites add/remove
- seller messaging
- admin panel access
- deployed site accessibility
- persistent data behavior in production

Validation was also supported through Django forms and model constraints.

---

## 11. Design Decisions

Several practical technical choices were made during development:

- Django ORM was chosen for clean relational model design
- Bootstrap was selected for rapid and responsive UI development
- ownership-based authorization was prioritized for listing security
- `image_url` support was added to simplify stable production rendering
- PostgreSQL support was introduced to improve deployment persistence
- the admin panel was preserved to satisfy management and grading expectations

---

## 12. Limitations

Current limitations include:
- no advanced analytics dashboard yet
- no full expert appraisal diagram logic in production
- no payment or premium ad module
- messaging system is basic and can be expanded
- image handling is practical but not a full media storage solution

---

## 13. Future Improvements

Possible future improvements:
- advanced listing statistics tables and charts
- appraisal / inspection diagram system
- premium listing and sponsorship features
- richer user dashboard
- improved inbox and messaging threads
- REST API integration
- stronger media storage/CDN support
- better reporting and moderation tools

---

## 14. Conclusion

VehicleBazaar successfully demonstrates a full Django marketplace workflow with authentication, authorization, CRUD operations, messaging, favorites, admin control, responsive interface design, deployment, and persistent data support.

The project reflects both practical software engineering decisions and an applied understanding of Django web development architecture.