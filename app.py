import streamlit as st
import pandas as pd

class app():
    def __init__(self) -> None:
        file = st.file_uploader("Elegir archivo de notas", type=".csv")

        if file is not None:
            df = pd.read_csv(file)
            st.write(file)