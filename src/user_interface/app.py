from shiny import App, ui, reactive, render
from ipyleaflet import GeoJSON, Map, Marker  
from shinywidgets import output_widget, render_widget
import leafmap.foliumap as leafmap, folium
# from branca.element import Figure
import folium
from get_municipalities import get_municipalities_list

# Get municipalities list
municipalities_list = get_municipalities_list()

app_ui = ui.page_fillable(
    ui.page_navbar(
        # First tab (Panel A)
        ui.nav_panel(
            "Dashboard",
            ui.page_sidebar(
                ui.sidebar(
                    "Input Farm Data",
                    # Input for latitude
                    ui.input_numeric("lat_input", "Enter Latitude:", value=39.99),
                    ui.input_numeric("lon_input", "Enter Longitude:", value=-8.22),
                    ui.input_action_button("update_button", "Update Map"),
                    ui.output_text_verbatim("coord_display"),
                    "OR",
                    # ui.input_text("municipality_input", "Municipality:", placeholder="Enter Municipality"),
                    ui.input_selectize(
                        "municipality_input",
                        "Municipality:",
                        choices=municipalities_list
                        # placeholder="Enter Municipality"
                    ),
                    ui.input_numeric("property_size_input", "Enter Property Size:", value=None),
                ), 
                ui.layout_columns( 
                    ui.card(
                        ui.output_ui("map_output"),
                        height="250px"),
                    ui.card("Weather Data"), 
                    ui.card("Crop Recommendation"), 
                    col_widths = [4, 4, 4]
                ),
                    ui.layout_columns( 
                    ui.card("Crop Recommendations"), 
                    ui.card("Card 2"), 
                    ui.card("Card 3"), 
                    col_widths = [6, 3, 3]
                # ) 
                ),
            )
        ),
                # Second tab (Panel B)
        ui.nav_panel(
            "Documentation",
            ui.p("Page B content")
        ),
        title="Climate-Resilient Crop Selection Tool",  
        id="page"  
    )
)

def server(input, output, session):

    @output
    @render.text
    def selected_municipality():
        return f"Selected Municipality: {input.municipality_input}"
   
    coords = reactive.Value((39.99, -8.22))  # Initialize with default coordinates

    # Effect to update coordinates only when the button is clicked
    @reactive.Effect
    # TODO: move this into another file 
    def update_button():
        if input.update_button():  # Only triggers when the button is clicked
            coords.set((input.lat_input(), input.lon_input()))

    # Render the map when the reactive value changes
    @output
    @render.ui
    def map_output():
        # Get the current coordinates
        lat, lon = coords()

        # Create the Leaflet map
        m = leafmap.Map(center=(lat, lon), zoom=5.5)
        # Add topographical map
        m.add_basemap("OpenTopoMap")
        # Add a marker at the given location 
        m.add_marker(location=(lat, lon), popup=f"Lat: {lat}, Lon: {lon}")

        # Return the Leaflet map
        return m

    # Display the current coordinates as text
    # TODO change this to match closest municipality
    @output
    @render.text
    def coord_display():
        lat, lon = coords()
        return f"{lat}, {lon}"
    
    # TODO make municipality input based on list from data

    # TODO add overlay with climate zones

# Create the app
app = App(app_ui, server)