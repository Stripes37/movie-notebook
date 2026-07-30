# Project Ownership Notes

## Starting point

This project is being created from scratch. There is no existing codebase,
architecture, database schema, or AI-generated prototype to inherit.

## Ownership approach

I will implement the project incrementally. I may use AI to explain concepts,
review my work, and help diagnose errors, but I will avoid asking it to generate
entire features or modify the whole application at once.

## Development environment

- Operating system: Windows
- Terminal: Command Prompt
- Python version: Python 3.12.4
- Virtual environment: `.venv`

## How to launch the application

1. Open Command Prompt in the project folder.
2. Activate the virtual environment:

   `.venv\Scripts\activate.bat`

3. Start the application:

   `python -m streamlit run app.py`

4. Open `http://localhost:8501` if the browser does not open automatically.
5. Press `Ctrl+C` in Command Prompt to stop the application.

## Current application structure

- `app.py` is the Streamlit entry point.
- Streamlit runs the application on a local development server.
- The application currently displays a title and description.
- No database or film-management features have been implemented yet.