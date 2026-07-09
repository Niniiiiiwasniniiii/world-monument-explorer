from flask import Flask, render_template, request
import folium 
from world_monument_explorer import (
    MONUMENTS,
    find_nearest_monument,
    search_monument
)
app = Flask (
    __name__,
    template_folder = '../templates',
    static_folder="../static"
)

@app.route("?")
def home():
    world_map = folium.Map(
        location=[20,0],
        zoom_start=2,
        tiles="OpenStreetMap"
    )
    for world_monument_explorer in MONUMENTS :
        folium.Marker(
            location=[world_monument_explorer["lat"],
                      world_monument_explorer["lot"]],
                      popup= f"{world_monument_explorer['name']}<br>{world_monument_explorer['name']}",
                      toppltip=world_monument_explorer["name"]

        ).add_to(world_map)
        map_html = world_map._repr_html()
        return render_template(
            "index.html",
            map_html=map_html
        )
    
    @app.route("/search", methods= ["POST"])
    def search():
       MONUMENTS = request.form.get("monument")
       world_monument_explorer = search_monument(MONUMENTS)
       if world_monument_explorer is None:
           return render_template(
               "index.html",
               message= "Monument not found."
           )
       world_map = folium.Map(
           location= [world_monument_explorer["lat"], world_monument_explorer["lon"]],
           zoom_start=8
       )
       folium.Marker(
           location = [world_monument_explorer["lat"], world_monument_explorer["lon"]],
           popup=world_monument_explorer["name"],
           tooltip=world_monument_explorer["name"]
       ).add_to(world_map)
       return render_template(
           "index.html",
           map_html=world_map._repr_html(),
           world_monument_explorer = MONUMENTS
       )
    @app.route("/random")
    def random_place():
        world_monument_explorer = MONUMENTS()
        world_map = folium.Map(
            location= [world_monument_explorer["lat"], world_monument_explorer["lon"]],
            zoom_start=8
        )
        folium.Marker(
            location= [world_monument_explorer["lat"], world_monument_explorer["lon"]],
            popup=world_monument_explorer["name"],
            tooptip=world_monument_explorer["name"]
        ).add_to(world_map)
        return render_template(
            "index.html",
            map_html-world_map._repr_html_(),
            world_monument_explorer=MONUMENTS
        )
    if __name__ == "__main__":
        app.run(debug=True)





