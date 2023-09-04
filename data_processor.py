import os
import pandas as pd
import constants
from dotenv import load_dotenv

load_dotenv()


list_of_countries = constants.COUNTRIES_LIST
final_df = pd.DataFrame()
files = [os.getenv('SURVEY_2023'), os.getenv('SURVEY_2022'), os.getenv('SURVEY_2021'), os.getenv('SURVEY_2020'),
         os.getenv('SURVEY_2019'), os.getenv('SURVEY_2018'), os.getenv('SURVEY_2017')]
column_name_mappings = {"LanguageHaveWorkedWith": "Language"}

for file in files:
    df = pd.read_csv(file)

    target_employment = 'Employed, full-time'
    df = df[(df['Country'] == 'Greece') & (df['Employment'] == target_employment)]

    total_respondents = df.shape[0]
    df = df['LanguageHaveWorkedWith'].str.split(';').explode()
    df = df.value_counts().reset_index()

    df[df.columns[-1]] = (df[df.columns[-1]] / total_respondents) * 100

    filename = f"Survey_{file[-8:-4]}"

    if final_df.empty:
        final_df = df
        name_of_last_column = final_df.columns[-1]
        final_df.rename(columns={name_of_last_column: filename}, inplace=True)
    else:
        final_df = final_df.merge(df, on='LanguageHaveWorkedWith', how='outer')
        name_of_last_column = final_df.columns[-1]
        final_df.rename(columns={name_of_last_column: filename}, inplace=True)


final_df.rename(columns=column_name_mappings, inplace=True)
final_df.fillna(0, inplace=True)
print(final_df.head(10))
print('----------------------')
print(final_df.tail(10))
print('----------------------')

