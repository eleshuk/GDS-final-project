from shiny import App, ui, reactive, render
from ipyleaflet import GeoJSON, Map, Marker  
from shinywidgets import output_widget, render_widget
import leafmap.foliumap as leafmap, folium
# from branca.element import Figure
import folium


app_ui = ui.page_sidebar(
    ui.sidebar("Input Farm Data", 
            # # Input for latitude
        ui.input_numeric("lat_input", "Enter Latitude:", value=39.99),
        ui.input_numeric("lon_input", "Enter Longitude:", value=-8.22),
        ui.input_action_button("update_button", "Update Map"),
        ui.output_text_verbatim("coord_display"),
        "OR",
        ui.input_text("municipality_input", "Municipality:", "Enter Municipality")
    ),
    ui.layout_columns(
        ui.card(
            ui.output_ui("map_output"),
        ),
        ui.card(
            ui.output_text_verbatim("message", "Example data"),
        ),
    ),
    title="Climate-Resilient Crop Selection Tool",
)


# Define server
def server(input, output, session):
   
    coords = reactive.Value((39.99, -8.22))  # Initialize with default coordinates

    # Effect to update coordinates only when the button is clicked
    @reactive.Effect
    def update_coords_on_click():
        if input.update_button():  # Only triggers when the button is clicked
            coords.set((input.lat_input(), input.lon_input()))

    # Render the map when the reactive value changes
    @output
    @render.ui
    def map_output():
        # Get the current coordinates
        lat, lon = coords()

        # Create the Leaflet map
        m = leafmap.Map(center=(lat, lon), zoom=6)
        # Add a marker at the given location
        m.add_marker(location=(lat, lon), popup=f"Lat: {lat}, Lon: {lon}")

        # Return the Leaflet map
        return m

    # Display the current coordinates as text
    # TODO change this to match correct 
    @output
    @render.text
    def coord_display():
        lat, lon = coords()
        return f"{lat}, {lon}"
    
    # TODO make municipality input based on list from data

# Create the app
app = App(app_ui, server)