import panel as pn
import Scatter_Plot as sc
import Cleaning as c

api = c.DfCleaner(c.file_path)

def get_scatter_dataset(role, min_noise):
    """
    returns df used in scatter plot
    """
    global api
    df = api.get_subset_scatter(role, min_noise)
    return pn.pane.DataFrame(df)

def get_scatter(df, color_map, x, y, color, role, title):
    """
    returns the scatter plot
    """
    global api
    scatter_df = api.points_plot(x, y, color, role)
    fig = sc.make_scatter(scatter_df, color_map, x, y, color, title)
    return fig

def get_bar_dataset():
    pass

def get_bar():
    pass

def main():
    pn.extension()

    global api
    api.clean_data()

    # widgets
    # scatter dropdown menu widget
    role_select = pn.widgets.Select(name = "Roles", options = api.get_role())

    # scatter noise volume level slider
    noise_slider = pn.widgets.IntSlider(name = "Noise Volume", start = 0, end = 10, step = 1, value = 0)

    # Todo: seba, add the creation of ur bar widgets here

    # connecting widgets to functions
    scatter_dataset = pn.bind(get_scatter_dataset, role_select, noise_slider)
    scatter_plot = pn.bind(get_scatter, role_select, noise_slider)
    # Todo: connect your widgets to the datasetyou want the widget to use
    # it's in the syntax of (dataset, whatevery widgets need to use that dataset)

    # dashboard
    scatter_search = pn.Card(
        pn.Column(
            role_select,
            noise_slider
        ),
        title = "Search", collapsed = False
    )
    # Todo: make a seperate dashboard car for bar

    # layout
    layout = pn.template.FastListTemplate(
        title = "Background Noise and Focus",
        sidebar = [
            scatter_search
        ],
        theme_toggle = False,
        main = [
            pn.Tabs(# Todo: make a seperate object (tab) for bar plot dataset and plot
                ("Scatter Plot Dataset", scatter_dataset),
                ("Scatter Plot", scatter_plot),
                active = 1
            )
        ],
        header_backgorund = "blue"
    ).servable()

    layout.show()



if __name__ == "__main__":
    main()