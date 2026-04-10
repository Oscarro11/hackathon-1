import pandas as pd

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