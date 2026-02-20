import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def make_bar_plot(df, color_map, x, y, color, title=''):
    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        title=title
        )

    fig.show()