import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class app():
    def __init__(self) -> None:
        self.tables = {}

        st.set_page_config(page_title="Resumen de Tablas", layout="wide")
        st.title("Analisis de notas de estudiante")
        file = st.file_uploader("Elegir archivo de notas", type="xlsx")


        if file is not None:
            excel = pd.ExcelFile(file)
            sheetnames = excel.sheet_names

            for sheetname in sheetnames:
                df = pd.read_excel(excel, sheet_name=sheetname)
                self.tables[f"{sheetname}"] = df

            selected_table = st.sidebar.selectbox(
                "Elige la clase para la cual hacer el analisis",
                list(self.tables.keys())
            )
        else:
            st.write("Elige un archivo de notas para analizar")

app()