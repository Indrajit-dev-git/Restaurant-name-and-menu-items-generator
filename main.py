import streamlit as st
import langchain_helper
from dotenv import load_dotenv

load_dotenv()

st.title('Restaurant Name Generator')

cuisine = st.sidebar.selectbox(
    "Choose a cusine :",
    ("Indian", "American", "Italian","Mexican","Arabic"),
)

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_titles(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write('**Menu Items**')
    for item in menu_items:
        st.write("-",item)