# A Loan Default Prediction WebApp

This projects showcases how to serve a trained machine learning model
while creating a user interface for interaction with users.

## Tools
This reactive UI is built with HTML, CSS and vanilla JavaScript
The backend runs on FastAPI which avails the frontend resources and the
machine learning model. The ML model is trained using ScikitLearn

To run the project locally clone this repo and:
```
$cd app
```

Create a virtual environment
```
$python -m venv .venv #Linux python3
```

Activate the environment:
# On Linux
```
$source .venv/bin/activate
```
# On Windows
```
$.venv/Scripts/activate
```

To run the app:
```
$uvicorn main:app --reload
```

Navigate to ```http://127.0.0.1/8000/```

# Example
![Sample try](app/assets/loan_app_img.png)