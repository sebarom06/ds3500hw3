import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def no_underscore(text):
    """
    makes underscores into spaces and makes lowercase into uppercase
    """
    return text.replace("_", " ").title()
def make_scatter(df, color_map, x, y, color, title = ""):
    """
    makes the scatter plot with different colors to different types
    """
    fig = px.scatter(
        df,
        x = x,
        y = y,
        color_discrete_map = color_map,
        color = color,
        title = title,
        labels = {x: no_underscore(x), y : no_underscore(y)}
    )

    return fig
