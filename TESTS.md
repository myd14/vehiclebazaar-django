# Basic Test Documentation – VehicleBazaar

## 1. Purpose

This document summarizes the core manual test scenarios performed for the VehicleBazaar project. The purpose of these tests is to confirm that the main user flows, listing management functions, admin access, and deployment behavior work correctly.

---

## 2. Testing Scope

The following project areas were tested:

- authentication
- authorization
- listing creation and editing
- listing archive / activate flow
- favorites
- messaging
- admin panel
- deployed system behavior
- persistent data behavior

---

## 3. Test Environment

### Local Environment
- Python 3.11
- Django
- SQLite
- Anaconda environment: `carlisting`

### Production Environment
- Render deployment
- PostgreSQL database
- GitHub integration

---

## 4. Manual Test Cases

### Test 1 – User Registration
**هدف / Purpose:** Verify that a new user can create an account.

**Steps:**
1. Open the Register page
2. Enter username, email, and password
3. Submit the form

**Expected Result:**
- User account is created successfully
- User can proceed to login

**Result:** Passed

---

### Test 2 – User Login
**Purpose:** Verify that registered users can log in.

**Steps:**
1. Open the Login page
2. Enter valid username and password
3. Submit the form

**Expected Result:**
- User is logged in
- Navigation bar reflects authenticated state

**Result:** Passed

---

### Test 3 – User Logout
**Purpose:** Verify that authenticated users can log out.

**Steps:**
1. Log in to the system
2. Click Logout

**Expected Result:**
- Session ends successfully
- User returns to public state

**Result:** Passed

---

### Test 4 – Create Listing
**Purpose:** Verify that authenticated users can create a vehicle listing.

**Steps:**
1. Log in
2. Open Add Listing page
3. Fill in listing fields
4. Submit the form

**Expected Result:**
- New listing is created
- Listing appears in user listings / listing pages

**Result:** Passed

---

### Test 5 – Edit Own Listing
**Purpose:** Verify that a user can edit only their own listing.

**Steps:**
1. Log in as listing owner
2. Open Edit page of own listing
3. Change listing information
4. Save changes

**Expected Result:**
- Listing updates successfully
- Updated data is visible on detail/list pages

**Result:** Passed

---

### Test 6 – Archive Listing
**Purpose:** Verify that listing owners can archive their own listings.

**Steps:**
1. Log in as owner
2. Open owned listing
3. Click Archive

**Expected Result:**
- Listing moves to inactive state
- Listing is no longer shown as active

**Result:** Passed

---

### Test 7 – Reactivate Listing
**Purpose:** Verify that archived listings can be reactivated.

**Steps:**
1. Log in as owner
2. Open archived listing controls
3. Click Activate

**Expected Result:**
- Listing becomes active again
- Listing reappears in active listings

**Result:** Passed

---

### Test 8 – Authorization Control
**Purpose:** Verify that users cannot edit or delete listings they do not own.

**Steps:**
1. Log in as User A
2. Open listing owned by User B
3. Check available action buttons

**Expected Result:**
- Edit/Delete controls are not shown
- Unauthorized modification is blocked

**Result:** Passed

---

### Test 9 – Favorite Add / Remove
**Purpose:** Verify that users can add and remove favorites.

**Steps:**
1. Log in
2. Open a listing not owned by the current user
3. Add listing to favorites
4. Remove listing from favorites

**Expected Result:**
- Favorite state changes correctly
- Favorite count / user state updates accordingly

**Result:** Passed

---

### Test 10 – Messaging Seller
**Purpose:** Verify that a user can send a message to a listing owner.

**Steps:**
1. Log in as non-owner user
2. Open listing detail page
3. Click message action
4. Submit message

**Expected Result:**
- Message is stored successfully
- Message becomes visible in admin panel

**Result:** Passed

---

### Test 11 – Admin Panel Access
**Purpose:** Verify that admin panel is active and accessible.

**Steps:**
1. Open `/admin`
2. Log in with admin credentials

**Expected Result:**
- Admin panel opens successfully
- Admin can manage users, cars, messages, and favorites

**Result:** Passed

---

### Test 12 – Search and Filter
**Purpose:** Verify that search and listing filter logic works.

**Steps:**
1. Open listing page
2. Search by keyword / title / brand / model
3. Apply filter options if available

**Expected Result:**
- Relevant listings are shown
- Search narrows down results correctly

**Result:** Passed

---

### Test 13 – Deployment Availability
**Purpose:** Verify that the deployed site is reachable.

**Steps:**
1. Open deployed Render URL
2. Visit public listing pages
3. Visit detail pages

**Expected Result:**
- Site loads successfully
- Public pages render without critical errors

**Result:** Passed

---

### Test 14 – Data Persistence
**Purpose:** Verify that newly added data remains available after refresh / restart conditions.

**Steps:**
1. Register a new user
2. Add a new listing
3. Refresh page and revisit site
4. Confirm stored data still exists

**Expected Result:**
- User and listing remain stored
- Production database retains changes

**Result:** Passed

---

## 5. Validation Summary

The most critical platform flows were successfully tested:

- account creation
- login/logout
- listing CRUD operations
- archive/activate workflow
- favorite system
- messaging system
- admin access
- deployment availability
- persistent data behavior

---

## 6. Known Limitations

- Tests are mainly manual rather than automated unit tests
- Messaging system is functional but still basic
- Advanced chart/statistics testing has not yet been implemented
- Media handling is practical but not a full production-grade media pipeline

---

## 7. Conclusion

The basic test process shows that VehicleBazaar is functionally stable for the main project requirements. Core marketplace actions, admin access, authentication, and deployed behavior have been verified successfully.