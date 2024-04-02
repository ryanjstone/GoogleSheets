# Import Streamlit
import streamlit as st

# Import Streamlit GSheets module
from streamlit_gsheets import GSheetsConnection

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Read Weighings worksheet
df = conn.read(worksheet="Weighings")

# Print dataframe
st.dataframe(df)