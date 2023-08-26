import os
import pandas as pd
from collections import Counter
from dotenv import load_dotenv

load_dotenv()

# GET SURVEY FILENAME AND CREATE DATAFRAME
csv_filename = os.getenv('SURVEY_2023')
df = pd.read_csv(csv_filename)

# GET THE LIST OF COLUMNS IN THE SURVEY
col_list = df.columns.tolist()
print(col_list)

# FILTER THE DATAFRAME AND KEEP ONLY THE DESIRED COLUMNS
columns_to_keep = ['Employment', 'Country', 'LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith',
                   'WebframeHaveWorkedWith', 'ToolsTechHaveWorkedWith']
filtered_df = df[columns_to_keep]

# FILTER THE DATAFRAME ONLY FOR THE COUNTRY NEEDED AND FULL-TIME EMPLOYMENT
countries = ['France', 'Ireland', 'Germany', 'Netherlands', 'Canada', 'Greece', 'Albania', 'Serbia', 'Bulgaria',
             'Romania', 'New Zealand', 'Japan', 'Singapore', 'Australia', 'Austria', 'Spain', 'Portugal', 'Turkey',
             'Croatia', 'Poland', 'Czech Republic', 'Italy']
target_country = 'France'
target_employment = 'Employed, full-time'
employees_df = filtered_df['Employment'] == target_employment
target_df = filtered_df[(filtered_df['Country'] == target_country) & (filtered_df['Employment'] == target_employment)]

# GET THE TOTAL NUMBER OF RESPONDENTS
total_respondents = target_df.shape[0]
print(total_respondents)

# GET A DICT OF ALL PROGRAMMING LANGUAGES AND NUMBER OF TIMES APPEARED
all_programming_languages = ";".join(target_df['LanguageHaveWorkedWith'].astype(str))
all_programming_languages = all_programming_languages.split(";")
languages_counts = Counter(all_programming_languages)
print(languages_counts)


# GET A DICT OF ALL WEB FRAMEWORKS AND NUMBER OF TIMES APPEARED
all_web_frames = ";".join(target_df['WebframeHaveWorkedWith'].astype(str))
all_web_frames = all_web_frames.split(";")
web_frames_counts = Counter(all_web_frames)
print(web_frames_counts)

# GET A DICT OF ALL DATABASES AND NUMBER OF TIMES APPEARED
all_databases = ";".join(target_df['DatabaseHaveWorkedWith'].astype(str))
all_databases = all_databases.split(";")
databases_counts = Counter(all_databases)
print(databases_counts)

# GET A DICT OF ALL TECH TOOLS AND NUMBER OF TIMES APPEARED
all_tools = ";".join(target_df['ToolsTechHaveWorkedWith'].astype(str))
all_tools = all_tools.split(";")
tools_counts = Counter(all_tools)
print(tools_counts)


