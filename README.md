# Full-Stack Software Developer Project

This project is submitted as part of the Full-Stack Software Developer Trainee assignment from **CodeRower Software Pvt. Ltd.** It demonstrates the use of a Python Django backend with HTML/CSS frontend to perform RESTful operations with a MongoDB or SQLite database.

---

## 🔧 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB (original), SQLite (used for local development)
- **Architecture**: REST API

---

## 🚀 Features

### ✅ Backend

- **GET** `/api/configurations/<id>`  
  Returns a 2D array for a given configuration ID.

- **PUT** `/api/configurations/<id>`  
  Updates the `remark` field for a given configuration ID.

> ⚠️ Note: `PUT` endpoint uses `csrf_exempt` for API testing while retaining overall CSRF middleware protection.

---

### ✅ Frontend

1. **Fetch Configuration Page**  
   - Input config ID  
   - Fetch and display associated 2D array

2. **Update Remark Page**  
   - Input config ID  
   - Input remark  
   - Submit to update the backend

---

## 📁 Project Structure

coderower_assignment/
├── backend/
│ ├── manage.py
│ ├── backend/
│ │ ├── settings.py
│ │ └── urls.py
│ └── configurations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ └── configurations/
│ │ ├── fetch_config.html
│ │ └── update_remark.html


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/coderower_assignment.git
cd coderower_assignment/backend

2. Create a virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies

pip install -r requirements.txt

4. Migrate the database

python manage.py makemigrations
python manage.py migrate

5. Run the development server

python manage.py runserver

🔐 CSRF Note

CSRF protection (django.middleware.csrf.CsrfViewMiddleware) is enabled in settings.

To allow the API PUT call for /api/configurations/<id> to function during testing (e.g., via curl or fetch API), Django’s csrf_exempt decorator is only applied to that specific view.

Do not remove CSRF middleware from settings for production or public deployment.
✅ Sample curl Request

curl -X PUT "http://localhost:8000/api/configurations/testid" \
     -H "Content-Type: application/json" \
     -d "{\"remark\": \"Updated via curl\"}"
