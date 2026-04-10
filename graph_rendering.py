#Esta función genera un gráfico de barras comparando el aporte real de cada tarea con su porcentaje, usando matplotlib, y luego lo muestra en la interfaz de Streamlit
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
# Función para graficar aportes vs porcentajes
# Crear posiciones numéricas para cada tarea (0,1,2,3...)
# Crear figura y eje del gráfico
def value_vs_weight_graph(tareas, aportes, porcentajes):
    x = np.arange(len(tareas))  # posiciones
    width = 0.35  # ancho de barras

    fig, ax = plt.subplots()
# Barras de "aporte real"
    # ---------- Configuración visual ----------
#este apartado ayuda en el diseño mostrandonos como titulos nobres esto ayudando a identificar lo que se visualiza
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
