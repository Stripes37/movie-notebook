import streamlit as st
from src.database import initialize_database

initialize_database()

st.title("Film Criticism Research Notebook")
st.write("A local application for organizing film criticism research.")