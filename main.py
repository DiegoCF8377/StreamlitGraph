import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
import json
#REs
import requests
import streamlit as st

import streamlit as st
#test
# Check for theme parameter in URL
query_params = st.experimental_get_query_params()
theme = query_params.get("theme", ["light"])[0]  # Default to light




x = requests.get('https://hackmty24.vercel.app/api/getPlotData')

# Muestra el contenido de la respuesta de la API
print(x.text)

# Asigna el contenido de la respuesta JSON a una variable
graph_data = json.loads(x.text)

# Inicializa las listas para nodos y enlaces
nodes = []
links = []
categories = [
    {"name": "tristeza"},
    {"name": "tranquilidad"},
    {"name": "felicidad"},
    {"name": "enojo"}
]

# Función para determinar la categoría basada en el cuadrante
def determine_category(x, y):
    if x >= 0 and y >= 0:
        return 0  # Primer cuadrante
    elif x >= 0 and y < 0:
        return 1  # Cuarto cuadrante
    elif x < 0 and y < 0:
        return 2  # Tercer cuadrante
    elif x < 0 and y >= 0:
        return 3  # Segundo cuadrante

# Recorre los datos para crear los nodos
for index, item in enumerate(graph_data):
    category = determine_category(item['x'], item['y'])
    node = {
        "id": item['_id'],
        "name": item['date'],
        "x": item['x'],
        "y": item['y'],
        "category": category
    }
    nodes.append(node)

    # Crea enlaces secuenciales
    if index > 0:
        link = {
            "source": str(index - 1),
            "target": str(index)
        }
        links.append(link)

# Crea el diccionario final con nodos, enlaces y categorías
graph = {
    "nodes": nodes,
    "links": links,
    "categories": categories
}

# Muestra el resultado convertido
#print(json.dumps(graph, indent=4))

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

rojo = []
amarillo = []
verde = []
azul = []
dates = []
for g in graph["nodes"]:
    dates.append(g["name"])
    if g["x"] > 0:
        rojo.append(g["x"])
        azul.append(0)
    elif g["x"] < 0:
        azul.append(g["x"])
        rojo.append(0)
    if g["y"] > 0:
        verde.append(g["y"])
        amarillo.append(0)
        
    elif g["y"] < 0:
        amarillo.append(g["y"])
        verde.append(0)
        
print(rojo)
# Definición de las opciones del gráfico
options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {"data": ["rojo", "amarillo", "verde", "azul"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": dates,
    },
    "series": [
        {
            "name": "rojo",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": rojo,
            "itemStyle": {"color": "#111111"}, 
        },
        {
            "name": "amarillo",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": amarillo,
            "itemStyle": {"color": "yellow"},  
        },
        {
            "name": "verde",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": verde,
            "itemStyle": {"color": "green"},  
        },
        {
            "name": "azul",
            "type": "bar",
            "stack": "emociones",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": azul,
            "itemStyle": {"color": "blue"}, 
        },
    ],
}

st_echarts(options=options, height="500px")
# Cambiar el color de fondo según el tema
st.title("Energía emocional")
if theme == "dark":
    
    st.write(
        """
        <style>
        /* Cambiar el color de fondo */
        div[data-testid="stAppViewContainer"] {
            background-color: #c2c2c2;
        }
        /* Cambiar el color del texto */
        div[data-testid="stMarkdownContainer"] {
            color: #E1E1E1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.write(
        """
        <style>
        /* Cambiar el color de fondo */
        div[data-testid="stAppViewContainer"] {
            background-color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    