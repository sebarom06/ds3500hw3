import pandas as pd

critical_col = ["role", "task_type", "background_noise_type"]
ind = "focus_duration_minutes"
dpd = "perceived_focus_score"
noise_type = "background_noise_type"
file_path = "background_noise_focus_dataset.csv"

class dfCleaner:
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

    def points_plot(self, x = ind, y = dpd, color = noise_type):
        """
        creating dataframe suitable for plot
        """
        result = self.df[[x, y, color]]
        return result

def main():
    dataf = dfCleaner(file_path)
    dataf.clean_data()
    print(dataf.df)

if __name__ == "__main__":
    main()