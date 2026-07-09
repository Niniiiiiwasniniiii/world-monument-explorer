import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from flask import Flask, render_template, request
import folium

from world_monument_explorer import (
    MONUMENTS,
    search_monument,
    random_monument
)

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def home():

    world_map = folium.Map(
        location=[20, 0],
        zoom_start=2,
        tiles="OpenStreetMap"
    )

    for monument in MONUMENTS:
        folium.Marker(
            location=[monument["lat"], monument["lon"]],
            popup=f"{monument['name']}<br>{monument['country']}",
            tooltip=monument["name"]
        ).add_to(world_map)

    return render_template(
        "index.html",
        map_html=world_map._repr_html_(),
        monument=None,
        message=None
    )


@app.route("/search", methods=["POST"])
def search():

    name = request.form.get("monument")

    monument = search_monument(name)

    if monument is None:

        world_map = folium.Map(
            location=[20, 0],
            zoom_start=2
        )

        return render_template(
            "index.html",
           map_html=world_map._repr_html_(),
            monument=None,
            message="Monument not found."
        )

    world_map = folium.Map(
        location=[monument["lat"], monument["lon"]],
        zoom_start=8
    )

    folium.Marker(
        location=[monument["lat"], monument["lon"]],
        popup=monument["name"],
        tooltip=monument["name"]
    ).add_to(world_map)

    return render_template(
        "index.html",
        map_html=world_map._repr_html_(),
        monument=monument,
        message=None
    )


@app.route("/random")
def random_place():

    monument = random_monument()

    world_map = folium.Map(
        location=[monument["lat"], monument["lon"]],
        zoom_start=8
    )

    folium.Marker(
        location=[monument["lat"], monument["lon"]],
        popup=monument["name"],
        tooltip=monument["name"]
    ).add_to(world_map)

    return render_template(
        "index.html",
        map_html=world_map._repr_html_(),
        monument=monument,
        message=None
    )


if __name__ == "__main__":
    app.run(debug=True)



