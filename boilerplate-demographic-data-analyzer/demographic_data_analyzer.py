import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"] == "Male"]["age"]
    average_age_men = round(np.mean(average_age_men) , 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df[df["education"] == "Bachelors"])
    people_count = len (df["education"])
    percentage_bachelors = round(100* (percentage_bachelors / people_count) , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[df["education"] == "Bachelors"]) + len(df[df["education"] == "Masters"]) +len(df[df["education"] == "Doctorate"])
    higher_education = round(100* (higher_education / people_count) , 1)

    lower_education = people_count - (len(df[df["education"] == "Bachelors"]) + len(df[df["education"] == "Masters"]) +len(df[df["education"] == "Doctorate"]))
    lower_education = round(100* (lower_education / people_count) , 1)


    # percentage with salary >50K
    higher_education_list = (df.loc[((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"))])
    lower_education_list = (df.loc[(df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")])

    higher_education_rich_list = higher_education_list.loc[higher_education_list["salary"] == ">50K"]
    lower_education_rich_list = lower_education_list.loc[lower_education_list["salary"] == ">50K"]

    higher_education_count = len(higher_education_list)
    higher_education_rich_count = len( higher_education_rich_list)
    higher_education_rich = round(100* (higher_education_rich_count / higher_education_count) , 1)

    lower_education_count = len(lower_education_list)
    lower_education_rich_count = len( lower_education_rich_list)
    lower_education_rich = round(100* (lower_education_rich_count / lower_education_count) , 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours_count = df.loc[df["hours-per-week"] == df["hours-per-week"].min()]
    num_min_workers = len(df.loc[df["hours-per-week"] == df["hours-per-week"].min()])
    num_min_workers_rich = len(min_work_hours_count.loc[min_work_hours_count["salary"] == ">50K"])

    rich_percentage = round(100* (num_min_workers_rich / num_min_workers) , 1)

    # What country has the highest percentage of people that earn >50K?
    new_df = df.loc[df["salary"] == ">50K"]["native-country"].value_counts()
    new_df2 = df["native-country"].value_counts()
    richest = (new_df/new_df2).max()

    highest_earning_country = (new_df/new_df2).sort_values(ascending=False).index[0]
    highest_earning_country_percentage = round((100* richest), 1)


   # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[df["native-country"] == "India"]["occupation"].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
