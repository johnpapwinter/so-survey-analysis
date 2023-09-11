import os
import pandas as pd
import constants
from dotenv import load_dotenv
from languages_cleaner import generate_answer_counter
from excel_service import export_to_excel

load_dotenv()

# GET SURVEY FILENAME AND CREATE DATAFRAME
csv_filename = os.getenv('SURVEY_2023')
df = pd.read_csv(csv_filename)


# FILTER THE DATAFRAME AND KEEP ONLY THE DESIRED COLUMNS
columns_to_keep = ['Employment', 'Country', 'LanguageHaveWorkedWith',
                   'DatabaseHaveWorkedWith', 'WebframeHaveWorkedWith']
filtered_df = df[columns_to_keep]

# FILTER THE DATAFRAME ONLY FOR THE COUNTRY NEEDED AND FULL-TIME EMPLOYMENT
list_of_countries = constants.COUNTRIES_LIST
target_employment = 'Employed, full-time'


for country in list_of_countries:
    temp_df = filtered_df[
        (filtered_df['Country'] == country) & (filtered_df['Employment'] == target_employment)]

    total_people = temp_df.shape[0]
    print(f"--------FOR {country.upper()}---------")
    print(generate_answer_counter(temp_df, 'LanguageHaveWorkedWith', total_people))
    print(generate_answer_counter(temp_df, 'WebframeHaveWorkedWith', total_people))
    print(generate_answer_counter(temp_df, 'DatabaseHaveWorkedWith', total_people))
    print(f"-----WITH A NUMBER OF RESPONDENTS: {total_people}----")
    print("====================================")

