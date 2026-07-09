
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Government Budget Comparison Dashboard", layout="wide")

st.markdown("""
<style>
.stApp {
    background-image: url('https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: 350px;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

st.title("🇮🇳 Government Budget Comparison Dashboard")

year1 = st.selectbox("Select Budget 1", ["2025-26", "2026-27"])
year2 = st.selectbox("Select Budget 2", ["2025-26", "2026-27"])

sample = pd.DataFrame({
    "Ministry": ["Finance", "Defence", "Education"],
    "2025-26": [1939001, 681210, 128650],
    "2026-27": [1972509, 784678, 139289]
})

st.dataframe(sample, use_container_width=True)

st.bar_chart(sample.set_index("Ministry")[[year1, year2]].rename(
    columns={"2025-26":"2025-26","2026-27":"2026-27"}
))
