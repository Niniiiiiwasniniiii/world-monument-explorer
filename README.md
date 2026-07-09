# 🌍 World Monument Explorer

A simple interactive web app that lets users explore famous monuments from around the world on an interactive map.

This project was built using **Python**, **Flask**, and **Folium**. It started as a Streamlit project, but I later converted it into a Flask application so it could be deployed online.

---

## Features

- 🗺️ Interactive world map
- 📍 Markers for famous monuments
- 🔎 Search monuments by name
- 🎲 Random monument generator
- 📖 Read a short history of each monument
- 💡 Fun facts about every monument

---

## Built With

- Python
- Flask
- Folium
- HTML
- CSS

---

## Project Structure

```
world-monument-explorer/
│
├── api/
│   └── index.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── world_monument_explorer.py
├── requirements.txt
├── vercel.json
└── README.md
```

---

## Running Locally

Clone the repository

```bash
git clone https://github.com/Niniiiiiwasniniiii/world-monument-explorer.git
```

Go into the project folder

```bash
cd world-monument-explorer
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the app

```bash
python -m api.index
```

Then open:

```
http://127.0.0.1:5000
```

---

## What I Learned

This project taught me a lot more than I expected.

Some things I learned while building it:

- Working with Flask routing
- Building interactive maps using Folium
- Using HTML templates with Jinja
- Connecting Python with a frontend
- Git and GitHub basics
- Deploying a Python project
- Debugging import errors and template errors


---

## Challenges

Some of the challenges I faced included:

- Learning how templates work
- Making the project deployment-ready
- Debugging several runtime and template errors

Although it took a while, solving each issue helped me understand how Flask applications are structured.

---

## Future Improvements

Some features I'd like to add in the future:

- More monuments from different countries
- Filters by continent
- Images for every monument
- Dark mode
- "Nearby monuments" feature
- Quiz mode to test geography knowledge
- Better UI and animations

---

## Author

Made by **nini**

```
Learning Python one project at a time :)
```
