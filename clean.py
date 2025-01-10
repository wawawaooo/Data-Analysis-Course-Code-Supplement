import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Reading Data
covid_19 = pd.read_csv("covid_19.csv")
covid_age = pd.read_csv("covid_age.csv")

# Clean up column names
covid_19.columns = covid_19.columns.str.strip()
covid_age.columns = covid_age.columns.str.strip()

# Rename columns
covid_19.rename(columns={"Date": "date"}, inplace=True)
covid_age.rename(columns={"Date Administered": "date"}, inplace=True)

# Delete extra columns
covid_19.drop(columns=["data"], inplace=True, errors='ignore')
covid_age.drop(columns=["date.Administered"], inplace=True, errors='ignore')

# Cleaning up time strings
def clean_date_column(date):
    return date.replace(" 12:00:00 AM", "")

covid_age["date"] = covid_age["date"].apply(clean_date_column)

# Group by date and sum
covid_19_group = covid_19.groupby("date").sum(numeric_only=True).reset_index()

# Merge Datasets
wrangling_df = pd.merge(covid_19_group, covid_age, on="date", how="inner")

# Replace NA with 0
wrangling_df.fillna(0, inplace=True)

# Create a new column
wrangling_df["Administered_Daily_Pct"] = (wrangling_df["Administered_Daily"] / wrangling_df["Administered_Cumulative"]) * 100
wrangling_df["Series_Complete_Daily_Pct"] = (wrangling_df["Series_Complete_Daily"] / wrangling_df["Series_Complete_Cumulative"]) * 100
wrangling_df["Series_Complete_Ratio"] = wrangling_df["Series_Complete_Daily"] / wrangling_df["Administered_Daily"]
wrangling_df["Booster_Daily_Pct"] = (wrangling_df["Booster_Daily"] / wrangling_df["Booster_Cumulative"]) * 100
wrangling_df["Booster_Ratio"] = wrangling_df["Booster_Daily"] / wrangling_df["Administered_Daily"]

# Convert date to datetime format
wrangling_df["date"] = pd.to_datetime(wrangling_df["date"], errors="coerce")

# Filter data for the years 2021 and 2022
wrangling_df = wrangling_df[wrangling_df["date"].dt.year.isin([2021, 2022])]

# Sort by date
wrangling_df.sort_values(by="date", inplace=True)

# Save the cleaned data
wrangling_df.to_csv("wrangling_df.csv", index=False)

# Generate chart function
def generate_plot1(month, year):
    df = wrangling_df[(wrangling_df["date"].dt.month == month) & (wrangling_df["date"].dt.year == year)]
    df_grouped = df.groupby("AgeGroupVacc")["Series_Complete_Pop_pct_agegroup"].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_grouped, x="AgeGroupVacc", y="Series_Complete_Pop_pct_agegroup")
    sns.lineplot(data=df_grouped, x="AgeGroupVacc", y="Series_Complete_Pop_pct_agegroup", linestyle="--")
    plt.xticks(rotation=45)
    plt.title("Series Complete Vaccination by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Series Complete Cumulative")
    plt.show()

def generate_plot2(month, year):
    df = wrangling_df[(wrangling_df["date"].dt.month == month) & (wrangling_df["date"].dt.year == year)]
    df_grouped = df.groupby("AgeGroupVacc")["Administered_Dose1_pct_agegroup"].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_grouped, x="AgeGroupVacc", y="Administered_Dose1_pct_agegroup", color="skyblue")
    plt.xticks(rotation=45)
    plt.title("Average Vaccination by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Average Vaccination (%)")
    plt.show()

def generate_plot3(month, year):
    df = wrangling_df[(wrangling_df["date"].dt.month == month) & (wrangling_df["date"].dt.year == year)]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="Administered_Daily", y="Series_Complete_Daily")
    sns.regplot(data=df, x="Administered_Daily", y="Series_Complete_Daily", scatter=False, color="red", line_kws={"linestyle": "dashed"})
    plt.title("Administered Daily vs Series Complete Daily")
    plt.xlabel("Administered Daily")
    plt.ylabel("Series Complete Daily")
    plt.show()

if __name__ == "__main__":
    print("Cleaned data")
    print(wrangling_df.head(50))   #type whay you want



