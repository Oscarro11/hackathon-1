import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import loader_functions
import graph_rendering

# ---------- Config ----------
st.set_page_config(page_title="Resumen de Tablas", layout="wide")

# ---------- UI ----------
st.title("Análisis de notas de estudiante")

file = st.file_uploader("Elegir archivo de notas", type="xlsx")


# ---------- State management ----------
if "tables" not in st.session_state:
    st.session_state.tables = {}
    st.session_state.dataframes = {}

# ---------- Main logic ----------
if file is not None:
    # Load only when file changes (important for performance)
    if st.session_state.get("last_file") != file:
        st.session_state.tables = loader_functions.load_tables(file)
        st.session_state.dataframes = loader_functions.calc_df(st.session_state.tables)
        st.session_state.last_file = file

    tables = st.session_state.tables
    dataframes = st.session_state.dataframes

    if tables:
        selected_table = st.sidebar.selectbox(
            "Elige la clase para la cual hacer el análisis",
            list(tables.keys())
        )

        df_actual = tables[selected_table]
        df_aportes = dataframes[selected_table]
        st.subheader(f"Clase: {selected_table}")

        graph_rendering.value_vs_weight_graph(df_aportes["Tarea"], df_aportes["Aporte"], df_aportes["Porcentaje"])

    else:
        st.warning("No se encontraron tablas en el archivo.")

else:
    st.info("Elige un archivo de notas para analizar")