import faicons as fa
import plotly.express as px

# Load data and compute static values
from shared import app_dir, tips
from shinywidgets import output_widget, render_plotly

from shiny import App, reactive, render, ui

from shiny import App, ui, render
from shinywidgets import output_widget, register_widget
import ipyleaflet

from shiny import App, ui, render
from shinywidgets import output_widget, register_widget
import ipyleaflet

# Shiny app UI
app_ui = ui.page_fluid(
    ui.h2("Leaflet Map with Drawing Tools"),
    output_widget("leaflet_map")  # Output container for the map
)

def server(input, output, session):
    # Create the Leaflet map
    m = ipyleaflet.Map(center=(39.3999, -8.2245), zoom=6)
    
    # Add drawing control to the map
    from ipyleaflet import DrawControl
    draw_control = DrawControl()

    # Configure draw options
    draw_control.circle = {}
    draw_control.circlemarker = {}
    draw_control.polygon = {
        "shapeOptions": {
            "color": "#6bc2e5",
            "weight": 4
        }
    }
    draw_control.rectangle = {
        "shapeOptions": {
            "color": "#e56b6b",
            "weight": 4
        }
    }
    draw_control.polyline = {}

    # Add event handler for drawing completion
    def handle_draw(target, action, geo_json):
        print("Drawn geometry:", geo_json)  # Print GeoJSON of the drawn shape

    draw_control.on_draw(handle_draw)

    # Add the draw control to the map
    m.add_control(draw_control)

    # Register the map widget to Shiny
    register_widget("leaflet_map", m)

app = App(app_ui, server)


