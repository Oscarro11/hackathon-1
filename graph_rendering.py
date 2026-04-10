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

def plot_final_grades(final_grades):

    # Filtrar valores válidos
    filtered = {k: v for k, v in final_grades.items() if v is not None}

    # Ordenar de menor a mayor
    sorted_items = sorted(filtered.items(), key=lambda x: x[1])

    cursos = [item[0] for item in sorted_items]
    notas = [item[1] for item in sorted_items]

    # Crear figura
    fig, ax = plt.subplots()

    ax.bar(cursos, notas)

    # Etiquetas
    ax.set_title("Notas finales por curso")
    ax.set_ylabel("Nota final")
    ax.set_xlabel("Curso")

    ax.set_xticklabels(cursos, rotation=45, ha="right")

    # Mostrar valores encima de cada barra
    for i, v in enumerate(notas):
        ax.text(i, v, f"{v:.1f}", ha="center", va="bottom")

    plt.tight_layout()
    st.pyplot(fig)
