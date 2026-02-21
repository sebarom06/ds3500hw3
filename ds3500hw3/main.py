import panel as pn
import Scatter_Plot as sc
import Cleaning as c


api = c.DfCleaner(c.file_path)

def get_scatter_dataset(role):
    """
    returns df used in scatter plot
    """
    global api
    df = api.get_subset_scatter(role)
    return pn.pane.DataFrame(df)

def get_scatter(role, y_axis):
    """
    returns the scatter plot
    """
    global api
    scatter_df = api.points_plot(x = c.noise_type, y = y_axis, color = c.noise_type, role = role)
    fig = sc.make_scatter(scatter_df, color_map = c.color_map, x = c.noise_type, y = y_axis, color = c.noise_type,
                          title = "Comparing Focus Score with Background Noise Types ")
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
    y_axis_select = pn.widgets.Select(name = "Y Axis",
                                     options = [
                                         "perceived_focus_score",
                                         "task_completion_quality",
                                         "mental_fatigue_after_task"
                                     ])

    # Todo: seba, add the creation of ur bar widgets here

    # connecting widgets to functions
    scatter_dataset = pn.bind(get_scatter_dataset, role_select)
    scatter_plot = pn.bind(get_scatter, role_select, y_axis_select)
    # Todo: connect your widgets to the datasetyou want the widget to use
    # it's in the syntax of (dataset, whatevery widgets need to use that dataset)

    # dashboard
    scatter_search = pn.Card(
        pn.Column(
            role_select,
            y_axis_select,
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
        header_background = "blue"
    )

    layout.show()



if __name__ == "__main__":
    main()