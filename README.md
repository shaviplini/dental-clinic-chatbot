# Dental Clinic Chatbot & Admin Tool

A simple, self-hosted Python Flask chatbot and browser dashboard made for local dental clinics. It lets businesses answer basic patient questions automatically and lets non-technical staff manage the data directly.

## How it works
* `app.py`: The core Python Flask server. It handles the message routing, counts keyword matches to figure out answers, and manages the API endpoints for saving data.
* `index.html`: A clean, floating web widget that sits in the bottom right corner of a website for patients to chat with.
* `admin.html`: A basic browser form for the front-desk staff to edit answers, office hours, or keywords without touching code.
* `faqs.json`: A simple configuration file used to store all the answers and trigger phrases.

## Setup & Run
1. Install Flask and Flask-CORS: `pip install flask flask-cors`
2. Run the backend server: `python3 app.py`
3. Open `index.html` or `admin.html` in any browser to test.
