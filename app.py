import os
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

'''
AI Usage:
AI was used in the process of setting up our project in Render.com.
AI helped generate and correct the requirements.txt file while caused the build deployment to fail.
AI pointed out that for render to run our code, we would have to make adjustments to our app.run ports and also include the import os line to the header of the code.
'''


app = Dash(__name__,use_pages=True, external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True,title="Team 13! CTBA")
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
    port = int(os.environ.get("PORT", 8050))  #line sourced from GPT
    app.run(host="0.0.0.0", port=port, debug=True)
