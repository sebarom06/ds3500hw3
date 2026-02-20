import pandas as pd

critical_col = ["role", "task_type", "background_noise_type"]
ind = "focus_duration_minutes"
dpd = "perceived_focus_score"
noise_type = "background_noise_type"
file_path = "background_noise_focus_dataset.csv"
#Todo write column names you want to use for barchart
categorical = "role"
numerical = "focus_duration_minutes"

class DfCleaner:
    def __init__(self, filename):
        """
        loads data into the dataframe
        path to filename
        """
        self.df = pd.read_csv(filename)

    def clean_data(self, critical = critical_col):
        """
        dropping Nan if its in critical columns
        """
        self.df = self.df.dropna(subset = critical)

    def get_role(self):
        """
        returns list of roles to choose from
        """
        roles = self.df["role"].unique().tolist()
        roles.sort()
        return ["All Roles"] + roles

    def get_subset_scatter(self, role = "role", min_noise = 0):
        """
        getting subset for scatter plot
        drop down menu of roles
        noise volume level slider
        """
        df = self.df.copy()

        if role != "All Roles":
            df = df[df["role"] == role]

        df = df[df["noise_volume_level"] >= min_noise]

        return df

    def get_subset_bar(self, x_group = "role"):
        """
        getting subset for the barchart
        """
        df = self.df.copy()

        df = df.groupby([x_group, "background_noise_type"])["focus_duration_minutes"].mean().reset_index()
        df.columns = ["x_category", "noise_type", "focus_duration_minutes"]

        # Todo: make subset for whatever other widget you do

        return df

    def points_plot(self, x = ind, y = dpd, color = noise_type, role = "role"):
        """
        creating dataframe suitable for plot
        """
        df = self.get_subset_scatter(role)

        result = df[[x, y, color]]
        return result

    def bar_points(self, x = categorical, y = numerical, x_group = "role"):
        """
        creates bar plot dataframe with the subset of chosen role
        """
        # Todo: how do you feel about using button group to choose the y data (numerical)
        # Todo: so they can choose between perceived focus, task completion, etc
        df = self.get_subset_bar(x_group)

        return df

def main():
    datadf = DfCleaner(file_path)
    datadf.clean_data()
    print(datadf.points_plot(role = ""))


if __name__ == "__main__":
    main()