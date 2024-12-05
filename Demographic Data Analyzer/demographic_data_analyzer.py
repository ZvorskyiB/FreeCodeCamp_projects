import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('Demographic Data Analyzer\\adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = np.array(df['race'].value_counts().reset_index()['count'])

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100*len(df[df['education']=='Bachelors'])/len(df), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = 100*np.sum(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))/len(df) 
    lower_education = 100*np.sum(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))/len(df) 

    # percentage with salary >50K
    higher_education_rich = round(100*np.sum((df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))&(df['salary']=='>50K'))/np.sum(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])),1)
    lower_education_rich = round(100*np.sum((~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))&(df['salary']=='>50K'))/np.sum(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = np.sum(df['hours-per-week']==df['hours-per-week'].min()) 

    rich_percentage = 100*np.sum((df['hours-per-week']==df['hours-per-week'].min())&(df['salary']=='>50K'))/np.sum(df['hours-per-week']==df['hours-per-week'].min())

    # What country has the highest percentage of people that earn >50K?
    p=[]
    for state in df['native-country'].unique():
      p.append(100*np.sum((df['native-country']==state)&(df['salary']=='>50K'))/np.sum(df['native-country']==state))
    States=pd.DataFrame(index=df['native-country'].unique(), data={'percentage': p})
    highest_earning_country = States[States['percentage']==States['percentage'].max()].index[0]
    highest_earning_country_percentage = round(States['percentage'].max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country']=='India')&(df['salary']=='>50K')]['occupation'].describe().iloc[2]

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