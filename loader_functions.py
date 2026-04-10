#Primero se leen todas las hojas del archivo Excel y se guardan como tablas. Luego, 
#se procesan los datos para calcular el aporte de cada tarea usando la fórmula nota 
#por porcentaje dividido entre 100, generando un nuevo conjunto de datos listo para ser visualizado.
import pandas as pd
# ---------- FUNCIÓN 1: Cargar tablas ----------
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
# ---------- FUNCIÓN 2: Procesar datos ----------
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
