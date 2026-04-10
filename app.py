import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------- Config ----------
st.set_page_config(page_title="Resumen de Tablas", layout="wide")

# ---------- Helpers ----------
def load_tables(file):
    """Read all sheets into a dict of DataFrames."""
    excel = pd.ExcelFile(file)
    tables = {}

    for sheetname in excel.sheet_names:
        df = pd.read_excel(
            excel,
            sheet_name=sheetname,
            header=0,
            index_col=0
        )
        tables[sheetname] = df

    return tables

def calc_df(tables):
    dicc_df = {}

    for name, df_actual in tables.items():

        nota = pd.to_numeric(df_actual.loc["Nota"], errors="coerce")
        porcentaje = pd.to_numeric(df_actual.loc["Porcentaje"], errors="coerce")

        aportes = (nota * porcentaje) / 100

        df_aportes = pd.DataFrame({
            "Tarea": aportes.index,
            "Aporte": aportes.values,
            "Porcentaje": porcentaje.values
        }).dropna()

        dicc_df[name] = df_aportes

    return dicc_df

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
        st.session_state.tables = load_tables(file)
        st.session_state.dataframes = calc_df(st.session_state.tables)
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

        tareas = df_aportes["Tarea"]
        aporte = df_aportes["Aporte"]
        porcentaje = df_aportes["Porcentaje"]

        x = np.arange(len(tareas))  # posiciones
        width = 0.35  # ancho de barras

        fig, ax = plt.subplots()

        # Barras
        ax.bar(x - width/2, aporte, width, label="Aporte real")
        ax.bar(x + width/2, porcentaje, width, label="Porcentaje")

        # Etiquetas
        ax.set_xticks(x)
        ax.set_xticklabels(tareas, rotation=45, ha="right")

        ax.set_title("Aporte real vs Peso de cada tarea")
        ax.set_ylabel("Valor")
        ax.legend()

        # Ajuste para que no se corten etiquetas
        plt.tight_layout()

        # Mostrar en Streamlit
        st.pyplot(fig)
    else:
        st.warning("No se encontraron tablas en el archivo.")

else:
    st.info("Elige un archivo de notas para analizar")