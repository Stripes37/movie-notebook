# Film Criticism Research Notebook
    **Description**: A local application for organizing films, critics, publications, reviews, and notes about how different critics interpret the same film. The initial version will allow the user to add films, view saved films, and store the data persistently in SQLite.

## Planned first version
The first version of the application will:

1. Allow the user to enter a film title and release year.
2. Validate that the title is not empty and the year is reasonable.
3. Save the film to a local SQLite database.
4. Display all saved films in the Streamlit interface.
5. Show clear success and error messages.

The first version will not include AI analysis, review scraping, user accounts,
advanced search, exports, or critic and publication management.

### Initial technology choices

- Python: I already have some familiarity with it and it is suitable for
  data-oriented applications.
- Streamlit: It allows me to create a usable interface while keeping the
  project focused on Python.
- SQLite: It provides persistent relational storage without requiring a
  separate database server.
- pytest: It will be used to test validation and database functions.