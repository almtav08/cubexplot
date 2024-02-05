from dash import Dash, dcc, html
import plotly.graph_objects as go
import polars as pl

# Crear la aplicación Dash
app = Dash(__name__)
server=app.server

# Crear datos de ejemplo
data = pl.read_csv("plots.csv")

# Crear figura con Plotly Express
limit = data.shape[0]
symbols = ['circle' for _ in range(limit)]
colors = ['blue' for _ in range(limit)]
marker=dict(size=2, color=colors, opacity=0.8, symbol=symbols)

fig = go.Figure(data=[go.Scatter3d(x=list(data['percentage']), y=list(data['concepts']), z=list(data['secs']), mode='markers', marker=marker)])
fig.update_layout(scene=dict(xaxis_title='Percentage ', yaxis_title='N concepts', zaxis_title='Seconds'), margin=dict(l=0, r=0, t=0, b=0))

# Definir el diseño de la aplicación Dash
app.layout = html.Div([
    dcc.Graph(id='scatter-plot', figure=fig, style={'width': '100%', 'height': '100%'})
], style={'width': '98dvw', 'height': '98dvh'})

app.title = 'Video metadata plotting'

# Iniciar la aplicación Dash
if __name__ == '__main__':
    app.run(debug=False)
