import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def value_vs_weight_graph(tareas, aportes, porcentajes):
    x = np.arange(len(tareas))  # posiciones
    width = 0.35  # ancho de barras

    fig, ax = plt.subplots()

    # Barras
    ax.bar(x - width/2, aportes, width, label="Aporte real")
    ax.bar(x + width/2, porcentajes, width, label="Porcentaje")

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