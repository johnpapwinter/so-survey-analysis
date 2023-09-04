import os
import pandas as pd
import constants
from dotenv import load_dotenv
from collections import Counter
from utils import generate_answer_counter

load_dotenv()


list_of_countries = constants.COUNTRIES_LIST
final_df = pd.DataFrame()
files = [os.getenv('SURVEY_2022'), os.getenv('SURVEY_2023')]

for file in files:
    df = pd.read_csv(file)

    columns_to_keep = ['Employment', 'Country', 'LanguageHaveWorkedWith',
                       'DatabaseHaveWorkedWith', 'WebframeHaveWorkedWith']
    df = df[columns_to_keep]
    target_employment = 'Employed, full-time'
    df = df[(df['Country'] == 'Greece') & (df['Employment'] == target_employment)]
    df = df['LanguageHaveWorkedWith'].str.split(';').explode()
    df = df.value_counts().reset_index()

    if final_df.empty:
        final_df = df
    else:
        final_df = final_df.merge(df, on='LanguageHaveWorkedWith', how='outer')


final_df['count_x'].fillna(0, inplace=True)
final_df['count_y'].fillna(0, inplace=True)
print(final_df.head(10))
print('----------------------')
print(final_df.tail(10))
