import pandas as pd
import csv

merged_data = pd.read_csv("merged_star_data.csv")

print(merged_data.columns)

merged_data.drop(columns=["Luminosity"], inplace=True)

merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

merged_data.dropna(inplace=True)

merged_data.to_csv("cleaned_merged_star_data.csv", index=False)
