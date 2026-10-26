# Panel de anuncios de venta de coches

Aplicación web hecha con **Streamlit** que permite explorar un conjunto de datos de anuncios de venta de coches usados en EE. UU. (`vehicles_us.csv`).

## ¿Qué hace la aplicación?

- Muestra una vista previa de los datos.
- Construye un **histograma** de la distribución del odómetro (kilometraje).
- Construye un **gráfico de dispersión** que relaciona el odómetro con el precio, coloreado por condición del vehículo.
- Construye un gráfico de barras con el precio mediano por tipo de vehículo.

Los gráficos se generan con **plotly-express** al marcar las casillas de verificación o al pulsar el botón.

## Estructura del proyecto

```
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
```

## Cómo ejecutarla en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Aplicación desplegada

Disponible en Render: https://TU-APP.onrender.com
