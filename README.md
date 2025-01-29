# cargararchivos.py
Esta Aplicación permitirá cargar Archivos .CSV y .XLSX

Explicación del código:

- Carga de archivos: Usamos st.file_uploader para permitir al usuario subir archivos.

- Lectura de datos: Dependiendo de la extensión (.csv o .xlsx), usamos pd.read_csv o pd.read_excel.

- Gráficos modernos: Usamos Plotly Express para generar gráficos interactivos y visualmente atractivos.

- Interfaz intuitiva: Selectores para elegir columnas y tipo de gráfico.

Resultado:

- Una aplicación web donde puedes subir archivos CSV/XLSX.

- Vista previa de los datos.

- Gráficos interactivos con opciones personalizables.
