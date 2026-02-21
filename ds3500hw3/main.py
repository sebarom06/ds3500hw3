import panel as pn
import Box_plot as sc
import Cleaning as c


api = c.DfCleaner(c.file_path)

def get_box_dataset(role):
    """
    returns df used in box plot
    """
    global api
    df = api.get_subset_box(role)
    return pn.pane.DataFrame(df)

def get_box(role, y_axis):
    """
    returns the box plot
    """
    global api
    box_df = api.points_plot(x = c.noise_type, y = y_axis, color = c.noise_type, role = role)
    fig = sc.make_box(box_df, color_map = c.color_map, x = c.noise_type, y = y_axis, color = c.noise_type,
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
    # box dropdown menu widget
    role_select = pn.widgets.Select(name = "Roles", options = api.get_role())

    # box y axis select
    y_axis_select = pn.widgets.Select(name = "Y Axis",
                                      options={
                                          sc.no_underscore(col): col
                                          for col in [
                                              "perceived_focus_score",
                                              "task_completion_quality",
                                              "mental_fatigue_after_task"
                                          ]
                                      })

    # Todo: seba, add the creation of ur bar widgets here

    # connecting widgets to functions
    box_dataset = pn.bind(get_box_dataset, role_select)
    box_plot = pn.bind(get_box, role_select, y_axis_select)
    # Todo: connect your widgets to the datasetyou want the widget to use
    # it's in the syntax of (dataset, whatevery widgets need to use that dataset)

    # dashboard
    box_search = pn.Card(
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
            box_search
        ],
        theme_toggle = False,
        main = [
            pn.Tabs(# Todo: make a seperate object (tab) for bar plot dataset and plot
                ("Box Plot Dataset", box_dataset),
                ("Box Plot", box_plot),
                active = 1
            )
        ],
        header_background = "blue"
    )

    layout.show()



if __name__ == "__main__":
    main()