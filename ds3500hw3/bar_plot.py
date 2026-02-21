import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def make_bar_plot(df, x, y, color, title=''):
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
        color=color,
        barmode="group",
        labels={x: x.replace("_", " ").title(), y: y.replace("_", " ").title()}
    )

    return fig