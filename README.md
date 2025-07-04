# AdminDash
A full-stack user management app with CRUD operations, form validation, PAN masking, and Excel upload/download support. Built using React, FastAPI, and MySQL. Features include responsive UI, error handling, and bulk user import with validation.

## Features

- Create, read, update, and delete users
- Bulk upload users using an Excel (.xlsx) file
- Downloadable Excel template with predefined headers
- PAN field masking with toggle visibility
- Frontend and backend input validations
- Auto-refreshing user table on all actions
- Toast-style success/error messages

## Technologies Used

- **Frontend**: React, Axios, HTML/CSS (with Tailwind )
- **Backend**: FastAPI (Python), Pydantic, openpyxl
- **File Handling**: Excel file processing with validation
- **Extras**: CORS middleware, React hooks

## Setup Instructions

### Backend (FastAPI)

1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

2. Install dependencies:
    ```bash
    pip install fastapi uvicorn openpyxl pydantic python-multipart
    ```

3. Run backend:
    ```bash
    uvicorn main:app --reload
    ```

> FastAPI will run on: `http://127.0.0.1:8000`

### Frontend (React)

1. Navigate to the frontend project directory and install dependencies:
    ```bash
    npm install
    ```

2. Start the development server:
    ```bash
    npm start
    ```

> React frontend runs on: `http://localhost:3000`

## How to Run Locally

- Start the backend with FastAPI using Uvicorn
- Run the React frontend in another terminal
- Add or upload users via the form or Excel
- Table updates automatically after each action

## Assumptions & Known Issues

- Uses in-memory list storage (not persistent). Add MySQL or SQLite for production.
- PAN format is validated using regex (`^[A-Z]{5}[0-9]{4}[A-Z]$`)
- Phone number must be 10 digits long
- Bulk uploads reject all data if even one row is invalid

## Files Included

- `main.py` – FastAPI backend logic
- `App.jsx` – Main React logic
- `data.xlsx` – Sample Excel file for testing
- `README.md` – Project overview and usage

---

Created by Rashi Sharma for a Full Stack Developer assessment.
