# Multilingual FAQ System

## Installation

# Clone the repo
git clone https://github.com/saideepvayyala/Backend
cd repo-name

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver

----API Endpoints
English: GET /api/faqs/

Hindi: GET /api/faqs/?lang=hi

Bengali: GET /api/faqs/?lang=bn

---Admin Access
Create a superuser:
python manage.py createsuperuser
Visit http://localhost:8000/admin to manage FAQs.
---
   **Repository Link**:https://github.com/saideepvayyala/Backend

   **Features Implemented**:
   - ✅ Multilingual FAQ model with auto-translation
   - ✅ REST API with caching (Redis)
   - ✅ Admin panel integration (django-ckeditor)

   @theakshaydhiman Please review my submission.
