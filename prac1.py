import pandas as pd
import numpy as np

class EmployeeTrainingDashboard:
    def __init__(self):
        self.df = None

    def create_training_df(self, training_data: list) -> pd.DataFrame:
        columns = ['Team', 'EmployeeName', 'Score', 'Result']
        df = pd.DataFrame(training_data, columns=columns)
        self.df = df  # Store for later use
        return df
    
    def team_score_summary(self, df: pd.DataFrame) -> pd.DataFrame:
        summary = df.groupby("Team")["Score"].agg(TotalScore="sum", AverageScore="mean").reset_index()
        return summary

    def add_result_points(self, df: pd.DataFrame) -> pd.DataFrame:
        def compute(result):
            if result == 'Pass':
                return 3
            else: 
                return 0
        self.df['Points'] = df['Result'].apply(compute)
        return self.df
    
    def filter_high_scorers(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
        return df[df["Score"] > n][["Team", "EmployeeName", "Score", "Result"]]
    
    def compute_pass_rate(self, df: pd.DataFrame) -> pd.DataFrame:
        pass_counts = df.groupby("Team")["Result"].value_counts().unstack().fillna(0)
        pass_counts["PassRate"] = (pass_counts["Pass"] / pass_counts.sum(axis=1)) * 100
        return pass_counts[["PassRate"]].reset_index()

    def top_teams_by_points(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
        team_points = df.groupby("Team")["Points"].sum().reset_index(name="TotalPoints")
        return team_points.sort_values(by="TotalPoints", ascending=False).head(n)