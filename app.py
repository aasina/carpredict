import streamlit as st
from multiapp import MultiApp
from apps import home, graph, predict  # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Graph", graph.app)
app.add_app("Predict", predict.app)

# The main app
app.run()