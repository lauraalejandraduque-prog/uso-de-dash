import plotly.express as px
from dash import Dash, dcc, html

app = Dash() #Iniciamos una aplicación de tipo dash

datos = px.data.tips() #guardamos los datos de plotly express
mi_figura = px.pie(datos, names="sex", values="tip") #guarda el gráfico en una variable

datos1 = px.data.gapminder()
datos_1952 = datos1[datos1["year"] == 1952]
grafico = px.bar(datos_1952, x="continent", y="pop")

app.layout = html.Div([
    html.H1("Gráfico de pastel con Plotly y Dash"),
    dcc.Graph(figure=mi_figura),
    html.H1("Población por continente (1952)"),
    dcc.Graph(figure=grafico)
])

app.run(debug=True, use_reloader=False)