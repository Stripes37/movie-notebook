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

## Day 2: Initial database layer

### Database location

The SQLite database is stored at:

`data/movie_notebook.db`

The database is excluded from Git because it contains local application data
and can be recreated by the application.

### Films table

The `films` table contains:

- `id`: A unique integer assigned by SQLite
- `title`: The film title
- `release_year`: The film's release year
- `created_at`: The time the film was inserted

### Database functions

- `get_connection()` opens the SQLite database and configures query results so
  columns can be accessed by name.
- `initialize_database()` creates the `films` table if it does not already
  exist.
- `add_film()` inserts a film using a parameterized SQL query and returns its
  new ID.
- `get_films()` retrieves all films and returns them as dictionaries.

### Current workflow

1. `app.py` starts.
2. `app.py` calls `initialize_database()`.
3. SQLite creates the database and table if necessary.
4. `add_film()` can insert a film.
5. `get_films()` can retrieve saved films.

### Current limitations

- There is no Streamlit film form.
- Film values are not yet validated.
- Duplicate films are allowed.
- Films cannot be edited or deleted.
- Database errors are not yet displayed through the interface.