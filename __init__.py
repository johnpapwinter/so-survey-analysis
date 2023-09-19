import os
import pandas as pd
import constants
from dotenv import load_dotenv
from data_processor import analyze_survey_language, analyze_survey_framework, analyze_survey_database
from data_visualizer import visualize_data

load_dotenv()

list_of_countries = constants.COUNTRIES_LIST
files = [os.getenv('SURVEY_2018'),
         os.getenv('SURVEY_2019'),
         os.getenv('SURVEY_2020'),
         os.getenv('SURVEY_2021'),
         os.getenv('SURVEY_2022'),
         os.getenv('SURVEY_2023')]

for country in list_of_countries:
    analyze_survey_language(country, files)
    analyze_survey_framework(country, files)
    analyze_survey_database(country, files)
    print('----------------------')
    print(f"RESULTS READY FOR {country.upper()}")
    print('----------------------')


visualize_data('languages.xlsx', 'Language')
visualize_data('frameworks.xlsx', 'Framework')
visualize_data('databases.xlsx', 'Database')

