# Film Criticism Research Notebook

A local Python application for organizing films and film-criticism research.

## Initial scope

The first version will:

- Allow the user to add a film
- Validate the film title and release year
- Save films in a local SQLite database
- Display saved films
- Show useful success and error messages

The first version will not include AI analysis, review scraping, user accounts,
advanced search, exports, or critic and publication management.

## Technology

- Python
- Streamlit
- SQLite
- pytest
- Git

## Running the application

1. Open Command Prompt in the project folder.

2. Activate the virtual environment:

   `.venv\Scripts\activate.bat`

3. Install dependencies when necessary:

   `python -m pip install -r requirements.txt`

4. Start the application:

   `python -m streamlit run app.py`

5. Open `http://localhost:8501` if the browser does not open automatically.

6. Press `Ctrl+C` in Command Prompt to stop the application.