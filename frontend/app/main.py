import streamlit as st
import requests
import os

# Load backend URL from .env or default
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("PDF Q&A AI Demo")

if st.button("Call"):
    try:
        response = requests.get(f"{BACKEND_URL}/hello")
        response.raise_for_status()
        data = response.json()
        st.success("Backend Response:")
        st.json(data)
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("db connected ?"):
    try:
        response = requests.get(f"{BACKEND_URL}/test-db")
        response.raise_for_status()
        data = response.json()
        st.success("Backend Response:")
        st.json(data)
    except Exception as e:
        st.error(f"Error: {e}")


if st.button("add qa"):
    try:
        response = requests.get(f"{BACKEND_URL}/add-qa")
        response.raise_for_status()
        data = response.json()
        st.success("Backend Response:")
        st.json(data)
    except Exception as e:
        st.error(f"Error: {e}")