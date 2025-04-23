# Detection-Of-Mental-State-With-EEG-Signal-Data-Using-Machine-Learning
## Project Overview:
The Detection of Mental State project leverages machine learning to classify an individual’s mental condition based on EEG signal data. Designed as a Django-based web application, the system allows patients to log in and analyze their cognitive state—be it tranquil, concentrating, or impartial—based on EEG datasets and predictive modeling. This provides a non-invasive, intelligent method to understand and track mental well-being.

## Problem Statement:
Mental health monitoring is a critical challenge, often reliant on subjective assessments or costly medical equipment. This project addresses the gap by using EEG data and machine learning to offer accessible mental state analysis. It encourages self-awareness and early identification of cognitive patterns that may require attention or improvement.

 ## Features:
- Patient Registration & Login
  Secure sign-up with validations and user session management.

- EEG-Based Mental State Prediction
  Processes EEG data using Support Vector Machine (SVM) to classify cognitive state into:

- Tranquil

- Concentrating

- Impartial

- Feature Selection
  Uses SelectKBest with ANOVA F-test to enhance model performance.

- Interactive Result Display
  Visual output and interpretation of EEG-derived prediction.

- Data Upload & Input Handling
  Reads EEG data from .csv for dynamic test case simulation.

## Existing Solutions & Improvements:
Traditional mental health tools focus on interviews, surveys, or medical evaluations. This project introduces a data-driven, real-time, web-based mental health insight tool. It bridges the gap between clinical methods and accessible, tech-enabled wellness tracking.

## Target Audience:
- Psychology & Neuroscience Researchers

- Health-Tech Startups

- Educational Institutions (for cognitive studies)

- General Users seeking cognitive self-assessment

## Components Used:
- Backend:
  Python Django – Web framework for routing, views, and templates

  SQLite – Default Django DB for storing patient details

  scikit-learn – For SVM classification and feature selection

- Frontend:
  HTML/CSS – User interface design

  Bootstrap – Responsive layout

- Dataset:
  CSV File – EEG signal data with features and labels (mental state classes)

🧪 Software Setup:
Step 1: Install required Python libraries
pip install django pandas scikit-learn
Step 2: Load dataset to /media folder as mental-state.csv
Step 3: Run Django server
python manage.py runserver
Step 4: Access web interface for login, registration, and mental state check.

 ## Usage Flow:
- Patient registers and logs in.

- Select a test instance (row number from CSV).

- System preprocesses the data and makes a prediction using trained SVM.

-  User receives result with interpretation and feature visualization.

## Future Enhancements:
Integration with real-time EEG headbands (e.g., NeuroSky) for live monitoring

Visualization Dashboard for cognitive trend tracking

Doctor Portal for reviewing patient analysis results

Mobile App Interface for mental state logs and push notifications

Integration with emotion tracking AI for holistic mental health monitoring

## Conclusion:
The Detection of Mental State project is a blend of web technology, data science, and health awareness. It empowers users to gain insights into their mental well-being using EEG data and intelligent algorithms—making mental health assessment more accessible, efficient, and impactful.
