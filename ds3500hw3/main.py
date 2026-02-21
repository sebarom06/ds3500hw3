import panel as pn
import Box_plot as sc
import bar_plot as bp
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

def get_bar_dataset(x_group):
    """"
    returns df used in bar plot
    """
    global api
    df = api.bar_points(x_group=x_group)
    return pn.pane.DataFrame(df)



def get_bar(x_group):
    """
    returns bar plot
    """
    global api
    bar_df = api.bar_points(x_group=x_group)
    fig = bp.make_bar_plot(bar_df, x="x_category", y="focus_duration_minutes",
                           color="noise_type", title="Avg Study Time by " + x_group.replace("_", " ").title())
    return fig

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

    x_group_select = pn.widgets.RadioButtonGroup(
        name="View By",
        options=["role", "task_type"],
        value="role"
    )

    # connecting widgets to functions
    box_dataset = pn.bind(get_box_dataset, role_select)
    box_plot = pn.bind(get_box, role_select, y_axis_select)
    bar_dataset = pn.bind(get_bar_dataset, x_group_select)
    bar_plot = pn.bind(get_bar, x_group_select)

    # it's in the syntax of (dataset, whatevery widgets need to use that dataset)

    # dashboard
    box_search = pn.Card(
        pn.Column(
            role_select,
            y_axis_select,
        ),
        title = "Search", collapsed = False
    )
    bar_search = pn.Card(
        pn.Column(x_group_select),
        title="Bar Search", collapsed=False
    )


    # layout
    layout = pn.template.FastListTemplate(
        title = "Background Noise and Focus",
        sidebar = [
            box_search,
            bar_search,
        ],
        theme_toggle = False,
        main = [
            pn.Tabs(
                ("Box Plot Dataset", box_dataset),
                ("Box Plot", box_plot),
                ("Bar Plot Dataset", bar_dataset),
                ("Bar Plot", bar_plot),
                active=1
            )
        ],
        header_background = "blue"
    )


    layout.show()



if __name__ == "__main__":
    main()