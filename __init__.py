import os
import pandas as pd
import constants
from collections import Counter
from dotenv import load_dotenv
from utils import calculate_percentages, generate_answer_counter

load_dotenv()

# GET SURVEY FILENAME AND CREATE DATAFRAME
csv_filename = os.getenv('SURVEY_2023')
df = pd.read_csv(csv_filename)

# GET THE LIST OF COLUMNS IN THE SURVEY
# col_list = df.columns.tolist()
# print(col_list)

# FILTER THE DATAFRAME AND KEEP ONLY THE DESIRED COLUMNS
columns_to_keep = ['Employment', 'Country', 'LanguageHaveWorkedWith',
                   'DatabaseHaveWorkedWith', 'WebframeHaveWorkedWith']
filtered_df = df[columns_to_keep]

# FILTER THE DATAFRAME ONLY FOR THE COUNTRY NEEDED AND FULL-TIME EMPLOYMENT
list_of_countries = constants.COUNTRIES_LIST
# target_country = 'Israel'
target_employment = 'Employed, full-time'
# employees_df = filtered_df['Employment'] == target_employment
# target_df = filtered_df[(filtered_df['Country'] == target_country) & (filtered_df['Employment'] == target_employment)]
#
# # GET THE TOTAL NUMBER OF RESPONDENTS
# total_respondents = target_df.shape[0]
# print(total_respondents)
#
# # GET A DICT OF ALL PROGRAMMING LANGUAGES AND NUMBER OF TIMES APPEARED
# all_programming_languages = ";".join(target_df['LanguageHaveWorkedWith'].astype(str))
# all_programming_languages = all_programming_languages.split(";")
# languages_counts = Counter(all_programming_languages)
# print(f"Total numbers of languages")
# print(languages_counts)
# print("Percentages of languages")
# print(calculate_percentages(dict(languages_counts), total_respondents))
#
#
# # GET A DICT OF ALL WEB FRAMEWORKS AND NUMBER OF TIMES APPEARED
# all_web_frames = ";".join(target_df['WebframeHaveWorkedWith'].astype(str))
# all_web_frames = all_web_frames.split(";")
# web_frames_counts = Counter(all_web_frames)
# print(f"Total numbers of frameworks")
# print(web_frames_counts)
# print("Percentages of frameworks")
# print(calculate_percentages(dict(web_frames_counts), total_respondents))
#
# # GET A DICT OF ALL DATABASES AND NUMBER OF TIMES APPEARED
# all_databases = ";".join(target_df['DatabaseHaveWorkedWith'].astype(str))
# all_databases = all_databases.split(";")
# databases_counts = Counter(all_databases)
# print(f"Total numbers of databases")
# print(databases_counts)
# print("Percentages of databases")
# print(calculate_percentages(dict(databases_counts), total_respondents))


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

