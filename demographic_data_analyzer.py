import pandas as pd

def calculate_demographic_data(print_data=True):
# Read data from the file (assuming the file is named 'adult_data.csv')
    df = pd.read_csv('adult.data.csv')

# How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

# What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

# What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (advanced_education['salary'] == '>50K').mean() * 100

# What percentage of people without advanced education make more than 50K?
    non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (non_advanced_education['salary'] == '>50K').mean() * 100

# What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

# What percentage of people who work the minimum number of hours per week have a salary of >50K?
    min_hours_per_week_earners = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (min_hours_per_week_earners['salary'] == '>50K').mean() * 100

# What country has the highest percentage of people that earn >50K?
    country_list = pd.DataFrame(data=df['native-country'].unique(), columns = ["native-country"])
    country_list['High_Earners'] = 0
    country_list['High_Earners_Ratio'] = 0

    country_list.set_index('native-country')

    filter_salary = df['salary'] == '>50K' 

    for i, row in country_list.iterrows():
        filter = df['native-country'] == row['native-country']
        country_list.iloc[i, 1] = df['native-country'].where(filter_salary & filter).dropna().count()
        country_list.iloc[i, 2] = country_list.iloc[i, 1] / df['native-country'].where(filter).dropna().count() * 100
    country_list.loc[country_list['High_Earners'].idxmax()]
    country_list.loc[country_list['High_Earners_Ratio'].idxmax()]
    highest_earning_country = country_list.loc[country_list['High_Earners_Ratio'].idxmax(), 'native-country']
    highest_earning_country_percentage = round(country_list.loc[country_list['High_Earners_Ratio'].idxmax(), 'High_Earners_Ratio'],1)

# Identify the most popular occupation for those who earn >50K in India.
    indian_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = indian_high_earners['occupation'].mode().iloc[0]

# Round all decimals to the nearest tenth
    average_age_men = round(average_age_men, 1)
    percentage_bachelors = round(percentage_bachelors, 1)
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = round(lower_education_rich, 1)
    rich_percentage = round(rich_percentage, 1)
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

 # Print the results
    print("Race counts:\n", race_count)
    print("Average age of men:", average_age_men)
    print("Percentage of people with a Bachelor's degree:", percentage_bachelors, "%")
    print("Percentage of people with advanced education earning >50K:", higher_education_rich, "%")
    print("Percentage of people without advanced education earning >50K:", lower_education_rich, "%")
    print("Minimum number of hours per week:", min_work_hours)
    print("Percentage of people working minimum hours per week and earning >50K:", rich_percentage, "%")
    print("Country with the highest percentage of people earning >50K:", highest_earning_country)
    print("Country with the highest percentage of people earning >50K:", highest_earning_country_percentage)
    print("Most popular occupation for Indian high earners:", top_IN_occupation)

  # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
        print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
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
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
'''
# Calculate the percentage of people earning >50K for each country
country_high_earners_percentage = data[data['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100

# Find the country with the highest percentage of people earning >50K
highest_earning_country_percentage = country_high_earners_percentage.max()
highest_earning_country = country_high_earners_percentage.idxmax()

# Round the percentage to the nearest tenth
highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

# Print the result
print("Country with the highest percentage of people earning >50K:", highest_earning_country)
print("Percentage of people earning >50K in the highest earning country:", highest_earning_country_percentage, "%")

'''

