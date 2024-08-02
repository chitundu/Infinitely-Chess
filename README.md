# Infinitely-Chess

## Introduction

Infinitely Chess is a Flask-based web application designed to assist users in learning and practicing chess. It provides various features including user registration, profile management, and an interactive chat interface powered by the Anthropic AI API to answer chess-related queries.

## Features

- User registration and login
- Profile management (edit and view profiles)
- Interactive chat for chess learning
- Practice section for honing chess skills
- Responsive routes and error handling

## Requirements

- Python 3.7+
- Flask
- Flask-CORS
- python-dotenv
- anthropic (Anthropic API client library)

## Setup Instructions

### Prerequisites

1. Ensure Python 3.7+ is installed.
2. Set up a virtual environment:
    
    ```
    python -m venv venv
    
    ```
    
3. Activate the virtual environment:
    - On Windows:
        
        ```
        venv\\Scripts\\activate
        
        ```
        
    - On macOS/Linux:
        
        ```
        source venv/bin/activate
        
        ```
        

### Installation

1. Clone the repository:
    
    ```
    git clone <https://github.com/chitundu/Infinitely-Chess.git>
    cd infinitely-chess
    
    ```
    
2. Install the required packages:
    
    ```
    pip install -r requirements.txt
    
    ```
    
3. Create a `.env` file in the root directory and add your Anthropic API key:
    
    ```
    ANTHROPIC_API_KEY=your_api_key_here
    
    ```
    

### Running the Application

1. Start the Flask application:
    
    ```
    python app.py
    
    ```
    
2. Open your browser and navigate to `http://localhost:5001` to access the application.

## Application Structure

```
infinitely-chess/
│
├── templates/
│   ├── Edit Profile.html
│   ├── index.html
│   ├── Profile1.html
│   ├── Sign In.html
│   ├── Sign Up.html
│   └── Practice.html
│
├── .env
├── app.py
├── requirements.txt
└── README.md

```

### Explanation of Files

- `app.py`: Main application file containing all routes and logic.
- `templates/`: Directory containing HTML templates for different pages.
- `.env`: Environment variables file (not included in the repository, to be created by the user).
- `requirements.txt`: List of required Python packages.
- `README.md`: This file.

## Routes

- `/`: Sign up page.
- `/index`: Main index page after login.
- `/sign_in`: Sign in page.
- `/edit_profile`: Page to edit user profile.
- `/profile`: Page to view user profile.
- `/save`: Endpoint to save profile changes (POST method).
- `/practice`: Page for chess practice.
- `/chat`: Endpoint to interact with the AI chat for chess queries (POST method).
- `/test`: Test endpoint to check if the server is running (GET method).

## Usage

### Chat with AI

To use the chat functionality, send a POST request to `/chat` with the following JSON payload:

```json
{
  "message": "Your chess-related question here",
  "length": "short",  // or "medium", "long"
  "humor": true  // or false
}

```

### Error Handling

- If the Anthropic API key is missing, the application will log an error and the chat functionality will be disabled.
- If there is an error in the chat request, the application will return an appropriate JSON response with an error message.

## Logging

The application uses Python's built-in `logging` module to log important events and errors. Logs include information about incoming requests, API interactions, and error messages.

