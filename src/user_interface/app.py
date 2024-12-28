from shiny import App, ui, reactive, render
from ipyleaflet import GeoJSON, Map, Marker  
from shinywidgets import output_widget, render_widget
import leafmap.foliumap as leafmap, folium
# from branca.element import Figure
import folium


app_ui = ui.page_sidebar(
    ui.sidebar("Input Farm Data", 
            # # Input for latitude
            # ui.input_text("lat_input", "Latitude:", "Enter Latitude"),
            # # Input for longitude
            # ui.input_text("long_input", "Longitude:", "Enter Longitude"),
            # "OR",
            # ui.input_text("municipality_input", "Municipality:", "Enter Municipality")
        ui.input_numeric("lat_input", "Enter Latitude:", value=39.99),
        ui.input_numeric("lon_input", "Enter Longitude:", value=-8.22),
        ui.input_action_button("update_button", "Update Map"),
        ui.output_text_verbatim("coord_display"),
        "OR",
        ui.input_text("municipality_input", "Municipality:", "Enter Municipality")
    ),
    ui.layout_columns(
        ui.card(
            output_widget("map_output"),
        ),
        ui.card(
            output_widget("map1"),
        ),
    ),
    title="Climate-Resilient Crop Selection Tool",
)


# Define the server
# def server(input, output, session):
    # @render_widget  
    # def map():
    #     # PT: 39.3999° N, 8.2245° W
    #     return Map(center=(39.3999, -8.2245), zoom=6) 

def server(input, output, session):
    # Reactive value to track the updated coordinates
    updated_coords = reactive.Value((39.99, -8.22))  # Initialize with default coordinates from inputs

    # Update the coordinates only when the button is clicked
    @reactive.Effect
    def on_button_click():
        if input.update_button():
            updated_coords.set((input.lat_input(), input.lon_input()))

    # # Function to create the map
    # def create_map(lat, lon):
    #     # Create a map centered on the provided coordinates
    #     m = folium.Map(location=(lat, lon), zoom_start=4)
    #     # Add a marker at the coordinates
    #     folium.Marker([lat, lon], popup=f"Lat: {lat}, Lon: {lon}").add_to(m)
    #     return m

    # # Render the map when the reactive value changes
    # @output
    # @render.ui
    # def map_output():
    #     # Get the current coordinates
    #     lat, lon = updated_coords()
    #     # Generate the folium map
    #     m = create_map(lat, lon)
    #     # Return the HTML representation of the map
    #     return ui.HTML(m._repr_html_())

    # # Display the current coordinates as text
    # @output
    # @render.text
    # def coord_display():
    #     lat, lon = updated_coords()
    #     return f"Current Coordinates: Latitude = {lat}, Longitude = {lon}"

    # Render the map when the reactive value changes
    @output
    @render.ui
    def map_output():
        # Get the current coordinates
        lat, lon = updated_coords()

        # Create the Leaflet map
        m = leafmap.Map(center=(lat, lon), zoom=4)
        # Add a marker at the given location
        m.add_marker(location=(lat, lon), popup=f"Lat: {lat}, Lon: {lon}")

        # Return the Leaflet map
        return m

    # Display the current coordinates as text
    @output
    @render.text
    def coord_display():
        lat, lon = updated_coords()
        return f"Current Coordinates: Latitude = {lat}, Longitude = {lon}"

# Create the app
app = App(app_ui, server)