import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Carga de Datos", layout="wide")

# Título de la aplicación
st.title("Cargar archivos CSV/XLSX y generar gráficos 📊")

# Cargar archivo
uploaded_file = st.file_uploader("Sube tu archivo (CSV o XLSX)", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Leer el archivo según su extensión
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            # Obtener las hojas disponibles
            xls = pd.ExcelFile(uploaded_file, engine="openpyxl")
            sheet_names = xls.sheet_names  # Lista de nombres de hojas
            selected_sheet = st.selectbox("Selecciona una hoja", sheet_names)  # Selector de hojas
            df = pd.read_excel(uploaded_file, sheet_name=selected_sheet, engine="openpyxl")
        
        # Mostrar datos
        st.subheader("Vista previa de los datos")
        st.dataframe(df.head(), use_container_width=True)

        # Seleccionar columnas para el gráfico
        st.subheader("Configurar el gráfico")
        x_axis = st.selectbox("Elige la columna para el eje X", df.columns)
        y_axis = st.selectbox("Elige la columna para el eje Y", df.columns)
        chart_type = st.selectbox("Tipo de gráfico", ["Línea", "Barras", "Dispersión"])

        # Crear el gráfico con Plotly (moderno e interactivo)
        if chart_type == "Línea":
            fig = px.line(df, x=x_axis, y=y_axis, title="Gráfico de Línea")
        elif chart_type == "Barras":
            fig = px.bar(df, x=x_axis, y=y_axis, title="Gráfico de Barras")
        elif chart_type == "Dispersión":
            fig = px.scatter(df, x=x_axis, y=y_axis, title="Gráfico de Dispersión")

        # Mostrar el gráfico
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error al procesar el archivo: {str(e)}")
else:
    st.warning("Por favor, sube un archivo CSV o XLSX.")
