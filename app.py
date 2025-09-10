import os
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__,use_pages=True, external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True,title="Final Project")
server = app.server

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavLink("Introduction", href="/", active="exact", className='headernav head-hover'),
            dbc.NavLink("Employment series", href="/FinalPage1", active="exact", className='headernav head-hover'),
            dbc.NavLink("Choropleth", href="/FinalPage2", active="exact", className='headernav head-hover'),
            dbc.NavLink("Wage Series", href="/FinalPage3", active="exact", className='headernav head-hover')
        ],
        brand="Employment & Wage Dash",
        brand_style = {'fontFamily':'Montserrat, sans-serif', 'fontSize':'32px', 'fontWeight':'semibold'},
        color="#080121",
        dark=True,
        className="mb-4"
    ),
    page_container
],className='Divstyle')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))  # use Render's PORT or default 8050
    app.run(host="0.0.0.0", port=port, debug=True)
