import os
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__,use_pages=True, external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True,title="Final Project")
server = app.server

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavLink("Introduction", href="/", active="exact", className='headernav'),
            dbc.NavLink("Employement series", href="/FinalPage1", active="exact", className='headernav'),
            dbc.NavLink("Choropleth", href="/FinalPage2", active="exact", className='headernav'),
            dbc.NavLink("Wage Series", href="/FinalPage3", active="exact", className='headernav')
        ],
        brand="Employment & Wage Dash",
        color="primary",
        dark=True,
        className="mb-4"
    ),
    page_container
],className='Divstyle')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))  # use Render's PORT or default 8050
    app.run_server(host="0.0.0.0", port=port, debug=True)
