# Student Exam Eligibility Portal
A flask based web application that allows student to check their exam eligibility 
status using Student ID and Name.


#Features
1. Studetn login form 
2. Dynamic result rendering 
3. SQLite database Integration
4. Flask routing and request handaling 
5. HTML template rendering 
6. Deployed on Render 

# Tech Stack
# Frontend
  1. HTML

# Backend
  1. Python
  2. Flask

# Database
  1. SQLite

# Deployment 
  1. Render

# Version Control 
  1. Git & GitHub

# Project Architecture 
Browser > Flask Route > SQL Query > SQLite Database >  Flask Respose > HTML Template

# Request Response Pipline
1. Student open the website
2. Flask send login.html
3. Student enters ID and Name
4. HTML form submits POST request
5. Flask /check route receives request
6. Python sends SQL query to SQLite 
7. Database returns matching result 
8. Flask renders result.html
9. Browser display  eligibility status 

#Run Locally 
pip install -r requirements.txt python app.py

Then open: 
http://127.0.0.1:5000

# Live Demo 
https://student-portal-906d.onrender.com

# Learning Outcomes 
Through this projects I learned:
1. Flask request-response architecture
2. Frontend-Backend communication
3. SQL query  integration
4. Dynamic HTML rendering 
5. Database-drive web applications
6. GitHub deployment workflow
7. Render cloud deploymnet  
