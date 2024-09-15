import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
import json
#REs
import requests
"""
# Realiza la solicitud GET a la API
x = requests.get('http://localhost:3000/api/addDataStream')

# Muestra el contenido de la respuesta de la API
print(x.text)

# Asigna el contenido de la respuesta JSON a una variable
graph = json.loads(x.text)

for idx, _ in enumerate(graph["nodes"]):
    graph["nodes"][idx]["symbolSize"] = 15

option = {
    "title": {
        "text": "Mapa de emociones",
        "subtext": "Default layout",
        "top": "bottom",
        "left": "right",
    },
    "tooltip": {},
    "legend": [{"data": [a["name"] for a in graph["categories"]]}],
    "series": [
        {
            "name": "Les Miserables",
            "type": "graph",
            "layout": "none",
            "data": graph["nodes"],
            "links": graph["links"],
            "categories": graph["categories"],
            "roam": False,
            "label": {"position": "right"},
            "draggable": False,
            "force": {"repulsion": 100},
        }
    ],
}
st_echarts(option, height="500px")
#st.title("Gráfico de Área Apilada")


"""

# Definición de las opciones del gráfico
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {"data": ["rojo", "amarillo", "verde", "azul"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["13/09", "14/09", "15/09", "16/09", "17/09", "18/09", "19/09"],
    },
    "series": [
        {
            "name": "rojo",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": np.random.randint(0, 10, 7).tolist(),
            "itemStyle": {"color": "red"},  # Color de las barras rojas
        },
        {
            "name": "amarillo",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": np.random.randint(0, 10, 7).tolist(),
            "itemStyle": {"color": "yellow"},  # Color de las barras amarillas
        },
        {
            "name": "verde",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": np.random.randint(0, 10, 7).tolist(),
            "itemStyle": {"color": "green"},  # Color de las barras verdes
        },
        {
            "name": "azul",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": np.random.randint(0, 10, 7).tolist(),
            "itemStyle": {"color": "blue"},  # Color de las barras azules
        },
    ],
}

# Renderizar el gráfico en Streamlit
st_echarts(options=options, height="500px")
